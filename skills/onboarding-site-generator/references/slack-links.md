# Resolving people to Slack links

Every named person in the page (buddy, peopleGroups, module `poc`) should
link to their real Slack profile, not an email or a guess.

1. Use the Slack connector's user search (e.g. `slack_search_users`) to find
   each person by name and get their member ID (`U0...`).
2. Build the profile URL as `https://deliveryhero.enterprise.slack.com/team/<ID>`.
3. If someone can't be found (name typo, contractor not on this Slack, etc.),
   don't fabricate an ID. Leave the person out or flag it to whoever
   requested the page — a broken/wrong Slack link is worse than no link.

**Known limitation:** this opens the person's Slack *profile*, not a direct
message — the visitor still has to click "Message" once. Getting a true
one-click DM link would need the workspace's Team ID or the DM channel ID,
neither of which is obtainable without actually sending a message first.
`/app_redirect?channel=<ID>` was floated as an alternative during the first
build of this page but was never verified against a real browser — worth
testing if this becomes a recurring complaint.

## Buddy avatar

The buddy's photo is embedded as a `data:image/...;base64,...` URI so the
final page has zero external requests (`buddy.avatarDataUri` in
`data-schema.md`). If the same person has already been someone's buddy in a
previous onboarding page, you can lift the data URI straight out of that
file's `hero__buddy-avatar` `background-image` instead of re-encoding a photo.
