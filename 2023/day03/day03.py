import itertools
with open("puzzle.txt") as f:
    lines = f.read().splitlines()
f.close()

## Part 1
def find_all_nums(grid):
    main = {}
    for i in range(len(grid)):
        temp, flag = "", False
        pos = []
        for j in range(len(grid[i])):
            if flag and (not grid[i][j].isdigit()):
                if temp not in main:
                    main[temp] = [pos]
                else:
                    main[temp].append(pos)
                temp, flag = "", False
                pos = []
            elif grid[i][j].isdigit():
                temp += grid[i][j]
                pos.append((i,j))
                flag = True

        if flag:
            if temp not in main:
                main[temp] = [pos]
            else:
                main[temp].append(pos)

    return main

def is_part_num(pos, grid):
    x,y = pos

    # Check Up
    if (x-1) >= 0:
        if grid[x-1][y] not in '01234566789.':
            return True
    
        # Check Top Left
        if ((y-1) >= 0) and (grid[x-1][y-1] not in '01234566789.'):
            return True

        # Check Top Right 
        if ((y+1) < len(grid[0])) and (grid[x-1][y+1] not in '01234566789.'):
            return True
            
    # Check Down
    if (x+1) < len(grid):
        if grid[x+1][y] not in '01234566789.':
            return True 

        # Check Bottom Left
        if ((y-1) >= 0) and (grid[x+1][y-1] not in '01234566789.'):
            return True        

        # Check Bottom Right
        if ((y+1) < len(grid[0])) and (grid[x+1][y+1] not in '01234566789.'):
            return True
    
    # Check Left
    if ((y-1) >= 0) and (grid[x][y-1] not in '01234566789.'):
        return True

    # Check Right 
    if ((y+1) < len(grid[0])) and (grid[x][y+1] not in '01234566789.'):
        return True  

    return False
    

all_num_pos = find_all_nums(lines)
ans = 0
for k,v in all_num_pos.items():
    for possible_pos in v:
        flag = False
        for pos in possible_pos:
            if is_part_num(pos,lines):
                flag = True
        if flag:
            ans += int(k)

print(ans)

## Part 2
def find_all_nums_reversed(grid):
    main = {}
    for i in range(len(grid)):
        temp, flag = "", False
        pos = []
        for j in range(len(grid[i])):
            if flag and (not grid[i][j].isdigit()):
                for item in pos:
                    main[item] = temp
                temp, flag = "", False
                pos = []
            elif grid[i][j].isdigit():
                temp += grid[i][j]
                pos.append((i,j))
                flag = True

        if flag:
            for item in pos:
                main[item] = temp

    return main

def find_all_gears(grid):
    return [
        (i, j)
        for i, j in itertools.product(range(len(grid)), range(len(grid[0])))
        if grid[i][j] == "*"
    ]

def generate_all_directions(x,y):
    return [(x-1,y-1), (x-1,y), (x-1, y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]


reversed_all_num_pos = find_all_nums_reversed(lines)
all_gears = find_all_gears(lines)

ans = 0
aaa = []
for gear in all_gears:
    poss = generate_all_directions(gear[0], gear[1])
    temp = []
    curr = None
    for i in poss:
        val = reversed_all_num_pos.get(i)
        if val != None:
            lst = all_num_pos[val]

            if curr is not None:
                if i in curr:
                    continue
                else:
                    curr = None
            
            for xxx in lst:
                if i in xxx and curr is None:
                    temp.append(val)
                    curr = xxx
                    break
        else:
            curr = None

    if len(temp) == 2:
        aaa.append(temp)
        ans += (int(temp[0]) * int(temp[1]))   

print(ans)