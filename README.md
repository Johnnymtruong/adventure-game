# Module 6 Game Planning Repository

This repository is YOUR game project. You will keep working in it during Modules 7 and 8.
Make **Commit 1, 2, and 3** at the checkpoints below, then record your **Walk Me Through Your Review** video.

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
(record material AI-supported decisions here as the project continues)
## Module 7: Core Mechanic and Tests

### Mechanic: Collect items and track score
When the player presses the E key, the game checks whether the player's
current location still has an item. If it does, the item is removed from
the world, added to the player's items, and its point value is added to
the score. If there is nothing left, the game shows "Nothing here to pick up."

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
| 3 | Boundary | Fresh run, press E [3 or 5] times | Score stays 10, Items shows only key | [what you saw] | [Pass/Fail] |
| 4 | Negative | Fresh run, press Q | Nothing changes | Nothing changed | Pass |
| 5 | Regression | Close the window with the X | Closes with no error | [what you saw] | [Pass/Fail] |

### Notes
- Moving between locations is not built yet, so the cave's map cannot be
  picked up in this version.
- Installed `pygame-ce` instead of `pygame` because regular pygame would not
  install on Python 3.14.