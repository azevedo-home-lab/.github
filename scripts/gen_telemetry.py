#!/usr/bin/env python3
"""Generate profile/assets/telemetry.svg from live GitHub org data.

Reads ORG_PAT (fine-grained org-read PAT) or GITHUB_TOKEN from the
environment. Exits 1 when most repos are unreadable, so a scheduled run
never commits near-zero data by mistake.
"""
import datetime
import json
import os
import sys
import time
import urllib.request

ORG = "azevedo-home-lab"
OUT = os.path.join(os.path.dirname(__file__), "..", "profile", "assets", "telemetry.svg")
TOKEN = os.environ.get("ORG_PAT") or os.environ.get("GITHUB_TOKEN") or ""
FONT = "Futura, 'Century Gothic', 'URW Gothic', sans-serif"

INK = "#1f2328"
MUTED = "#57606a"
FRAME = "#d0d7de"
BLUE = "#0969da"
RED = "#c1121f"


def api(path, ok404=False):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"},
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req) as r:
                if r.status == 202:  # stats still computing
                    time.sleep(3)
                    continue
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 202:
                time.sleep(3)
                continue
            if ok404 and e.code in (403, 404):
                return None
            raise
    return None


def main():
    repos = [r["name"] for r in api(f"/orgs/{ORG}/repos?per_page=100&type=all")]
    weeks = [0] * 52
    readable = 0
    alerts = 0
    for name in repos:
        part = api(f"/repos/{ORG}/{name}/stats/participation", ok404=True)
        if part and "all" in part:
            readable += 1
            for i, v in enumerate(part["all"]):
                weeks[i] += v
        a = api(f"/repos/{ORG}/{name}/dependabot/alerts?state=open&per_page=100", ok404=True)
        if a is not None:
            alerts += len(a)
    if readable < len(repos) / 2:
        sys.exit(f"only {readable}/{len(repos)} repos readable — token lacks org read access, refusing to write")

    prs = api(f"/search/issues?q=org:{ORG}+is:pr+is:open")["total_count"]
    bugs = api(f"/search/issues?q=org:{ORG}+is:issue+is:open+type:Bug")["total_count"]
    last12 = weeks[-12:]
    total = sum(last12)

    today = datetime.date.today()
    week_start = today - datetime.timedelta(days=(today.weekday() + 1) % 7)  # Sunday
    dates = [week_start - datetime.timedelta(weeks=11 - i) for i in range(12)]

    peak = max(last12) or 1
    x0, x1, base, hmax = 90, 1190, 300, 120
    slot = (x1 - x0) / 12
    bars, labels = [], []
    for i, v in enumerate(last12):
        cx = x0 + slot * (i + 0.5)
        h = max(round(v * hmax / peak), 1 if v else 1)
        if v:
            bars.append(f'<rect x="{cx-15:.0f}" y="{base-h}" width="30" height="{h}" fill="{BLUE}"/>')
        else:
            bars.append(f'<rect x="{cx-15:.0f}" y="{base-1}" width="30" height="1" fill="{FRAME}"/>')
        if v and (v == max(last12) or i == 11):
            labels.append(f'<text x="{cx:.0f}" y="{base-h-8}" text-anchor="middle" font-size="11" fill="{INK}">{v}</text>')
    ticks = "".join(
        f'<text x="{x0 + slot * (i + 0.5):.0f}" y="320" text-anchor="middle" font-size="10" letter-spacing="2" fill="{MUTED}">{dates[i].strftime("%b %d").upper()}</text>'
        for i in (0, 4, 8, 11)
    )

    stamp = today.isoformat()
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 340" width="1280" height="340" role="img" aria-label="Org telemetry: {total} commits in 12 weeks, {prs} open pull requests, {bugs} open bugs, {alerts} open Dependabot alerts">
  <rect width="1280" height="340" fill="#ffffff"/>
  <rect x="0.5" y="0.5" width="1279" height="339" fill="none" stroke="{FRAME}" stroke-width="1"/>
  <g font-family="{FONT}">
    <text x="90" y="30" fill="{MUTED}" font-size="10" letter-spacing="3">ORG TELEMETRY — ALL REPOSITORIES</text>
    <text x="1190" y="30" text-anchor="end" fill="{MUTED}" font-size="10" letter-spacing="2">SNAPSHOT {stamp}</text>
    <g text-anchor="middle">
      <text x="190" y="98" fill="{BLUE}" font-size="46">{total}</text>
      <text x="190" y="122" fill="{MUTED}" font-size="10" letter-spacing="4">COMMITS · 12 WEEKS</text>
      <text x="490" y="98" fill="{BLUE}" font-size="46">{prs}</text>
      <text x="490" y="122" fill="{MUTED}" font-size="10" letter-spacing="4">OPEN PULL REQUESTS</text>
      <text x="790" y="98" fill="{BLUE}" font-size="46">{bugs}</text>
      <text x="790" y="122" fill="{MUTED}" font-size="10" letter-spacing="4">OPEN BUGS</text>
      <text x="1090" y="98" fill="{RED}" font-size="46">{alerts}</text>
      <text x="1090" y="122" fill="{RED}" font-size="10" letter-spacing="4">DEPENDABOT ALERTS</text>
    </g>
    <text x="90" y="172" fill="{MUTED}" font-size="10" letter-spacing="3">COMMITS PER WEEK</text>
    {"".join(labels)}
    {ticks}
  </g>
  <line x1="90" y1="148" x2="1190" y2="148" stroke="{FRAME}" stroke-width="1"/>
  {"".join(bars)}
  <line x1="90" y1="300" x2="1190" y2="300" stroke="{FRAME}" stroke-width="1"/>
</svg>
'''
    with open(os.path.abspath(OUT), "w") as f:
        f.write(svg)
    print(f"wrote {OUT}: {total} commits/12w, {prs} PRs, {bugs} bugs, {alerts} alerts ({readable}/{len(repos)} repos)")


if __name__ == "__main__":
    main()
