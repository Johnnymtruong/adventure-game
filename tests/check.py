"""Automatic feedback for this lab.
Students: you do not need to edit this file. Push your commits and read
the Actions feedback. Each failed check tells you what to look at next.
"""
import json, os, subprocess, sys

CONFIG = json.loads(r"""{
  "required_files": [
    "game.py",
    "README.md"
  ],
  "source_contains": [
    {
      "file": "game.py",
      "contains": "import pygame",
      "why": "the game is built with Pygame"
    },
    {
      "file": "game.py",
      "contains": "while",
      "why": "a real game loop keeps the window open -- set_mode does NOT start a loop for you"
    },
    {
      "file": "game.py",
      "contains": "QUIT",
      "why": "the loop must handle the pygame.QUIT event so the window closes cleanly"
    }
  ],
  "no_todo": [
    "game.py"
  ],
  "readme_sections": [
    "Game concept",
    "Feature plan",
    "AI Review",
    "Final reflection"
  ]
}""")

failures = []

def note(ok, msg_pass, msg_fail):
    if ok:
        print("PASS:", msg_pass)
    else:
        print("FAIL:", msg_fail)
        failures.append(msg_fail)

for f in CONFIG["required_files"]:
    note(os.path.exists(f), "required file present: " + f, "required file missing or renamed: " + f)

for spec in CONFIG.get("runs", []):
    f = spec["file"]
    if not os.path.exists(f):
        continue
    try:
        r = subprocess.run([sys.executable, f], input=spec.get("stdin", ""),
                           capture_output=True, text=True, timeout=spec.get("timeout", 10))
        if spec.get("must_succeed", True):
            note(r.returncode == 0, f + " runs without errors",
                 f + " exited with an error. Read the message, fix one line, run again:\n" + r.stderr.strip()[-800:])
        if "expected_lines" in spec and r.returncode == 0:
            out = [l.rstrip() for l in r.stdout.strip().splitlines()]
            exp = spec["expected_lines"]
            note(out == exp, f + " output matches the required output",
                 f + " output does not match the required output yet.\nExpected:\n" + "\n".join(exp) + "\nActual:\n" + "\n".join(out))
    except subprocess.TimeoutExpired:
        note(False, "", f + " did not finish within the time limit. Does your loop reach its stopping condition?")

for spec in CONFIG.get("source_contains", []):
    f, needle, why = spec["file"], spec["contains"], spec["why"]
    if os.path.exists(f):
        src = open(f).read()
        note(needle in src, f + " contains " + repr(needle), f + " should contain " + repr(needle) + " -- " + why)

readme_src = open("README.md").read() if os.path.exists("README.md") else ""
for section in CONFIG.get("readme_sections", []):
    note(section in readme_src, "README section present: " + section, "README is missing the required section heading: " + section)

for f in CONFIG.get("no_todo", []):
    if os.path.exists(f):
        src = open(f).read()
        note("TODO" not in src, f + " has no remaining TODO markers", f + " still contains TODO markers -- finish those sections")

print()
if failures:
    print(str(len(failures)) + " check(s) need attention. Fix one thing, commit, and push again.")
    sys.exit(1)
print("All automatic checks passed. Automatic checks are feedback, not a final grade -- your instructor reviews the README and your commits.")
