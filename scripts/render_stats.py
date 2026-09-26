#!/usr/bin/env python3
"""Render public GitHub profile SVG cards using Python's standard library.

Usage: PROFILE_USERNAME=your-login GITHUB_TOKEN=... python3 scripts/render_stats.py
The token is optional for public REST data and required for the contribution
calendar. Only public repository endpoints and aggregate calendar counts are used.
"""

import argparse
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


API_ROOT = "https://api.github.com"
BACKGROUND = "#0d1117"
PANEL = "#161b22"
ACCENT = "#61dafb"
TEXT = "#c9d1d9"
MUTED = "#8b949e"
LANGUAGE_COLORS = {
    "Python": "#3572a5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "HTML": "#e34c26", "CSS": "#563d7c", "Java": "#b07219",
    "Kotlin": "#a97bff", "C": "#555555", "C++": "#f34b7d",
    "C#": "#178600", "Go": "#00add8", "Rust": "#dea584",
    "Shell": "#89e051", "Dart": "#00b4ab", "Swift": "#f05138",
    "Jupyter Notebook": "#da5b0b", "Ruby": "#701516", "PHP": "#4f5d95",
    "Other": MUTED,
}


class DataError(RuntimeError):
    """A source is unavailable or does not contain the expected public data."""


def integer(value, label):
    if type(value) is not int or value < 0:
        raise DataError(f"Invalid nonnegative integer for {label}.")
    return value


class GitHub:
    def __init__(self, token=None):
        self.token = token

    def request(self, path, payload=None):
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "public-profile-svg-cards",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        body = None
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = Request(API_ROOT + path, data=body, headers=headers)
        try:
            with urlopen(request, timeout=30) as response:
                if response.status != 200:
                    raise DataError(f"GitHub returned HTTP {response.status} for {path}.")
                return json.load(response)
        except HTTPError as exc:
            # Do not print response bodies, tokens, or private API content.
            raise DataError(f"GitHub returned HTTP {exc.code} for {path}; check access and rate limits.") from exc
        except (URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise DataError(f"Could not read GitHub data for {path}: {type(exc).__name__}.") from exc

    def public_user(self, username):
        result = self.request("/users/" + quote(username, safe=""))
        if not isinstance(result, dict) or not result.get("login"):
            raise DataError("GitHub did not return a public user profile.")
        for field in ("public_repos", "followers", "following"):
            integer(result.get(field), field)
        return result

    def public_repositories(self, username):
        repositories = []
        seen = set()
        for page in range(1, 1001):
            query = urlencode({"type": "owner", "sort": "full_name", "per_page": 100, "page": page})
            result = self.request(f"/users/{quote(username, safe='')}/repos?{query}")
            if not isinstance(result, list):
                raise DataError("GitHub did not return a public repository list.")
            for repository in result:
                if not isinstance(repository, dict) or repository.get("private") is not False:
                    raise DataError("The public repository endpoint returned unexpected visibility.")
                repo_id = integer(repository.get("id"), "repository ID")
                if repo_id in seen:
                    raise DataError("Repository pagination changed during this run; retry the refresh.")
                seen.add(repo_id)
                if not isinstance(repository.get("name"), str):
                    raise DataError("A public repository is missing its name.")
                owner = repository.get("owner", {}).get("login", "")
                if owner.lower() != username.lower():
                    raise DataError("A public repository has an unexpected owner.")
                if type(repository.get("fork")) is not bool:
                    raise DataError("A public repository is missing its fork status.")
                integer(repository.get("stargazers_count"), "repository stars")
                repositories.append(repository)
            if len(result) < 100:
                return repositories
        raise DataError("Repository pagination exceeded the supported limit.")

    def public_languages(self, username, repositories):
        totals = Counter()
        for repository in repositories:
            if repository["fork"]:
                continue
            path = f"/repos/{quote(username, safe='')}/{quote(repository['name'], safe='')}/languages"
            result = self.request(path)
            if not isinstance(result, dict):
                raise DataError("GitHub did not return public repository language bytes.")
            for language, amount in result.items():
                if not isinstance(language, str) or not language:
                    raise DataError("GitHub returned an invalid language name.")
                totals[language] += integer(amount, "language bytes")
        return dict(totals)

    def contribution_calendar(self, username, now):
        if not self.token:
            return None
        # This query asks for aggregate public-facing graph counts only. It
        # never requests private repository names, commits, or contribution URLs.
        query = """query($login: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $login) {
            contributionsCollection(from: $from, to: $to) {
              contributionCalendar {
                totalContributions
                weeks { contributionDays { date contributionCount } }
              }
            }
          }
        }"""
        result = self.request("/graphql", {
            "query": query,
            "variables": {
                "login": username,
                "from": (now - timedelta(days=364)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat(),
                "to": now.isoformat(),
            },
        })
        if not isinstance(result, dict) or result.get("errors"):
            raise DataError("The GitHub contribution calendar query failed; existing cards were preserved.")
        try:
            calendar = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        except (KeyError, TypeError) as exc:
            raise DataError("GitHub did not return a contribution calendar.") from exc
        return calendar


def calendar_statistics(calendar, today):
    """Compute streaks inside the returned range, allowing a zero-count today.

    The longest streak is explicitly restricted to the available calendar; it
    is never presented as an all-time record. Unknown or missing days are errors.
    """
    if not isinstance(calendar, dict) or not isinstance(calendar.get("weeks"), list):
        raise DataError("Invalid contribution calendar.")
    api_total = integer(calendar.get("totalContributions"), "calendar total")
    days = {}
    for week in calendar["weeks"]:
        if not isinstance(week, dict) or not isinstance(week.get("contributionDays"), list):
            raise DataError("Invalid contribution calendar week.")
        for entry in week["contributionDays"]:
            try:
                day = date.fromisoformat(entry["date"])
                count = integer(entry["contributionCount"], "daily contributions")
            except (KeyError, TypeError, ValueError) as exc:
                raise DataError("Invalid contribution calendar day.") from exc
            if day in days:
                raise DataError("The contribution calendar contains duplicate dates.")
            if day > today:
                if count:
                    raise DataError("The contribution calendar contains future contributions.")
                continue
            days[day] = count
    if not days:
        raise DataError("The contribution calendar is empty.")
    start, end = min(days), max(days)
    if end != today:
        raise DataError("The contribution calendar does not reach the current UTC date.")
    if len(days) != (end - start).days + 1:
        raise DataError("The contribution calendar has missing dates.")
    if sum(days.values()) != api_total:
        raise DataError("The calendar total does not match its daily counts.")
    longest = running = 0
    for day in sorted(days):
        running = running + 1 if days[day] > 0 else 0
        longest = max(longest, running)
    cursor = today if days[today] > 0 else today - timedelta(days=1)
    current = 0
    while cursor in days and days[cursor] > 0:
        current += 1
        cursor -= timedelta(days=1)
    return {"current": current, "longest": longest, "total": api_total,
            "start": start, "end": end, "days": len(days)}


def text(x, y, value, size=12, color=TEXT, weight=400, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>')


def card(title, description, content, height=200):
    return '\n'.join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="390" height="{height}" viewBox="0 0 390 {height}" role="img" aria-labelledby="card-title card-description">',
        f'<title id="card-title">{escape(title)}</title>',
        f'<desc id="card-description">{escape(description)}</desc>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif}</style>',
        f'<rect x="0.5" y="0.5" width="389" height="{height - 1}" rx="14" fill="{BACKGROUND}" stroke="#30363d"/>',
        f'<path d="M21 53H369" stroke="{PANEL}" stroke-width="2"/>',
        text(21, 33, title, 16, ACCENT, 600),
        *content,
        '</svg>',
        '',
    ])


def compact(value):
    return f"{value:,}" if value < 10000 else f"{value / 1000:.1f}k"


def render_stats(user, repositories, refreshed):
    stars = sum(integer(repo.get("stargazers_count"), "stars") for repo in repositories)
    metrics = [("Public repositories", user["public_repos"]), ("Stars received", stars),
               ("Followers", user["followers"]), ("Following", user["following"])]
    content = []
    for index, (label, value) in enumerate(metrics):
        x = 22 + (index % 2) * 184
        y = 84 + (index // 2) * 60
        content.extend([text(x, y, compact(value), 24, TEXT, 600), text(x, y + 19, label, 11, MUTED)])
    content.append(text(22, 187, f"Public profile · refreshed {refreshed.isoformat()} UTC", 10, MUTED))
    description = f"Public statistics for {user['login']}. " + "; ".join(f"{label}: {value}" for label, value in metrics) + ". Stars are summed across owned public repositories."
    return card("GitHub at a glance", description, content)


def render_streak(statistics, refreshed):
    if statistics is None:
        return card("Contribution rhythm", "The contribution calendar is unavailable because no GitHub token was supplied. No contribution counts were estimated.", [
            text(22, 90, "Contribution calendar unavailable", 15, TEXT, 600),
            text(22, 119, "A GitHub token is needed to refresh this card.", 12, MUTED),
            text(22, 141, "No contribution counts have been estimated.", 12, MUTED),
            text(22, 181, f"Checked {refreshed.isoformat()} UTC", 10, MUTED),
        ])
    metrics = [("Current streak", statistics["current"]), ("Longest in range", statistics["longest"]), ("Contributions", statistics["total"])]
    content = []
    for index, (label, value) in enumerate(metrics):
        center = 67 + index * 128
        if index < 2:
            content.append(f'<path d="M{132 + index * 128} 75V132" stroke="{PANEL}" stroke-width="2"/>')
        content.extend([text(center, 97, compact(value), 28, ACCENT if index == 0 else TEXT, 600, "middle"),
                        text(center, 120, label, 10, MUTED, 400, "middle")])
    content.extend([
        text(22, 158, f"{statistics['start'].isoformat()} — {statistics['end'].isoformat()}", 11, MUTED),
        text(22, 181, "Streaks in days · today may still be in progress", 10, MUTED),
    ])
    description = (f"Visible contribution calendar from {statistics['start']} through {statistics['end']}: "
                   f"{statistics['total']} contributions, current streak {statistics['current']} days, "
                   f"longest streak within this range {statistics['longest']} days. "
                   "A zero-count current UTC day does not break yesterday's active streak. These are not all-time statistics.")
    return card("Contribution rhythm", description, content)


def render_languages(languages, refreshed):
    ordered = sorted(((name, integer(amount, "language bytes")) for name, amount in languages.items() if amount),
                     key=lambda item: (-item[1], item[0]))
    total = sum(amount for _, amount in ordered)
    if not total:
        return card("Languages in public code", "GitHub reports no language bytes for the owned public non-fork repositories.", [
            text(22, 92, "No public language data yet", 15, TEXT, 600),
            text(22, 119, "Language shares will appear as code is published.", 12, MUTED),
            text(22, 181, "Owned public repositories · forks excluded", 10, MUTED),
        ])
    displayed = ordered[:4]
    if len(ordered) > 4:
        displayed.append(("Other", sum(amount for _, amount in ordered[4:])))
    content = ['<defs><clipPath id="language-bar"><rect x="22" y="72" width="346" height="12" rx="6"/></clipPath></defs>',
               '<g clip-path="url(#language-bar)">']
    offset = 22.0
    for index, (name, amount) in enumerate(displayed):
        width = 346 * amount / total
        color = LANGUAGE_COLORS.get(name, ("#61dafb", "#a78bfa", "#34d399", "#fbbf24")[index % 4])
        content.append(f'<rect x="{offset:.3f}" y="72" width="{width:.3f}" height="12" fill="{color}"/>')
        offset += width
    content.append('</g>')
    for index, (name, amount) in enumerate(displayed):
        x = 22 + (index % 2) * 179
        y = 111 + (index // 2) * 25
        color = LANGUAGE_COLORS.get(name, ("#61dafb", "#a78bfa", "#34d399", "#fbbf24")[index % 4])
        short_name = name if len(name) <= 15 else name[:14] + "…"
        content.extend([f'<circle cx="{x + 4}" cy="{y - 4}" r="4" fill="{color}"/>',
                        text(x + 14, y, short_name, 11),
                        text(x + 162, y, f"{amount / total:.1%}", 10, MUTED, 400, "end")])
    content.append(text(22, 187, "Public non-fork repositories · share of language bytes", 10, MUTED))
    description = "Language bytes across owned public non-fork repositories: " + "; ".join(f"{name}: {amount:,} bytes ({amount / total:.1%})" for name, amount in ordered) + ". This measures code volume, not skill or time spent."
    return card("Languages in public code", description, content)


def write_cards(output_dir, cards):
    """Prepare every SVG before replacing files; fetch errors leave files intact."""
    output_dir.mkdir(parents=True, exist_ok=True)
    pending = []
    try:
        for name, contents in cards.items():
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=output_dir, suffix=".tmp", delete=False) as handle:
                temporary = Path(handle.name)
                pending.append((temporary, output_dir / name))
                handle.write(contents)
            temporary.chmod(0o644)
        for temporary, destination in pending:
            os.replace(temporary, destination)
    finally:
        for temporary, _ in pending:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default=os.environ.get("PROFILE_USERNAME", "abhijithviswanathan"))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1] / "dist")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", args.username):
        parser.error("Invalid GitHub username.")
    now = datetime.now(timezone.utc)
    try:
        client = GitHub(os.environ.get("GITHUB_TOKEN") or None)
        user = client.public_user(args.username)
        repositories = client.public_repositories(args.username)
        languages = client.public_languages(args.username, repositories)
        calendar = client.contribution_calendar(args.username, now)
        statistics = calendar_statistics(calendar, now.date()) if calendar is not None else None
        cards = {"stats.svg": render_stats(user, repositories, now.date()),
                 "streak.svg": render_streak(statistics, now.date()),
                 "languages.svg": render_languages(languages, now.date())}
        write_cards(args.output_dir, cards)
    except (DataError, OSError) as exc:
        print(f"Profile card refresh failed: {exc}", file=sys.stderr)
        return 1
    print(f"Updated {len(cards)} public profile cards in {args.output_dir}.")
    if calendar is None:
        print("No GITHUB_TOKEN supplied: the streak card explicitly reports that the calendar is unavailable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
