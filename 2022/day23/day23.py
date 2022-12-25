from collections import deque

# Part 1
grid = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        grid.append(list(line.strip()))
f.close()

# Add padding
def pad_grid(num, grid):
    for i in range(len(grid)):
        grid[i] = ["."]*num + grid[i] + ["."]*num
    for _ in range(num):
        grid.insert(0, ["."]*len(grid[0]))
        grid.append(["."]*len(grid[0]))
    return grid

grid = pad_grid(5, grid)
directions = deque(["n", "s", "w", "e"])

# Get positions of all elves on map
elves = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            elves.append((i,j))

def propose(grid,x,y,directions):
    # Check any neighbouring elves in all 8 directions
    if (x+1) == len(grid): # Bottom border
        if (y-1) < 0: # Bottom-Left corner
            if grid[x-1][y] == "." and  grid[x-1][y+1] == "." and grid[x][y+1] == ".":
                return False, (x,y)
        elif (y+1) == len(grid[0]): # Bottom-Right corner
            if grid[x-1][y] == "." and  grid[x-1][y-1] == "." and grid[x][y-1] == ".":
                return False, (x,y)      
        else:
            if grid[x-1][y] == "." and  grid[x-1][y-1] == "." and grid[x-1][y+1] == "." and grid[x][y-1] == "." and grid[x][y+1] == ".":
                return False, (x,y)       
    elif (x-1) < 0: # Top border
        if (y-1) < 0: # Top-Left corner
            if grid[x+1][y] == "." and  grid[x][y+1] == "." and grid[x+1][y+1] == ".":
                return False, (x,y)
        elif (y+1) == len(grid[0]): # Top-Right corner
            if grid[x][y-1] == "." and  grid[x+1][y] == "." and grid[x+1][y-1] == ".":
                return False, (x,y)      
        else:
            if grid[x+1][y] == "." and  grid[x+1][y-1] == "." and grid[x+1][y+1] == "." and grid[x][y-1] == "." and grid[x][y+1] == ".":
                return False, (x,y)         
    elif (y-1) < 0: # Left border
        if grid[x-1][y] == "." and  grid[x+1][y] == "." and grid[x][y+1] == "." and grid[x-1][y+1] == "." and grid[x+1][y+1] == ".":
            return False, (x,y)      
    elif (y+1) == len(grid[0]): # Right border
        if grid[x][y-1] == "." and  grid[x-1][y] == "." and grid[x+1][y] == "." and grid[x-1][y-1] == "." and grid[x+1][y-1] == ".":
            return False, (x,y)   
    else:
        if grid[x][y-1] == "." and  grid[x][y+1] == "." and grid[x+1][y] == "." and grid[x-1][y] == "." and grid[x+1][y-1] == "." and grid[x+1][y+1] == "." and grid[x-1][y-1] == "." and grid[x-1][y+1] == ".":
            return False, (x,y)

    for dir in directions:
        if dir == "n":
            # Check if can move north at all
            if (x-1) >= 0 and (y-1) >= 0 and (y+1) < len(grid[0]):
                # Check for neighbouring elves
                if (grid[x-1][y] == ".") and (grid[x-1][y-1] == ".") and (grid[x-1][y+1] == "."):
                    return True, (x-1, y)
        elif dir == "s":
            # Check if can move south at all
            if (x+1) < len(grid) and (y-1) >= 0 and (y+1) < len(grid[0]):
                if (grid[x+1][y] == ".") and (grid[x+1][y-1] == ".") and (grid[x+1][y+1] == "."):
                    return True, (x+1, y)
        elif dir == "w":
            # Check if can move west at all
            if (y-1) >= 0 and (x-1) >= 0 and x+1 < len(grid):
                if (grid[x][y-1] == ".") and (grid[x-1][y-1] == ".") and (grid[x+1][y-1] == "."):
                    return True, (x, y-1)
        elif dir == "e":
            # Check if can move east at all
            if (y+1) < len(grid[0]) and (x-1) >= 0 and x+1 < len(grid):
                if (grid[x][y+1] == ".") and (grid[x-1][y+1] == ".") and (grid[x+1][y+1] == "."):
                    return True, (x, y+1)
    return False, (x,y)

def get_proposed_positions(positions, grid, directions):
    new_positions = []
    # First half of round: Get each proposed positions
    proposed = {}
    for x,y in positions:
        moved, new_pos = propose(grid,x,y,directions)
        if not moved: # Elf choose to stay in place
            new_positions.append(new_pos)
            continue
        if new_pos not in proposed:
            proposed[new_pos] = []
        proposed[new_pos].append((x,y))
    # Second half of round: Move valid ones
    for k,v in proposed.items():
        if len(v) == 1:
            old_x,old_y = v[0]
            new_x,new_y = k
            grid[old_x][old_y], grid[new_x][new_y] = ".", "#"
            new_positions.append(k)
        else:
            new_positions.extend(v)
    # Shift 1st direction to back
    directions.rotate(-1)
    return new_positions, grid, directions

for _ in range(10):
    elves, grid, directions = get_proposed_positions(elves, grid, directions)

def trim_rows(grid):
    empty = list(map(lambda x: "#" in x, grid))
    for start_idx in range(len(empty)):
        if empty[start_idx]:
            break
    for end_idx in range(1, len(empty)+1):
        if empty[-end_idx]:
            break
    if end_idx != 1:
        grid = grid[start_idx:-end_idx+1]
    else:
        grid = grid[start_idx:]
    return grid

def count_empty(grid):
    # Trim away empty rows
    grid = trim_rows(grid)
    # Trim away empty columns
    grid = list(map(list, zip(*grid)))
    grid = trim_rows(grid)
    grid = list(map(list, zip(*grid)))

    # Count empty tiles
    counts = 0
    for row in grid:
        counts += row.count(".")
    return counts

ans = count_empty(grid)
# print('\n'.join([''.join([str(cell) for cell in row]) for row in grid]))
print(ans)

# Part 2
grid = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        grid.append(list(line.strip()))
f.close()

# Add padding
grid = pad_grid(50, grid)
directions = deque(["n", "s", "w", "e"])

# Get positions of all elves on map
elves = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            elves.append((i,j))

def get_proposed_positions(positions, grid, directions):
    new_positions = []
    # First half of round: Get each proposed positions
    proposed = {}
    count = len(positions)
    for x,y in positions:
        moved, new_pos = propose(grid,x,y,directions)
        if not moved: # Elf choose to stay in place
            count -= 1
            new_positions.append(new_pos)
            continue
        if new_pos not in proposed:
            proposed[new_pos] = []
        proposed[new_pos].append((x,y))
    if count == 0:
        return True, new_positions, grid, directions
    # Second half of round: Move valid ones
    for k,v in proposed.items():
        if len(v) == 1:
            old_x,old_y = v[0]
            new_x,new_y = k
            grid[old_x][old_y], grid[new_x][new_y] = ".", "#"
            new_positions.append(k)
        else:
            new_positions.extend(v)
    # Shift 1st direction to back
    directions.rotate(-1)
    return False, new_positions, grid, directions

counter = 1
while True:
    flag, elves, grid, directions = get_proposed_positions(elves, grid, directions)
    if flag:
        break
    counter += 1
print(counter)