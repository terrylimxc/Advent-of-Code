points = []
folds = []
change = False

def convert_fold(x):
    x = x.split(' ')[-1]
    x = x.split('=')
    if x[0] == 'y':
        x[0] = True # Horizontal Fold
    else:
        x[0] = False # Vertical Fold
    x[1] = int(x[1])
    return x

with open('puzzle.txt') as f:
    for line in f:
        x = line.strip()
        if x == '':
            change = True
            continue
        if change:
            x = convert_fold(x)
            folds.append(x)
        else:
            x = list(map(lambda y: int(y), x.split(',')))
            points.append(x)
f.close()

def create_grid(points):
    zipped = list(zip(*points))
    max_x = max(zipped[1])+1
    max_y = max(zipped[0])+1
    
    grid = []
    for i in range(max_x):
        row = []
        for j in range(max_y):
            row.append(False)
        grid.append(row)

    for pt in points:
        grid[pt[1]][pt[0]] = True
    return grid

def count_dots(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                count += 1
    return count

def fold(grid,direction):
    orientation, line = direction
    if orientation:
        offset = 2
        for i in range(line+1, len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not grid[i-offset][j]:
                    grid[i-offset][j] = True
            offset += 2
    
        grid = grid[:line]

    else:
        for i in range(len(grid)):
            offset  = 2
            for j in range(line+1,len(grid[0])):
                if grid[i][j] and not grid[i][j-offset]:
                    grid[i][j-offset] = True
                offset += 2
        grid = list(map(lambda x: x[:line], grid))
    return grid


grid = create_grid(points)
for i in folds:
    grid = fold(grid,i)
    # Part 1
    ##print(count_dots(grid))
    ##break

# Part 2
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]:
            grid[i][j] = "x"
        else:
            grid[i][j] = " "

import pandas as pd
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    df = pd.DataFrame(grid)
    print(df)
