# Module 6 Game Planning Repository

This repository is YOUR game project. You will keep working in it during Modules 7 and 8.
Make **Commit 1, 2, and 3** at the checkpoints below, then record your **Walk Me Through Your Review** video.

## How to run
1. Install Python 3.
2. Install Pygame: `pip install pygame-ce`
3. Run the game: `python game.py`

**Controls:** Left/Right arrows move, E picks up an item, the X closes the game.

## Game concept (complete BEFORE any AI use)
What the player does, what the game responds to, and what the player is trying to accomplish (3-5 sentences):

My game is a simple adventure game where the player explores different areas and collects useful items. The game responds to the player's choices, such as where they move and which items they pick up. The player is trying to collect the required items and reach the final area to win.

## Feature plan (complete BEFORE any AI use)
Exactly three core features for the first playable version, plus one future feature:

1. Core feature: Move between locations
2. Core feature: Collect items
3. Core feature: Track player score
- Future feature (not built yet): Add enemies

-> **Commit 1: "Game concept and feature plan (pre-AI)"**

## AI Review (required)
Use the approved AI tool to review ONE planning or starter-code decision.

**My prompt (focused, with context):**
I'm building a small adventure game in Python with Pygame where the player moves between locations, collects items, and tracks a score. Should I store the player's location and score using plain variables, a dictionary, or a class? I'm leaning toward using a dictionary because it keeps related information together and seems easier for me as a beginner. I also want the game to stay simple for the first version, but I may add enemies later. Which option would be the best choice and why?

**The AI recommendation (summarized as separate claims):**
1. Plain variables are simple but can become harder to manage when the game gets bigger.
2. A dictionary keeps the player's information together in one place.
3. A class can organize both data and actions, but it requires more setup.
4. A dictionary can work for the first version and be changed to a class later if needed.

**Claim I verified and the documentation I used (link or citation):**
I verified the claim that a dictionary stores information using keys and values.

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

**The evidence, in my own words:**
The Python documentation shows that dictionary values can be accessed by using their keys, such as player["score"]. It also shows that values can be changed by assigning a new value to a key. This supports using a dictionary because I can keep the player's location, score, and items together and update them when the game changes.

**My decision (accept / revise / verify further / reject) and why:**
I accept the recommendation. I am going to use a dictionary because it is simple enough for me as a beginner and keeps the player information organized. I know I may need to change it to a class later when I add enemies, and I am comfortable doing that if the game becomes more complex.

**What changed in the repository because of this decision:**
No code changed yet. In game.py I will store the player as a dictionary with location, score, and items.

-> **Commit 2: "AI review documented"**

## Starter code
Complete game.py. Confirm: window opens with your title, stays open, closes cleanly.

## Final reflection
You remain responsible for this repository even with AI support. What is one thing in this repo you could now explain to another student without help?

I can now explain how the Pygame game loop keeps the window open and how pygame.QUIT lets the program close cleanly when the player clicks the X.

-> **Commit 3: "Working starter code and reflection"**

Then record and submit the **Walk Me Through Your Review** video.

## AI rules for this repo (Modules 6-8)
- AI use is permitted and (for the review step) required, using the instructor-approved AI tool.
- Never let AI replace your planning step, generate a complete finished game, or write your README explanations.
- Never put passwords, tokens, keys, or personal information in a prompt.
- If AI materially influences a later decision (Modules 7-8), document it in the AI Support Note section below.

## AI Support Note (Modules 7-8)
### Module 8 – Movement Feature

What I asked: I asked AI for help adding movement between the forest and cave.

What it suggested: AI provided code for the movement function, location dictionary, arrow key controls, and help text.

What I accepted, changed, or rejected, and why: I added the code to my game.py because it matched the dictionary approach I chose in Module 6.

How I checked it: I ran the tests and tested the game myself. I learned that the 5-point run happened because I didn't collect the key first, showing that each item adds its own points. I also recorded a demo to show the feature working.

## Module 7: Core Mechanic and Tests

### Mechanic: Collect items and track score
When the player presses the E key, the game checks whether the player's current location still has an item. If it does, the item is removed from the world, added to the player's items, and its point value is added to the score. If there is nothing left, the game shows "Nothing here to pick up."

### Code responsibilities
| Responsibility | Where it lives in game.py |
|---|---|
| State | `player`, `world`, and `item_values` dictionaries |
| Input | `KEYDOWN` check for the E key in the event loop |
| Update | `pick_up_item()` function |
| Draw | `font.render(...)` and `screen.blit(...)` lines |

### Test results
| # | Type | Steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Positive | Start the game, press E once | "You picked up the key", Score: 10, Items: key | Matched expected | Pass |
| 2 | Negative | Press E a second time | "Nothing here to pick up", score stays 10 | Matched expected | Pass |
| 3 | Boundary | Fresh run, press E several times | Score stays 10, Items shows only key | Matched expected | Pass |
| 4 | Negative | Fresh run, press Q | Nothing changes | Nothing changed | Pass |
| 5 | Regression | Close the window with the X | Closes with no error | Matched expected | Pass |

### Notes
- Moving between locations is not built yet, so the cave's map cannot be picked up in this version. (Fixed in Module 8, see below.)
- Installed `pygame-ce` instead of `pygame` because regular pygame would not install on Python 3.14.

## Module 8: Final Test Plan

| # | Type | Steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Positive | Fresh run, right arrow, E | Cave, map, Score: 5 | Matched expected | Pass |
| 2 | Positive | Fresh run, E, right arrow, E | Score: 15, Items: key, map | Score: 15, Items: key, map | Pass |
| 3 | Boundary | In the cave, press right arrow | "You can't go that way", stays in cave | "You can't go that way", stayed in cave | Pass |
| 4 | Boundary | In forest, press left arrow | "You can't go that way", stays in forest | "You can't go that way", stayed in forest | Pass |
| 5 | Regression | Pick up key, leave forest, come back, press E | "Nothing here to pick up", score doesn't change | "Nothing here to pick up", score stayed the same | Pass |
| 6 | Regression | Move around, then click the X | Window closes with no error | Window closed, no error | Pass |

### Retest of previously documented issue
- **Issue (Module 7):** The cave's map couldn't be picked up because movement wasn't built.
- **Fix:** Added a `connections` dictionary, a `move_player()` function, and arrow key input.
- **Retest:** Test 2. Score went to 15 and Items showed key, map. The cave's map can now be picked up. Pass.

### Polish
- Added on-screen controls at the bottom of the window: "Arrows: move   E: pick up".