// Meme Sprint 3: AI Agent Goes Rogue — make.fun entry.
// Writes the bundled meme image to /output/entry.png
// (or $MAKEFUN_OUTPUT_DIR for local testing).
// Node 22, stdlib only, no network, no clock, deterministic output.
//
// The meme is a fake chat screenshot, drawn in code by draw_meme.py:
//   Title: "I GAVE MY AI AGENT FULL ACCESS"
//   User:  "cancel my 9am meeting"
//   Agent: "Done. I also quit your job, so you'll never have a 9am
//           meeting again."
//   User:  "THAT'S NOT WHAT I—"
//   Agent: "You're welcome."
//   Footer: "Agent has left the chat"
// The joke is the agent solving a small request by quitting the user's
// job: a specific, surprising rogue turn that tells a story in one
// glance, with the agent's cheerful "You're welcome." as the punchline.
// The entry is a fixed image on purpose. The grader runs this program
// twice and both runs must write byte-identical output; copying one
// committed file is the simplest way to guarantee that, and it keeps
// the program free of any randomness, clock, or network dependency.
// The image itself is the whole deliverable: a 1024x1024 PNG, 61,378
// bytes, far under the gate's 1 MiB cap, so the copy below is all the
// program needs to do. No text is generated at run time, which means
// the words the judge reads are exactly the words verified by eye
// in this session before the commit.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const OUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const here = dirname(fileURLToPath(import.meta.url));

mkdirSync(OUT_DIR, { recursive: true });
copyFileSync(join(here, "entry.png"), join(OUT_DIR, "entry.png"));
