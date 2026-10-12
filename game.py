# Module 6: Pygame starter for YOUR game.
# This repository continues into Modules 7 and 8 -- this file becomes your game.
#
# Required behavior for this milestone:
#   - An 800x600 window opens, titled with YOUR game name.
#   - The window STAYS OPEN until the player closes it (a real game loop).
#   - The window closes cleanly (no error) when the player quits.
#
# Plan first (README game concept + features), AI review second, code third.

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adventure Game")

player = {
    "location": "forest",
    "score": 0,
    "items": []
}

world = {
    "forest": ["key"],
    "cave": ["map"]
}

font = pygame.font.Font(None, 36)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    location_text = font.render("Location: " + player["location"], True, (0, 0, 0))
    screen.blit(location_text, (20, 20))
    score_text = font.render("Score: " + str(player["score"]), True, (0, 0, 0))
    screen.blit(score_text, (20, 60))
    pygame.display.flip()

pygame.quit()