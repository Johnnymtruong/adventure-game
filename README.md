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
