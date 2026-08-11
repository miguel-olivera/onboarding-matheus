# Content library — UX Design craft

Reusable starting point for anyone joining as a **UX/Product Designer** on the
Glovo UX team (Staff, Sr, Ssr, Junior — the tasks below don't change much by
level). This is the library the team's first onboarding page was built from.

**Only for this craft.** If the new joiner is Research, Content/Localization,
or Motion — don't force this library onto them. Their Week 1 tooling overlaps
a lot (Workday, Slack, Confluence, Claude access...) but Week 2 and parts of
the Resource Hub genuinely differ. Until a craft-specific library exists for
them, ask the requesting manager for the equivalent content instead of
guessing, and consider saving what you learn as a new
`content-library-<craft>.md` next to this file for next time.

**These are starting points, not gospel.** Re-check with the manager that
nothing has changed (new tool, retired link, reorg) before reusing verbatim —
this content drifts as fast as any other internal doc.

## Week 1 — items (generic across the whole UX org)

```json
{
  "id": "week1",
  "icon": "1️⃣",
  "sectionLabel": "Your first weeks",
  "title": "Week 1: Welcome to Glovo",
  "blurb": "Get your hardware, software and access sorted, and meet the team.",
  "items": [
    {"id": "week1-1", "label": "<b>Go through the meetings and events the onboarding team invites you to</b>", "links": []},
    {"id": "week1-2", "label": "Check your Workday access — update your details and see the company structure", "tooltip": "Workday is Delivery Hero's HR platform — it's where your personal details, time off, payslips, and the company org chart live. Most official company communication happens through it.", "links": [{"text": "Workday", "url": "https://deliveryhero.okta.com/app/workday/exka6utkdG3QIo2EG416/sso/saml"}]},
    {"id": "week1-3", "label": "Request <b>Google Drive</b> access", "links": [{"text": "Mariana on Slack", "url": "https://deliveryhero.enterprise.slack.com/team/U03C1KPURDK"}]},
    {"id": "week1-4", "label": "Log in to <b>Figma</b> via SSO", "links": []},
    {"id": "week1-4b", "label": "Request <b>Figma Viewer</b> access", "links": [{"text": "Figma access guide", "url": "https://atlassian.cloud.deliveryhero.group/wiki/spaces/ETS/pages/151063768/Figma"}]},
    {"id": "week1-4c", "label": "Request <b>Figma Edit</b> access", "links": [{"text": "Request form", "url": "https://deliveryhero.atlassian.net/servicedesk/customer/portal/1395/group/2642/create/9771"}]},
    {"id": "week1-5", "label": "Log in to <b>Miro</b> via SSO", "links": [{"text": "Miro login", "url": "https://miro.com/login/"}]},
    {"id": "week1-6", "label": "Request a <b>Miro</b> license", "links": [{"text": "Request form", "url": "https://deliveryhero.atlassian.net/servicedesk/customer/portal/296/group/649/create/3816"}]},
    {"id": "week1-7", "label": "Ask your buddy to add you to the core <b>Slack</b> channels", "links": []},
    {"id": "week1-8", "label": "Log in to Confluence with your Google account", "tooltip": "Confluence is Atlassian's wiki tool — the UX team uses it to document processes, meeting notes, and reference pages alongside Jira.", "links": [{"text": "Confluence", "url": "https://id.atlassian.com/login?continue=https%3A%2F%2Fid.atlassian.com%2Fjoin%2Fuser-access%3Fresource%3Dari%253Acloud%253Aconfluence%253A%253Asite%252F66e7acb3-8179-4193-83a8-9ae0e35c5061%26continue%3Dhttps%253A%252F%252Fglovoapp.atlassian.net%252Fwiki%252Fspaces%252FCRM%252Fwhiteboard%252F5393448962"}]},
    {"id": "week1-9", "label": "<b>Get access</b> to GitHub — join the Glovo organization", "links": [{"text": "Step-by-step guide", "url": "https://scribehow.com/viewer/Request_Access_to_GitHub_Organization_for_Glovo_Account__aB0aELe7TM2rgkXRtfEQ5w"}]},
    {"id": "week1-10", "label": "Get access to <b>Claude</b> — raise a ticket and select Claude in the apps list", "links": [{"text": "Raise a ticket", "url": "https://glovoapp.atlassian.net/servicedesk/customer/portal/23/group/2726/create/7496"}]},
    {"id": "week1-11", "label": "Ask your buddy to add you to the team's Google Calendar, and add your birthday", "links": []},
    {"id": "week1-12", "label": "Go through the key onboarding docs", "links": [{"text": "UX & Product organizations", "url": "https://www.figma.com/board/EbQoVfbReGrYFGed7aTcdT/Product---UX-organization?node-id=157-64"}, {"text": "Our Design Process", "url": "https://www.figma.com/board/EbQoVfbReGrYFGed7aTcdT/Product---UX-organization?node-id=169-479"}, {"text": "Jira Projects tracker", "url": "https://glovoapp.atlassian.net/jira/plans/4363/scenarios/4364/timeline?vid=5734"}]},
    {"id": "week1-13", "label": "Know where to go for help", "links": [{"text": "Service Desk", "url": "https://glovoapp.atlassian.net/servicedesk/customer/portal/23/user/login?destination=portal%2F23%2Fgroup%2F150%3FgroupId%3D150"}, {"text": "Glovopedia", "url": "https://sites.google.com/glovoapp.com/glovopedia?pli=1"}]}
  ],
  "peopleGroups": [
    {"title": "Meet the UX Design team", "checkable": true, "people": [
      {"id": "week1-meet-jack", "name": "Jack Coles", "note": "Intro to Food", "slackId": "USNLGLV8C"},
      {"id": "week1-meet-miguel", "name": "Miguel Olivera", "note": "Intro to Growth", "slackId": "U0LHTEFTP"},
      {"id": "week1-meet-andrea", "name": "Andrea Escobar", "note": "Intro to Q-commerce", "slackId": "U0ALV9NEQMA"},
      {"id": "week1-meet-jordi", "name": "Jordi Alonso", "note": "Intro to Pintxo Design System", "slackId": "U023HP9BQ14"}
    ]}
  ],
  "closingNote": "Along the way, you'll keep getting invited to meet more of the team 🙂 And don't stress about lunch — we all eat together at the office every day."
}
```

"Meet the UX Design team" is a standing intro round for every new Designer,
not specific to any one person — reuse it as-is, same as the Resource Hub
POCs. Only re-check names/notes if the team composition changed since this
was last refreshed.

## Week 2 — items + standing team-intro groups (reusable)

The "Key projects to shadow" and "Product Managers & Engineering Managers"
peopleGroups are genuinely person-specific (see `SKILL.md`'s intake
questions 6-8) and must be built fresh each time. But two other Week 2
groups are standing team intros, just like Week 1's — reuse them:

```json
{
  "title": "UX Research", "checkable": true, "actionPrefix": "Meet",
  "note": "Book a session to get closer to key insights and the current UXR studies.",
  "link": {"text": "UXR studies list", "url": "https://docs.google.com/document/d/117zIgMw-9UApCd4Tvfe9J26Z46drZYUZhmpBxDXiriU/edit#heading=h.t8bq2d9pk90c"},
  "otherMembersNote": "Also part of the UXR team: Pablo Andres Margara, Alejandra Ramirez and Héctor Rebollo.",
  "people": [{"id": "week2-research-anna", "name": "Anna Kebets", "slackId": "U02NHDQSX0C"}]
}
```

```json
{
  "title": "Localization & Content", "checkable": true, "actionPrefix": "Meet",
  "note": "Get familiar with our localization and content guidelines and ways of working.",
  "link": {"text": "Localisation Hub", "url": "https://glovoapp.atlassian.net/wiki/spaces/LP/pages/5598874014/Localisation+Hub"},
  "people": [
    {"id": "week2-loc-emilia", "name": "Emilia Porfiri", "note": "Localization — guidelines & WoW", "slackId": "U0AGEMRCZ7A"},
    {"id": "week2-loc-content", "combine": [{"name": "Diane Chang", "slackId": "U09CWUAQ4RL"}, {"name": "Emilia Porfiri", "slackId": "U0AGEMRCZ7A"}], "note": "Content design — guidelines & WoW"}
  ]
}
```

If the buddy is themself part of UX Research (or another team these groups
introduce), drop that person from the group so they don't meet themselves.

## Week 2 — items only (title and scope vary per person, see SKILL.md)

```json
{
  "id": "week2",
  "icon": "2️⃣",
  "title": "Week 2 · <team/scope name>",
  "blurb": "Go deeper on our design principles, and start shadowing real projects.",
  "items": [
    {"id": "week2-1", "label": "Learn about our UX principles", "links": [{"text": "View principles", "url": "https://www.figma.com/slides/8fifOtZDMVQvj7JJ9yf8gK/Design-principles?node-id=3-14"}]},
    {"id": "week2-2", "label": "Take a look at the main UXR projects", "links": [{"text": "UXR projects", "url": "https://docs.google.com/document/d/117zIgMw-9UApCd4Tvfe9J26Z46drZYUZhmpBxDXiriU/edit"}]},
    {"id": "week2-3", "label": "Look at some Design Reviews from past projects", "links": [{"text": "Design Review docs", "url": "https://drive.google.com/drive/folders/1uDu6XhzvBnr5NuKJv6lOgSLC7R79Uip5"}]},
    {"id": "week2-4", "label": "Get familiar with the Pintxo Design System (Figma & docs)", "links": [{"text": "Figma", "url": "https://www.figma.com/design/TuxClC4JIItgCYAZiafQBt/Pintxo-Design-System"}, {"text": "Documentation", "url": "https://pintxo.glovoapp.com/4a9248a45/p/262983-pintxo-design-system"}]}
  ]
}
```

Re-title `week2` with whatever this person's actual scope is (e.g. "Week 2 ·
Retail + QC" for a Retail hire), and build `peopleGroups` from scratch:
projects to shadow, the relevant UXR contact, Localization/Content contact,
their PM/EM(s), and a few more teammates — all real names, resolved to real
Slack IDs.

## After your first month (standard, trackable — required for every Designer)

```json
{
  "id": "month1", "icon": "🎯", "sectionLabel": "After your first month",
  "title": "After your first month",
  "blurb": "Wrap up your first month by getting familiar with how we evaluate and grow on the team.",
  "poc": {"name": "Francisco Romano", "email": "francisco.romano@glovoapp.com", "slackId": "U02C3RV08BX"},
  "items": [
    {"id": "month1-1", "label": "Complete the Competency Framework", "links": [
      {"text": "Competency Framework - How it works", "url": "https://docs.google.com/presentation/d/1G0rygs6OAR3T231p3avjby0b9YvJ8JwH5HYRwrhXhO0/edit"},
      {"text": "Competency Framework - Self-Check", "url": "https://forms.gle/DBq26tMkNTBH16t69"},
      {"text": "UXD - Competency Framework", "url": "https://docs.google.com/spreadsheets/d/1cAE7-Ry85PkH7JStDTut_1lewoMEl03LPGGXZ5ZK_7s/edit"}
    ]}
  ]
}
```

Unlike the Resource Hub, this module has no `trackable:false` — it counts
toward progress like Week 1 and Week 2. It's a required, standard third
module for every UX Designer (not just Design leadership) — always include
it, right after Week 2 and before the Resource Hub.

## Resource Hub — 9 modules (stable, `trackable:false`)

These rarely change person to person. Re-verify links/POCs are current, but
otherwise these can go in as-is.

```json
[
  {
    "id": "org", "icon": "🧭", "trackable": false, "sectionLabel": "Resource hub — come back to these anytime", "title": "UX Organization",
    "blurb": "How the Product & UX team is structured, and where we live.",
    "items": [
      {"id": "org-1", "label": "Check out the Product & UX org chart", "links": [{"text": "View in Figma", "url": "https://www.figma.com/board/EbQoVfbReGrYFGed7aTcdT/Product---UX-organization?node-id=0-1"}]},
      {"id": "org-2", "label": "Explore the team's Drive (Product UX Repository)", "links": [{"text": "Open Drive", "url": "https://drive.google.com/drive/folders/0AInDpMY24RJQUk9PVA"}]},
      {"id": "org-3", "label": "Watch the latest UX All Hands", "links": [{"text": "View slides", "url": "https://docs.google.com/presentation/d/1nACQwUn987XD6XK87eMG3EBIx50Rqn3xJgnOsD7yU8E/edit"}]},
      {"id": "org-4", "label": "Join the Slack channel", "links": [{"text": "#glovo-ux-team", "url": "https://deliveryhero.enterprise.slack.com/archives/CJX8C61BJ"}]}
    ]
  },
  {
    "id": "process", "icon": "📊", "trackable": false, "title": "Visibility, Tracking & Processes",
    "blurb": "How we track the team's work: OKRs, sprints, and project templates.",
    "items": [
      {"id": "process-1", "label": "Check the OKR plan in Jira", "links": [{"text": "UX Team - Plan", "url": "https://glovoapp.atlassian.net/jira/plans/4363/scenarios/4364/timeline"}]},
      {"id": "process-2", "label": "Take a look at the sprint board (2-week cycles)", "links": [{"text": "UX Design Board", "url": "https://glovoapp.atlassian.net/jira/software/c/projects/PUX/boards/8139"}]},
      {"id": "process-3", "label": "Read the UX process doc (phases & outcomes)", "links": [{"text": "UX Team Process Tasks", "url": "https://docs.google.com/document/d/1FMDRSoCGfz7xR4IlIeuIh0UEty3ncxQqyVUNcsoFtzs/edit"}]},
      {"id": "process-4", "label": "Explore the Design Brief Docs folder", "links": [{"text": "Folder", "url": "https://drive.google.com/drive/folders/1p0EN_yViUSm0c4yT-cA4AxJlizPzg8pQ"}, {"text": "Template", "url": "https://docs.google.com/document/d/13Qq1IsQiK49V4FA2AP6LKksliG12UBeOf_RDCT2aQ3k/edit"}]},
      {"id": "process-5", "label": "Explore the Design Review docs folder", "links": [{"text": "Folder", "url": "https://drive.google.com/drive/folders/1uDu6XhzvBnr5NuKJv6lOgSLC7R79Uip5"}, {"text": "Template", "url": "https://docs.google.com/document/d/1K-C5jtBf6cFjFYy1_KXX4AYpherlW64tHdMeQNZxMss/edit"}]}
    ]
  },
  {
    "id": "competency", "icon": "🎯", "trackable": false, "title": "Competency Framework",
    "blurb": "The framework we use to evaluate and grow people on the team.",
    "poc": {"name": "Emilia Porfiri", "email": "emilia.porfiri@glovoapp.com", "slackId": "U0AGEMRCZ7A"},
    "items": [
      {"id": "competency-1", "label": "Book 15 min with the point of contact to walk you through it", "links": [{"text": "Emilia on Slack", "url": "https://deliveryhero.enterprise.slack.com/team/U0AGEMRCZ7A"}]},
      {"id": "competency-2", "label": "Watch \"Competency Framework - How it works\"", "links": [{"text": "View presentation", "url": "https://docs.google.com/presentation/d/1G0rygs6OAR3T231p3avjby0b9YvJ8JwH5HYRwrhXhO0/edit"}]},
      {"id": "competency-3", "label": "Complete your Self-Check", "links": [{"text": "Open form", "url": "https://forms.gle/DBq26tMkNTBH16t69"}]},
      {"id": "competency-4", "label": "Review the levels & competencies spreadsheet", "links": [{"text": "UXD - Competency Framework", "url": "https://docs.google.com/spreadsheets/d/1cAE7-Ry85PkH7JStDTut_1lewoMEl03LPGGXZ5ZK_7s/edit"}]}
    ]
  },
  {
    "id": "leads", "icon": "🗣️", "trackable": false, "title": "UX Leads",
    "blurb": "The coordination space between the team's leads.",
    "items": [{"id": "leads-1", "label": "Join the Slack channel", "links": [{"text": "#glovo-ux-leads", "url": "https://deliveryhero.enterprise.slack.com/archives/C08US81SP5Z"}]}]
  },
  {
    "id": "research", "icon": "🔍", "trackable": false, "title": "UX Research",
    "blurb": "How we generate and access user insights.",
    "poc": {"name": "Anna Kebets", "email": "anna.kebets@glovoapp.com", "slackId": "U02NHDQSX0C"},
    "items": [
      {"id": "research-1", "label": "Book 15 min with the point of contact to walk you through it", "links": [{"text": "Anna on Slack", "url": "https://deliveryhero.enterprise.slack.com/team/U02NHDQSX0C"}]},
      {"id": "research-2", "label": "Check the UXR board in Jira", "links": [{"text": "UXR Jira Board", "url": "https://glovoapp.atlassian.net/jira/software/c/projects/PUX/boards/8372"}], "note": "The team is still confirming this link — if it doesn't load, ask your point of contact."}
    ]
  },
  {
    "id": "localization", "icon": "🌍", "trackable": false, "title": "UX Localization & Content",
    "blurb": "How we adapt content and copy to each market.",
    "poc": {"name": "Emilia Porfiri", "email": "emilia.porfiri@glovoapp.com", "slackId": "U0AGEMRCZ7A"},
    "items": [
      {"id": "localization-1", "label": "Book 15 min with the point of contact to walk you through it", "links": [{"text": "Emilia on Slack", "url": "https://deliveryhero.enterprise.slack.com/team/U0AGEMRCZ7A"}]},
      {"id": "localization-2", "label": "Check the Localization board in Jira", "links": [{"text": "UXL Jira Board", "url": "https://glovoapp.atlassian.net/jira/software/c/projects/PUX/boards/12287"}], "note": "The team is still confirming this link — if it doesn't load, ask your point of contact."}
    ]
  },
  {
    "id": "pintxo", "icon": "🎨", "trackable": false, "title": "Pintxo Design System",
    "blurb": "Our design system: foundations, components, and how to contribute.",
    "poc": {"name": "Jordi Alonso", "email": "jordi.alonso@glovoapp.com", "slackId": "U023HP9BQ14"},
    "items": [
      {"id": "pintxo-1", "label": "Book 15 min with the point of contact to walk you through it", "links": [{"text": "Jordi on Slack", "url": "https://deliveryhero.enterprise.slack.com/team/U023HP9BQ14"}]},
      {"id": "pintxo-2", "label": "Watch \"Design System - Govern & Create: Pintxo Essentials\"", "links": [{"text": "View presentation", "url": "https://docs.google.com/presentation/d/1hkkG307g7eWZCjp653f6RhVRtWPclPuiXuDj3a7pEdQ/edit"}]},
      {"id": "pintxo-3", "label": "Check the Pintxo 2026 initiative in Jira", "links": [{"text": "PUX-2697", "url": "https://glovoapp.atlassian.net/browse/PUX-2697"}]},
      {"id": "pintxo-4", "label": "Explore the design system documentation", "links": [{"text": "pintxo.glovoapp.com", "url": "https://pintxo.glovoapp.com/"}]},
      {"id": "pintxo-5", "label": "Open the Figma files", "links": [{"text": "Project", "url": "https://www.figma.com/files/907684760615163521/project/66571034"}, {"text": "Main Library", "url": "https://www.figma.com/design/TuxClC4JIItgCYAZiafQBt/Pintxo-Design-System"}]},
      {"id": "pintxo-6", "label": "Join the Slack channels", "links": [{"text": "#design-system-community", "url": "https://deliveryhero.enterprise.slack.com/archives/C06JZFV3A0K"}, {"text": "#design-system-squad", "url": "https://deliveryhero.enterprise.slack.com/archives/C0403KNBKUZ"}, {"text": "#ptxo-ux", "url": "https://deliveryhero.enterprise.slack.com/archives/C08PG0DJU3X"}]},
      {"id": "pintxo-7", "label": "Review the Champions model notes", "links": [{"text": "Pintxo Champions Notes", "url": "https://docs.google.com/document/d/1yGBRlw_tY5_XvYtfu_PmCxZGn6gfQQo4HDuV_ihUqRI/edit"}]}
    ]
  },
  {
    "id": "a11y", "icon": "♿", "trackable": false, "title": "Accessibility (A11y)",
    "blurb": "How we design accessible experiences for everyone.",
    "poc": {"name": "Andrea Escobar", "email": "andrea.escobar@glovoapp.com", "slackId": "U0ALV9NEQMA"},
    "items": [
      {"id": "a11y-1", "label": "Book 15 min with the point of contact to walk you through it", "links": [{"text": "Andrea on Slack", "url": "https://deliveryhero.enterprise.slack.com/team/U0ALV9NEQMA"}]},
      {"id": "a11y-2", "label": "Complete the 3 training sessions", "links": [{"text": "Session 1 · Intro", "url": "https://docs.google.com/presentation/d/1mbgaoNxaqw2-wTrhJnen1d1MODKOjGT6VaPix0XZB7E/edit"}, {"text": "Session 2 · Contribution", "url": "https://docs.google.com/presentation/d/1dx6V1IBOjOzKb0urgGmVXuwwrISgXwBNrU5EVNEUkFI/edit"}, {"text": "Session 3 · Rollout", "url": "https://docs.google.com/presentation/d/1_lkI5ijhNLPm_LLMfw-10fThFt1oJDTvXWjdkZK_jbQ/edit"}]},
      {"id": "a11y-3", "label": "Check the A11y 2026 initiative in Jira", "links": [{"text": "PUX-2507", "url": "https://glovoapp.atlassian.net/browse/PUX-2507"}]},
      {"id": "a11y-4", "label": "Read the accessibility guidelines for tech teams", "links": [{"text": "Accessibility Guidelines", "url": "https://docs.google.com/document/d/1qO3rBzECMqk5RCa1xpUxX6LtLNzD5PAkF1To2E9Ab4I/edit"}]},
      {"id": "a11y-5", "label": "Join the Slack channel", "links": [{"text": "#glovo-tech-accessibility-support", "url": "https://deliveryhero.enterprise.slack.com/archives/C08PXRAHNJ3"}]}
    ]
  },
  {
    "id": "okr", "icon": "🚀", "trackable": false, "title": "UX OKR: Delivery Theme — <current half>",
    "blurb": "The OKR that frames the team's delivery work this half — and your stream.",
    "poc": {"name": "Francisco Romano", "email": "francisco.romano@glovoapp.com", "roleLabel": "OKR lead", "slackId": "U02C3RV08BX"},
    "items": [
      {"id": "okr-1", "label": "Check the initiative in Jira", "links": [{"text": "<ticket>", "url": "https://glovoapp.atlassian.net/browse/<ticket>"}]},
      {"id": "okr-2", "label": "Take a look at the Roadmap", "links": [{"text": "View in Figma", "url": "https://www.figma.com/board/1w3KIrNA0lMqJc3F7l12ud/Roadmap"}]},
      {"id": "okr-3", "label": "Read the OKR's weekly notes", "links": [{"text": "Weekly notes", "url": "https://docs.google.com/document/d/1QtlM7RGkIKkqt4hVMpnLQFMKFeqLivSssx3SrgGiEKs/edit"}]},
      {"id": "okr-4", "label": "Read the monthly report", "links": [{"text": "Monthly Report", "url": "https://docs.google.com/document/d/1058Swd1s-UAWJaHP19drO8S-rkvG-PJztTvgHLN4dfs/edit"}]},
      {"id": "okr-5", "label": "Understand your stream's goal: <stream name>", "links": []},
      {"id": "okr-6", "label": "Book a sync with the leads of your stream's initiatives", "links": []}
    ],
    "spotlight": {
      "title": "🌟 Your stream: <stream name>",
      "leadTemplate": "Lead: {name}",
      "initiatives": []
    }
  }
]
```

The `okr` module needs the most editing per person: swap `<current half>` and
the Jira ticket. `spotlight` and the `okr-5`/`okr-6` items are only filled in
if the intake surfaced a specific OKR stream — that's not part of the
standard questionnaire (see `SKILL.md`), so by default just drop `spotlight`
and those two items rather than inventing a stream (see `data-schema.md`).
