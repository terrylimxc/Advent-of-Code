with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()
grid = list(map(lambda x: list(map(lambda y: int(y), list(x))), lines))

# Part 1
def check_top(grid,i,j):
    start = grid[i][j]
    while i > 0:
        if grid[i-1][j] >= start:
            return False
        i -= 1
    return True

def check_bot(grid,i,j):
    start = grid[i][j]
    while i < len(grid)-1:
        if grid[i+1][j] >= start:
            return False
        i += 1
    return True

def check_left(grid,i,j):
    start = grid[i][j]
    while j > 0:
        if grid[i][j-1] >= start:
            return False
        j -= 1
    return True

def check_right(grid,i,j):
    start = grid[i][j]
    while j < len(grid[0])-1:
        if grid[i][j+1] >= start:
            return False
        j += 1
    return True

counter = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        top, bot, left, right = check_top(grid,i,j), check_bot(grid,i,j), check_left(grid,i,j), check_right(grid,i,j)
        total = top + bot + left + right
        if total > 0:
            counter += 1
counter += len(grid[0])*2 + (len(grid)-2)*2

print(counter)

# Part 2
def scenic_score(grid,i,j):
    start = grid[i][j]
    or_i, or_j = i,j

    # Top
    top = 0
    while True:
        top += 1
        if i-1 <= 0 or grid[i-1][j] >= start:
            break
        i -= 1
    i = or_i
    
    # Bottom
    bot = 0
    while True:
        bot += 1
        if i+1 >= len(grid)-1 or grid[i+1][j] >= start:
            break
        i += 1
    i = or_i

    # Left
    left = 0
    while True:
        left += 1
        if j-1 <= 0 or grid[i][j-1] >= start:
            break
        j -= 1
    j = or_j

    # Right
    right = 0
    while True:
        right += 1
        if j+1 >= len(grid[0])-1 or grid[i][j+1] >= start:
            break
        j += 1

    return top * bot * left * right

scores = []
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        scores.append(scenic_score(grid, i, j))

print(max(scores))