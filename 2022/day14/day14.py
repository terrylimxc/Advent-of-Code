lines = []
with open('puzzle.txt') as f:
    packet = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())
f.close()

# Part 1
lines = list(map(lambda x: x.split(" -> "), lines))
lines = list(map(lambda x: list(map(lambda y: [int(y.split(",")[0]), int(y.split(",")[1])], x)), lines))

rocks = []
for i in lines:
    for j in range(len(i)-1):
        start, end = i[j], i[j+1]
        if start[0] == end[0]:
            if (end[1]-start[1]) > 0: # Increasing
                r = list(range(start[1], end[1]+1))
            else: # Decreasing
                r = list(range(end[1], start[1]+1))
            rocks.extend(list(map(lambda x: [x, start[0]], r)))
        else:
            if (end[0]-start[0]) > 0: # Increasing
                r = list(range(start[0], end[0]+1))
            else: # Decreasing
                r = list(range(end[0], start[0]+1))
            rocks.extend(list(map(lambda x: [start[1], x], r)))

grid = []
for i in range(700):
    temp = []
    for j in range(700):
        temp.append(".")
    grid.append(temp)

for i,j in rocks:
    grid[i][j] = "#"

def move_sand(grid, x, y):
    if grid[x][y] == "." and grid[x+1][y] in ("#", "o") and grid[x+1][y-1] in ("#", "o") and grid[x+1][y+1] in ("#", "o"): 
        # Stable
        return (x,y)
    else:
        # Move down
        if grid[x][y] == "." and grid[x+1][y] == ".":
            return move_sand(grid,x+1,y)
        # Move diagonally left
        if grid[x][y] == "." and grid[x+1][y] in ("#", "o") and grid[x+1][y-1] == ".":
            return move_sand(grid,x+1,y-1)
        # Move diagonally right
        if grid[x][y] == "." and grid[x+1][y] in ("#", "o") and grid[x+1][y+1] == ".":
            return move_sand(grid,x+1,y+1) 

counter = 0
while True:
    try:
        next_sand = [0,500]
        while True: # Find 1st possible position
            if (grid[next_sand[0]][next_sand[1]] == ".") and (grid[next_sand[0]+1][next_sand[1]] != "."):
                break
            next_sand = [next_sand[0]+1, next_sand[1]]

        next_sand = move_sand(grid, next_sand[0], next_sand[1])

        grid[next_sand[0]][next_sand[1]] = "o"
        counter += 1
    except IndexError: # Into the abyss
        break

print(counter)

# Part 2
grid = []
for i in range(700):
    temp = []
    for j in range(700):
        temp.append(".")
    grid.append(temp)

for i,j in rocks:
    grid[i][j] = "#"

max_x = max(map(lambda x: x[0], rocks)) + 2

for j in range(len(grid[0])):
    grid[max_x][j] = "#"

counter = 0
while True:
    next_sand = [0,500]
    while True: # Find 1st possible position
        if (grid[next_sand[0]][next_sand[1]] == ".") and (grid[next_sand[0]+1][next_sand[1]] != "."):
            break
        next_sand = [next_sand[0]+1, next_sand[1]]

    next_sand = move_sand(grid, next_sand[0], next_sand[1])

    grid[next_sand[0]][next_sand[1]] = "o"
    counter += 1

    if next_sand == (0,500):
        break

print(counter)
