---
name: onboarding-site-generator
description: Generates a self-contained, interactive HTML onboarding page (progress bar, checklists, badges, confetti celebration) for a new joiner on Glovo's UX team, in the Pintxo Design System look and feel. Use this whenever a UX team manager wants to build, generate, create, or update an onboarding page/site/microsite for a new hire or new joiner, or mentions "onboarding" together with a person's name/role. Currently scoped to the UX/Product Design craft — say so up front if the new joiner is Research, Content/Localization, or another craft, since the bundled content library doesn't cover them yet.
---

# Onboarding site generator (Glovo UX team)

Produces one HTML file per new joiner: a self-contained page (no external
requests, works opened straight from Finder) with a hero banner, a buddy
callout, a progress bar + badges, and an accordion of modules — some
trackable ("Your first weeks"), some pure reference ("Resource hub"). This
packages the process used to build the team's first interactive onboarding
page so any manager can repeat it for their own new joiner.

**The Resource Hub modules are intentionally hidden today.**
`assets/template.html` has `var SHOW_RESOURCE_HUB = false;` — by design, not
a bug — so the 9 reference modules never render even though they're fully
built into `data.json`/`MODULES`. Still build them into every `data.json` as
described below (the content is there for whenever the hub gets switched on),
just don't be surprised that they don't show up when you preview a page.
Don't flip this flag without checking first — it was confirmed as
intentional.

**Scope today: UX/Product Design craft only.** The bundled content library
(`references/content-library-design-craft.md`) covers Design. If the person
joining is Research, Content/Localization, Motion, or anything else, tell the
requester clearly that this craft isn't covered yet, and fall back to
gathering *all* content conversationally (don't silently reuse the Design
library — it will contain wrong tools/links for a different craft). Consider
saving what you learn as a new `content-library-<craft>.md` for next time.

## Why a template + script instead of writing HTML from scratch

Writing the full page by hand each time (like the very first version of this
page) is slow and risks tiny drifts in the CSS/JS engine between people.
Instead:

- `assets/template.html` already contains the CSS, the JS progress/badge/
  confetti engine, and the embedded Glovo Sans fonts (base64, offline-safe) —
  copied verbatim from the first working version of this page. It has 8 placeholders
  (`{{TITLE}}`, `{{BUDDY_NAME}}`, etc.) for the parts that vary by person.
- `scripts/build_onboarding.py` takes a `data.json` (the content you gather
  and decide, per person) and mechanically substitutes it into the template.
  It refuses to write a file if any placeholder is left unfilled or the JSON
  is missing required fields — so a bad or incomplete `data.json` fails loud
  instead of shipping a broken page.

Your job is everything *upstream* of the script: gathering and judging the
right content. The script's job is purely the mechanical assembly — don't
hand-edit its output HTML afterwards; fix `data.json` and re-run it instead,
so the file stays regeneratable.

## Workflow

**Everything you ask the requester stays in English, always** — the 8
questions below, any follow-up or clarifying question (a missing Slack
handle, "which project did you mean", a photo request, etc.), and anything
you ask outside the numbered list. This holds no matter what language the
requester is chatting in, including Spanish, since the generated onboarding
pages are English-only and the intake should match end to end. It's easy to
slip into the requester's language for an off-script follow-up — actively
watch for that, not just for the scripted questions.

### 1. Run the intake questionnaire

Ask these questions, in this order, like a short form — one at a time is
fine, but don't skip ahead or improvise substitutes for them. Where a
question has a fixed set of options, present it as a pick from a list (use
the `AskUserQuestion` tool if it's available in the session) rather than an
open text question:

1. Name of the new joiner.
2. **Craft** — pick one: *UX Designer / UX Researcher / Content Designer /
   Localization Specialist*.
3. **Seniority** — pick one: *Manager / Staff / Senior / Mid / Junior*.
4. Who is the buddy?
5. One short sentence about the buddy.
6. What project(s) will they shadow, and who gives the intro to each one?
7. Who is their PM / EM?
8. What other teammates should they meet?

`profile.role` is just questions 2+3 combined (e.g. "Staff UX Designer").
There's no separate "team/scope" question — if one falls out naturally from
the shadowing projects or PM/EM answers, use it to title the Week 2 module
(e.g. "Week 2 · Retail + QC"); otherwise a generic "Week 2 · Your team" title
is fine.

**Craft gate:** only *UX Designer* is implemented today (it uses the
ready-made Week 1 checklist in `references/content-library-design-craft.md`
as-is). If
the answer to question 2 is Researcher, Content Designer, or Localization
Specialist, say clearly that craft is still work-in-progress and stop there
instead of guessing content for it — don't continue the questionnaire.

**Question 6 — finding the shadow-project doc automatically:** for each
project named, search the Design Reviews Drive folder
(`https://drive.google.com/drive/folders/1uDu6XhzvBnr5NuKJv6lOgSLC7R79Uip5`,
folder ID `1uDu6XhzvBnr5NuKJv6lOgSLC7R79Uip5`) with whatever Google Drive
search tool is available (e.g. `search_files`/`read_file_content`) for a doc
whose title plausibly matches the project. If you find a clear match, use it
as that person's `link.url` in `peopleGroups` (this is how earlier pages
linked each shadow project to its design review doc). If nothing matches
clearly, leave the entry without a link rather than guessing a doc.

If any answer is missing or ambiguous — especially a name, Slack handle, or
link — ask again rather than fabricating content to fill the gap.

**Not part of the form, reused as-is:** the 9 Resource Hub modules' points of
contact, Week 1's "Meet the UX Design team" group, Week 2's "UX Research" and
"Localization & Content" groups, and the OKR module/spotlight all come
straight from `references/content-library-design-craft.md` unmodified —
they're standing team intros, not specific to any one new joiner. Only touch
them if the requester proactively mentions something changed (a POC moved
teams, a new OKR stream, someone new joined UXR, etc.) — don't ask about them
by default, and don't invent an OKR spotlight when none was given (the
template renders the OKR module fine
with no `spotlight` at all — see `data-schema.md`).

### 2. Resolve every named person to a real Slack link

For the buddy and everyone in `peopleGroups`/`poc`, search Slack for their
member ID and build a `/team/<ID>` link. Full detail, including the known
"opens profile not DM" limitation, in `references/slack-links.md`.

### 3. Assemble `data.json`

Follow `references/data-schema.md` for the exact shape (`profile`, `buddy`,
`modules[]`). The `modules` array always has this order: **Week 1** → **Week
2** → **After your first month** → the 9 Resource Hub modules. The first and
third are standard, required, and reused as-is for every Designer; only Week
2's person-specific `peopleGroups` (shadow projects, PM/EM, other teammates)
and its title need building from scratch each time, using what you gathered
in step 1. Edit the Resource Hub only for the OKR module's `spotlight` and
any POC that's changed since the library was last refreshed.

Keep every `id` unique across the whole array, and get the `trackable` flag
right: Resource Hub modules are `trackable:false` (reference only, never
counted); Week 1, Week 2, and "After your first month" are all trackable
(checkboxes, counted toward progress/badges/confetti) — don't mark "After
your first month" as `trackable:false`, it's a required module, not
reference material.

### 4. Render the page

```
python3 scripts/build_onboarding.py path/to/data.json Onboarding-<Name>-EN.html
```

If the script raises a missing-field or leftover-placeholder error, that's
`data.json` being incomplete — fix the data, don't patch the output HTML or
the template to work around it.

### 5. Sanity-check before handing it over

- Open the file in a browser if one's available and click through the
  checkboxes, confirm progress/badges/confetti behave, and that no Slack
  link 404s.
- If there's no browser available in this environment, at minimum grep the
  output for `{{` (should find nothing — the build script already checks
  this) and spot-check a few of the Slack URLs and Jira links resolve to
  real, current pages.
- Mention to the requester: progress is saved in `localStorage` per browser
  (no backend, no sync across devices), and Slack links open the person's
  profile, not a DM thread directly.

## Extending to a new craft

When the same request comes in for a non-Design craft for the first time:
gather everything conversationally (nothing to start from yet), build their
page, and afterwards offer to extract a `content-library-<craft>.md` from
what you learned, mirroring the structure of the Design one — so the next
person in that craft doesn't start from zero either.
