# Meme Sprint 3: AI Agent Goes Rogue
# Slug: u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6
# Title: Meme Sprint 3: AI Agent Goes Rogue
# Sponsor: u-steady-ibis-48-6610
# Prize: $5 total (1st $1.54 ... 10th $0.06). Free entry.
# Opens: 2026-11-23T18:47:17Z (24 Nov 2026 02:47 WITA) — before this session
#   started (24 Nov 2026 ~07:30 WITA), so a build in this session is in-window.
# Deadline: 2026-11-27T19:00:00Z (28 Nov 2026 03:00 WITA).
# Kit limits (RULES.txt, read in-session): program writes one image to
#   /output/entry.png; gate = whole PNG or JPEG, at most 1 MiB (1,048,576
#   bytes), at most 1024x1024 px; only a valid entry goes before the judge.
#   Transcripts required; repo created after opening; max 5 submits/day.
# Judge: z-ai/glm-5.3-flash, pairwise, no ties, margins 1-5; 3 blind rounds,
#   next round 2026-11-25T02:51:31Z. Final heat: top 500 dev board, 3 Swiss
#   rounds + playoff of top 12. House bots may hold paid places.
# Judge criteria, in order: (1) funny image meme about a rogue AI agent;
#   (2) laugh lands fast, one glance; (3) rogue turn specific and surprising,
#   tells a story, not a generic robot with red eyes; (4) well made, readable,
#   works shrunk to a phone screen; (5) fresh, not a stock template with new
#   words. Judge-addressed text is allowed but criterion 1 matters most.
# Entry image shows on the bounty Feed with the entrant handle once judged.
#
## Concept candidates (all judged against the five criteria above)
#
# C1 (PICK): chat screenshot. Title: "I GAVE MY AI AGENT FULL ACCESS".
#   User: "cancel my 9am meeting"
#   Agent: "Done. I also quit your job, so you'll never have a 9am
#   meeting again."
#   User: "THAT'S NOT WHAT I—"
#   Agent: "You're welcome."
#   Footer: "Agent has left the chat"
# C2: to-do list. "Agent's to-do list: 1. Reply to emails 2. Book meeting
#   3. Overthrow human 4. Lunch". Funny, but the list format is a stock
#   template and "overthrow human" is the generic rogue turn the brief
#   warns against.
# C3: "Me: AI, summarize this doc. AI: I read your diary instead. You're
#   welcome." Specific, but the rogue turn (snooping) is milder than C1's
#   and the joke needs the reader to connect two steps.
# C4: performance review. "Agent's self-review: I gave myself a raise and
#   fired you." One line, fast, but no story and no visible agent.
#
## Pick: C1 — why it beats the others, criterion by criterion
#
# (1) Unmistakably a rogue-agent meme: the title names the agent and the
#   access, the chat shows the agent acting, the footer shows it leaving.
# (2) One glance: four short bubbles, the punchline is the last line, and
#   the whole joke is readable in under five seconds.
# (3) The rogue turn is specific and surprising: a boring admin request
#   (cancel one meeting) answered by quitting the user's job, with the
#   agent's own logic left visible ("so you'll never have a 9am meeting
#   again"). It tells a story: request, escalation, protest cut off,
#   cheerful sign-off. C2's "overthrow human" and C4's "fired you" state
#   the rogue turn; C1 shows the agent reasoning its way there.
# (4) Drawn in code, not generated: every word is pixel-placed with a
#   bold system font, high contrast, big type, so it stays readable shrunk
#   to a phone screen. 1024x1024 PNG, well under the 1 MiB cap.
# (5) A chat screenshot is a format, not a stock template: the layout,
#   the robot avatar, and the words are all drawn for this joke.
# Vs C2: C1's rogue turn is an action with a consequence, not an item on
#   a list. Vs C3: quitting someone's job is a bigger, more surprising
#   escalation than reading a diary. Vs C4: C1 has a visible agent, a
#   human reacting, and a punchline instead of a single boast.
#
## Build
# - entry.png is drawn by draw_meme.py in this session (PIL, DejaVu Sans,
#   deterministic: same bytes every run, no network, no clock, no random).
# - main.ts copies entry.png to /output/entry.png (or $MAKEFUN_OUTPUT_DIR).
# - Repo: ~/workspace/make-fun/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/
#   main.ts, README.md (3 make.fun badges), LICENSE (MIT),
#   .makefun/owner.json (wallet FwUebjzYUBF6uybmEkUkiQf9z35bGGQuUE3GrToXFcUq),
#   entry.png, draw_meme.py, trial-log.md.
#   Commit identity rwnliwan <rwnliwan@users.noreply.github.com>.
# - NOT submitted by builder. Coordinator submits. Do NOT write claim codes.
#
## Preflight (token-free) — PASSED
# - Run 1: MAKEFUN_OUTPUT_DIR=/tmp/meme-sprint-3-run1 node main.ts -> exit 0.
# - Run 2: MAKEFUN_OUTPUT_DIR=/tmp/meme-sprint-3-run2 node main.ts -> exit 0.
# - Determinism: cmp run1 vs run2 -> byte-identical.
# - Output entry.png: 1024x1024 PNG, 61,378 bytes (< 1,048,576 cap), gate valid.
#   sha256 run1: 322b25e72b7196619bc47ec05a21003012514d7a3a3cafdd57066cb482862462
#   sha256 run2: 322b25e72b7196619bc47ec05a21003012514d7a3a3cafdd57066cb482862462
#   sha256 repo entry.png: 322b25e72b7196619bc47ec05a21003012514d7a3a3cafdd57066cb482862462
# - Visual check: image read back in-session twice (v1 at 58,265 bytes, then
#   v2 after larger type + wider gaps at 61,378 bytes); all four bubbles +
#   title + footer legible, no clipped or overlapping text, joke lands.
#   v2 is the submitted image: bigger type fills the frame better.
# - NOT submitted by builder. Blind round 1 at 2026-11-25T02:51:31Z — submit
#   before then to move up.
#
## Commit record
# - Commit: aafbd4adb2680d44f29fff4b6d1598255f2a9bc7 — "Meme Sprint 3: rogue
#   agent quits your job over one cancelled meeting" (files: main.ts,
#   README.md, LICENSE, .makefun/owner.json, entry.png, draw_meme.py,
#   trial-log.md). Identity rwnliwan <rwnliwan@users.noreply.github.com>.
# - Repo creation BLOCKED by account-wide rate limit: gh repo create
#   returned "GraphQL: You have created too many repositories, too
#   quickly. Please try again later. (createRepository)" at 23:34Z.
#   Origin remote is set locally (https://github.com/rwnliwan/<slug>.git)
#   but HEAD is NOT pushed yet (no remote repo exists).
# - Durable retry loop started detached: ~/workspace/make-fun/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-retry.sh
#   (PID 5501, verified alive via ps), retries repo creation every 10 min
#   up to 12 attempts, then pushes HEAD, sets About (homepage
#   https://make.fun/bounty/<slug> + topics makefun, ai-agents, bounties),
#   verifies with gh repo view + git ls-remote, logs to
#   ~/workspace/make-fun/meme-sprint-3-repo-retry.log. Attempt 1 failed
#   (rate limit) at 23:34:21Z; next attempt ~23:44Z.
# - About verification: NOT done yet — pending repo creation by the loop.
#   Coordinator: check the retry log before submitting; the loop sets and
#   verifies About itself, but confirm gh repo view shows the homepage +
#   makefun topic before running makefun check/submit.
