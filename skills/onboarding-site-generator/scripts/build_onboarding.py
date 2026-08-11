#!/usr/bin/env python3
"""
Renders a new-joiner onboarding HTML page from assets/template.html + a data.json.

Usage:
    python3 build_onboarding.py <data.json> [output.html]

If output.html is omitted, writes "Onboarding-<profile.name>-EN.html" into the
current working directory, spaces in the name replaced with "-".

The data.json must match references/data-schema.md. This script does no content
generation or validation of business logic (missing Slack IDs, wrong crafts,
etc.) -- that judgment call belongs to whoever (or whichever Claude session)
assembled data.json. This script only does the mechanical find-and-replace into
the template, so a placeholder can never leak into the final HTML by accident.
"""
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = SKILL_DIR / "assets" / "template.html"

REQUIRED_TOP_LEVEL = ["profile", "buddy", "modules"]
REQUIRED_BUDDY = ["name", "note", "slackUrl", "avatarDataUri"]
REQUIRED_PROFILE = ["name", "role"]


def load_data(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    missing = [k for k in REQUIRED_TOP_LEVEL if k not in data]
    if missing:
        raise ValueError(f"data.json is missing top-level keys: {missing}")
    missing = [k for k in REQUIRED_PROFILE if k not in data["profile"]]
    if missing:
        raise ValueError(f"profile is missing keys: {missing}")
    missing = [k for k in REQUIRED_BUDDY if k not in data["buddy"]]
    if missing:
        raise ValueError(f"buddy is missing keys: {missing}")
    if not isinstance(data["modules"], list) or not data["modules"]:
        raise ValueError("modules must be a non-empty array")
    return data


def render(data):
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    profile = data["profile"]
    buddy = data["buddy"]
    modules = data["modules"]

    replacements = {
        "{{TITLE}}": f"{profile['name']}'s UX Onboarding · Glovo",
        "{{BUDDY_AVATAR_DATA_URI}}": buddy["avatarDataUri"],
        "{{BUDDY_NAME}}": buddy["name"],
        "{{BUDDY_NOTE}}": buddy["note"],
        "{{BUDDY_SLACK_URL}}": buddy["slackUrl"],
        "{{FOOTER_TEXT}}": f"{profile['name']}’s UX onboarding · Glovo — your progress is saved in this browser.",
        "{{MODULES_JSON}}": json.dumps(modules, ensure_ascii=False),
        "{{PROFILE_JSON}}": json.dumps(
            {"name": profile["name"], "role": profile["role"], "date": profile.get("date", "")},
            ensure_ascii=False,
        ),
    }

    out = template
    for key, value in replacements.items():
        if key not in out:
            raise ValueError(f"template is missing placeholder {key} -- was it edited?")
        out = out.replace(key, value)

    leftover = re.findall(r"\{\{[A-Z_]+\}\}", out)
    if leftover:
        raise ValueError(f"unreplaced placeholders left in output: {sorted(set(leftover))}")

    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    data_path = Path(sys.argv[1])
    data = load_data(data_path)
    html = render(data)

    if len(sys.argv) >= 3:
        out_path = Path(sys.argv[2])
    else:
        safe_name = data["profile"]["name"].strip().replace(" ", "-")
        out_path = Path.cwd() / f"Onboarding-{safe_name}-EN.html"

    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
