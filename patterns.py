import random as rnd

alive = "■"
dead = "."

def add_glider(grid, x, y):
    glider_pattern = [
        [dead, alive, dead],
        [dead, dead, alive],
        [alive, alive, alive]
    ]
    
    for i in range(3):
        for j in range(3):
            grid[y + i][x + j] = glider_pattern[i][j]

def add_block(grid, x, y):
    block_pattern = [
        [alive, alive],
        [alive, alive]
    ]
    
    for i in range(2):
        for j in range(2):
            grid[y + i][x + j] = block_pattern[i][j]

def add_beehive(grid, x, y):
    beehive_pattern = [
        [dead, alive, alive, dead],
        [alive, dead, dead, alive],
        [dead, alive, alive, dead]
    ]
    
    for i in range(3):
        for j in range(4):
            grid[y + i][x + j] = beehive_pattern[i][j]

def add_blinker(grid, x, y):
    blinker_pattern = [
        [alive],
        [alive],
        [alive]
    ]
    
    for i in range(3):
        for j in range(1):
            grid[y + i][x + j] = blinker_pattern[i][j]

def add_toad(grid, x, y):
    toad_pattern = [
        [dead, dead, alive, dead],
        [alive, dead, dead, alive],
        [alive, dead, dead, alive],
        [dead, alive, dead, dead]
    ]
    
    for i in range(4):
        for j in range(4):
            grid[y + i][x + j] = toad_pattern[i][j]

def add_beacon(grid, x, y):
    beacon_pattern = [
        [alive, alive, dead, dead],
        [alive, alive, dead, dead],
        [dead, dead, alive, alive],
        [dead, dead, alive, alive]
    ]
    
    for i in range(4):
        for j in range(4):
            grid[y + i][x + j] = beacon_pattern[i][j]

def add_pulsar(grid, x, y):
    pulsar_pattern = [
        [dead, dead, alive, alive, alive, dead, dead, dead, alive, alive, alive, dead, dead],
        [dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead],
        [alive, dead, dead, dead, dead, alive, dead, alive, dead, dead, dead, dead, alive],
        [alive, dead, dead, dead, dead, alive, dead, alive, dead, dead, dead, dead, alive],
        [alive, dead, dead, dead, dead, alive, dead, alive, dead, dead, dead, dead, alive],
        [dead, dead, alive, alive, alive, dead, dead, dead, alive, alive, alive, dead, dead],
        [dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead],
        [dead, dead, alive, alive, alive, dead, dead, dead, alive, alive, alive, dead, dead],
        [alive, dead, dead, dead, dead, alive, dead, alive, dead, dead, dead, dead, alive],
        [alive, dead, dead, dead, dead, alive, dead, alive, dead, dead, dead, dead, alive],
        [alive, dead, dead, dead, dead, alive, dead, alive, dead, dead, dead, dead, alive],
        [dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead, dead],
        [dead, dead, alive, alive, alive, dead, dead, dead, alive, alive, alive, dead, dead]
    ]
    
    for i in range(13):
        for j in range(13):
            grid[y + i][x + j] = pulsar_pattern[i][j]

def add_lwss(grid, x, y):
    lwss_pattern = [
        [dead, alive, alive, alive, alive],
        [alive, dead, dead, dead, alive],
        [dead, dead, dead, dead, alive],
        [alive, dead, dead, alive, dead]
    ]
    
    for i in range(4):
        for j in range(5):
            grid[y + i][x + j] = lwss_pattern[i][j]


def add_random_pattern(grid):
    patterns = [
        add_glider,
        add_block,
        add_beehive,
        add_blinker,
        add_toad,
        add_beacon,
        add_pulsar,
        add_lwss
    ]
    
    pattern = rnd.choice(patterns)
    # Ensure the pattern fits within the grid boundaries
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    if pattern == add_glider:
        x, y = rnd.randint(0, max_x - 2), rnd.randint(0, max_y - 2)
        pattern(grid, x, y)
    elif pattern == add_block:
        x, y = rnd.randint(0, max_x - 1), rnd.randint(0, max_y - 1)
        pattern(grid, x, y)
    elif pattern == add_beehive:
        x, y = rnd.randint(0, max_x - 3), rnd.randint(0, max_y - 3)
        pattern(grid, x, y)
    elif pattern == add_blinker:
        x, y = rnd.randint(0, max_x), rnd.randint(0, max_y - 2)
        pattern(grid, x, y)
    elif pattern == add_toad:
        x, y = rnd.randint(0, max_x - 3), rnd.randint(0, max_y - 4)
        pattern(grid, x, y)
    elif pattern == add_beacon:
        x, y = rnd.randint(0, max_x - 3), rnd.randint(0, max_y - 3)
        pattern(grid, x, y)
    elif pattern == add_pulsar:
        x, y = rnd.randint(0, max_x - 12), rnd.randint(0, max_y - 12)
        pattern(grid, x, y)
    elif pattern == add_lwss:
        x, y = rnd.randint(0, max_x - 4), rnd.randint(0, max_y - 3)
        pattern(grid, x, y)
