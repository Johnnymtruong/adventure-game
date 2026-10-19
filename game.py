import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Adventure Game")

# STATE: the player and the items still lying around in each location
player = {
    "location": "forest",
    "score": 0,
    "items": []
}

world = {
    "forest": ["key"],
    "cave": ["map"]
}

# How many points each item is worth
item_values = {
    "key": 10,
    "map": 5
}

# NEW: where each arrow key leads from each location
connections = {
    "forest": {"right": "cave"},
    "cave": {"left": "forest"}
}

font = pygame.font.Font(None, 36)
message = ""  # text shown after the player tries to pick something up


# UPDATE: tries to pick up an item in the player's current location
def pick_up_item():
    location = player["location"]
    if len(world[location]) > 0:
        item = world[location].pop(0)            # remove it from the world
        player["items"].append(item)             # add it to the player's items
        player["score"] += item_values[item]     # raise the score
        return "You picked up the " + item
    return "Nothing here to pick up"


# NEW: UPDATE: tries to move the player in a direction
def move_player(direction):
    location = player["location"]
    if direction in connections[location]:
        player["location"] = connections[location][direction]
        return "You moved to the " + player["location"]
    return "You can't go that way"


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # NEW: INPUT: E picks up, arrow keys move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                message = pick_up_item()
            elif event.key == pygame.K_RIGHT:
                message = move_player("right")
            elif event.key == pygame.K_LEFT:
                message = move_player("left")

    # DRAW: everything the player can see
    screen.fill((255, 255, 255))
    location_text = font.render("Location: " + player["location"], True, (0, 0, 0))
    score_text = font.render("Score: " + str(player["score"]), True, (0, 0, 0))
    items_text = font.render("Items: " + ", ".join(player["items"]), True, (0, 0, 0))
    message_text = font.render(message, True, (0, 0, 0))
    help_text = font.render("Arrows: move   E: pick up", True, (100, 100, 100))  # NEW
    screen.blit(location_text, (20, 20))
    screen.blit(score_text, (20, 60))
    screen.blit(items_text, (20, 100))
    screen.blit(message_text, (20, 160))
    screen.blit(help_text, (20, 550))  # NEW
    pygame.display.flip()

pygame.quit()