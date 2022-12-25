with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        jet = list(line.strip())
f.close()

# Part 1
def piece(time):
    if time == 0:
        return [[1,1,1,1]], 4, 1
    elif time == 1:
        return [[0,1,0],[1,1,1],[0,1,0]], 3, 3
    elif time == 2:
        return [[0,0,1],[0,0,1],[1,1,1]], 3, 3
    elif time == 3: 
        return [[1],[1],[1],[1]], 1, 4
    elif time == 4:
        return [[1,1],[1,1]], 2, 2

def get_position(h,time):
    if time == 0:
        return [(h+3,2),(h+3,3),(h+3,4),(h+3,5)]
    elif time == 1:
        return [(h+3,3),(h+4,2),(h+4,3),(h+4,4),(h+5,3)]
    elif time == 2:
        return [(h+3,2),(h+3,3),(h+3,4),(h+4,4),(h+5,4)]
    elif time == 3:
        return [(h+3,2),(h+4,2),(h+5,2),(h+6,2)]
    elif time == 4:
        return [(h+3,2),(h+3,3),(h+4,2),(h+4,3)]
    
def update_move(move, pos, grid):
    new_pos = []
    if move == "<":
        for i in pos:
            if i[1] == 0 or grid[i[0]][i[1]-1] != 0: # Either current rock or another rock is already at left wall 
                return pos
            new_pos.append((i[0], i[1]-1))
        return new_pos
    elif move == ">":
        for i in pos:
            if i[1] == 6 or grid[i[0]][i[1]+1] != 0: # Either current rock or another rock is already at right wall 
                return pos
            new_pos.append((i[0], i[1]+1))
        return new_pos

def move_down(pos, grid):
    new_pos = []
    for x,y in pos:
        if x==0 or grid[x-1][y] != 0: # Check whether reach limit
            return None, False
        new_pos.append((x-1,y))
    return new_pos, True

grid = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
height, idx = -1, 0

for i in range(2022):
    rock, rock_w, rock_h = piece(i%5)
    pos = get_position(height+1, i%5)
    for _ in range(rock_h):
        grid.append([0,0,0,0,0,0,0])
    while True:
        if idx >= len(jet): # Restart jet
            idx -= len(jet)
        pos = update_move(jet[idx], pos, grid)
        idx += 1
        new_pos, fall = move_down(pos, grid)
        if not fall: # Change to new rock and update height
            for x,y in pos:
                grid[x][y] = 1
                if x > height:
                    height = x
            break
        pos = new_pos
print(height+1)

# Part 2
grid = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
height, idx = -1, 0
peaks = [0,0,0,0,0,0,0]
seen, height_dict = {}, {}
flag = True
for i in range(1000000000000):
    rock, rock_w, rock_h = piece(i%5)
    pos = get_position(height+1, i%5)
    for _ in range(rock_h):
        grid.append([0,0,0,0,0,0,0])
    while True:
        if idx >= len(jet): # Restart jet
            idx -= len(jet)
        pos = update_move(jet[idx], pos, grid)
        idx += 1
        new_pos, fall = move_down(pos, grid)
        if not fall: # Change to new rock and update height
            temp = height
            for x,y in pos:
                grid[x][y] = 1
                if x > height:
                    height = x
            max_diff = height - temp
            for j in range(len(peaks)):
                peaks[j] -= max_diff
            for x,y in pos:
                peaks[y] = max(peaks[y], x-height)
            break
        pos = new_pos
    height_dict[i] = height
    key = (tuple(peaks), idx, i%5)
    if key in seen and seen[key] != 0:
        temp = seen[key]
        diff = height - height_dict[seen[key]]
        cycle = i - seen[key]
        goal = 1000000000000 - seen[key]
        num_cycles, remaining_cycle = goal // cycle, goal % cycle
        temp_h = height_dict[seen[key]+remaining_cycle]
        flag = False
        break
    seen[key] = i

print(height+1) if flag else print(temp_h + (num_cycles*diff))

# Credits: https://topaz.github.io/paste/#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