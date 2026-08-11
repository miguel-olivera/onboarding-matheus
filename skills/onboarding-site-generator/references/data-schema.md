# data.json schema

This is the shape `scripts/build_onboarding.py` expects. It mirrors the JS
data structures already used by the rendering engine in `assets/template.html`
(the `MODULES` array and `DEFAULT_PROFILE` object) — nothing here is a new
format, it's just the same shape lifted into a standalone JSON file so it can
be assembled once and handed to the build script.

Top level:

```json
{
  "profile": { ... },
  "buddy": { ... },
  "modules": [ ... ]
}
```

## profile

```json
{"name": "Dom", "role": "Staff UX Designer", "date": ""}
```

- `name` — used for greeting ("Hi, Dom 👋"), the page title, the footer, and
  the `localStorage` key that stores progress (so two people never collide).
  First name is enough; if you only have a full name the page extracts the
  first word automatically at render time.
- `role` — shown under the name in a couple of places. Match whatever title
  the person actually has (Staff/Sr/Ssr + craft), not a generic placeholder.
- `date` — currently unused by the template but kept for forward
  compatibility; pass `""` if you don't have one.

## buddy

```json
{
  "name": "Miguel Olivera",
  "note": "Your point of reference during onboarding — he'll check in on you, reach out anytime.",
  "slackUrl": "https://deliveryhero.enterprise.slack.com/team/U0LHTEFTP",
  "avatarDataUri": "data:image/jpeg;base64,..."
}
```

- `slackUrl` must be a real, resolved Slack profile link (`/team/<ID>`), never
  a placeholder or a guessed ID — see `references/slack-links.md`.
- `avatarDataUri` is a `data:image/...;base64,...` string so the final HTML
  stays a single self-contained file with zero external requests. Ask the
  requesting manager for a photo, or reuse the buddy's existing avatar if
  they've already appeared in a previous onboarding page.

## modules

An ordered array. Each entry renders as one accordion module. Two module
"families" exist, distinguished by `trackable`:

- **Trackable modules** (`trackable` omitted, or `true`) — these are the
  "Your first weeks" modules (Week 1, Week 2, After your first month, ...).
  They have checkboxes, they count toward the progress bar, badge shelf, and
  the 100% confetti celebration.
- **Non-trackable modules** (`trackable:false`) — the "Resource hub". Pure
  reference material: no checkboxes, no counting, always available. This
  matters because the Resource Hub is meant to be looked at repeatedly, not
  "completed" — don't set `trackable:false` on anything that's actually a
  first-weeks task, or it'll silently stop counting toward progress.

Common module fields:

```json
{
  "id": "week1",
  "icon": "1️⃣",
  "sectionLabel": "Your first weeks",
  "title": "Week 1: Welcome to Glovo",
  "blurb": "Get your hardware, software and access sorted, and meet the team.",
  "trackable": true,
  "poc": {"name": "Anna Kebets", "email": "anna.kebets@glovoapp.com", "slackId": "U02NHDQSX0C", "roleLabel": "OKR lead"},
  "items": [ ... ],
  "peopleGroups": [ ... ],
  "spotlight": { ... },
  "closingNote": "Optional closing line shown at the bottom of the module."
}
```

- `id` — unique, kebab-case, stable (used for the `localStorage` progress
  key of every item inside — don't rename an id between edits of the same
  person's page or their saved progress resets for that item).
- `sectionLabel` — only set this on the *first* module of a new section; it
  renders as a divider/heading above the module (e.g. "Your first weeks",
  "Resource hub — come back to these anytime"). Leave it out on every
  subsequent module in the same section.
- `poc` — a single point of contact for the whole module. `roleLabel`
  defaults to "Point of contact" if omitted.

### items[]

```json
{"id": "week1-3", "label": "Request <b>Google Drive</b> access", "tooltip": "optional hover explainer", "links": [{"text": "Mariana on Slack", "url": "https://..."}], "note": "optional small print under the item"}
```

`label` accepts inline HTML (`<b>`) for emphasis — keep it to bold only, no
other tags. `id` must be unique across the *entire* modules array, not just
within one module.

### peopleGroups[]

Used for "people to meet" / "who to shadow" / "points of contact" — the part
that's genuinely different for every new joiner, since it depends on their
team, craft, and scope. Never invent names here — always ask the requesting
manager, or read them from the input folder (see `SKILL.md`).

```json
{
  "title": "Meet the UX Design team",
  "checkable": true,
  "actionPrefix": "Meet",
  "note": "optional context line",
  "link": {"text": "optional single link", "url": "https://..."},
  "otherMembersNote": "optional 'also on this team: ...' line",
  "people": [
    {"id": "week1-meet-jack", "name": "Jack Coles", "note": "Intro to Food", "slackId": "USNLGLV8C"},
    {"id": "week1-meet-combo", "combine": [{"name": "Alicia Fundora", "slackId": "..."}, {"name": "Beatriz Ruette", "slackId": "..."}], "note": "Visual & Motion Design — joint intro"}
  ]
}
```

- `checkable: true` gives each person row its own checkbox that counts toward
  the module's progress, same as a normal item.
- Use `combine` instead of `name`/`slackId` when two people share one intro
  session/row (e.g. a joint intro).
- `slackId` is the raw Slack member ID (the `U0...` string), not a URL — the
  template builds the `/team/<slackId>` link itself.

### spotlight (OKR-style modules only)

```json
{
  "title": "🌟 Your stream: Accelerate execution",
  "leadTemplate": "Lead: {name}",
  "initiatives": [
    {"name": "Repository Governance, Architecture & Discoverability", "lead": "Camilla Chang", "status": "On track", "jira": "PUX-4481", "url": "https://glovoapp.atlassian.net/browse/PUX-4481"}
  ]
}
```

`spotlight` is optional — the template only renders it `if(m.spotlight)`, so
when the intake didn't turn up a specific OKR stream (it isn't part of the
standard form, see `SKILL.md`), just omit the key entirely rather than
inventing initiatives. Same goes for the two stream-specific `items` in the
OKR module (`okr-5`, `okr-6` in the content library) — drop them if there's
no real stream to point to.

## Fields that stay the same for almost everyone

The Resource Hub modules (`org`, `process`, `competency`, `leads`, `research`,
`localization`, `pintxo`, `a11y`, `okr`'s items-but-not-spotlight) rarely
change between people on the same craft — see
`references/content-library-design-craft.md` for a ready-to-copy version of
all of these. Start there and only edit what's genuinely different for this
person (usually just the `okr.spotlight` and any `poc` that changed since a
reorg).
