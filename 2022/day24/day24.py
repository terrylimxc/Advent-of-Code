grid = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        grid.append(list(line.strip()))
f.close()

# Part 1
h, w = len(grid)-2, len(grid[0])-2
blizzards = []
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        if grid[i][j] == "<":
            a,b = (0,-1)
        elif grid[i][j] == ">":
            a,b = (0,1)
        elif grid[i][j] == "^":
            a,b = (-1,0)
        elif grid[i][j] == "v":
            a,b = (1,0)
        else:
            continue
        blizzards.append((i-1,j-1,a,b))

grid_at_time = {}
def update_grid(blizzards, h, w, time):
    if time in grid_at_time:
        return grid_at_time[time]
    new_grid = []
    for i in range(h):
        row = ["."] * w
        new_grid.append(row)
    for b_x, b_y, b_x_shift, b_y_shift in blizzards:
        x = (b_x+b_x_shift*time) % h
        y = (b_y+b_y_shift*time) % w
        new_grid[x][y] = "#"
    grid_at_time[time] = new_grid
    return new_grid

def search(blizzards, time, flag):
    if flag:
        start, end= (-1,0), (h-1,w-1)
    else:
        start, end = (h,w-1), (0,0)
    queue = {start}
    while queue:
        next_steps = set()
        time += 1
        new_grid = update_grid(blizzards, h, w, time)
        for (x,y) in queue:
            if (x,y) == end:
                return time
            for a,b in [(1,0), (0,1), (0,0), (-1,0), (0,-1)]:
                if a!=0 or b!=0:
                    if x+a<0 or y+b < 0 or x+a >= h or y+b >= w:
                        continue
                if x==-1 or x == h or new_grid[x+a][y+b] == ".":
                    next_steps.add((x+a,y+b))
        queue = next_steps

print(search(blizzards,0,True))

# Part 2
trip1 = search(blizzards,0,True)
trip2 = search(blizzards,trip1,False)
trip3 = search(blizzards,trip2,True)
print(trip3)

# Credits: https://github.com/WilliamLP/AdventOfCode/blob/master/2022/day24.py