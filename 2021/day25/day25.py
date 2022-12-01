grid = []
with open('puzzle.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
        
f.close()

RIGHT = len(grid[0])-1
BOTTOM = len(grid)-1

def find_all_east_south(grid):
    east = []
    south = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Find all east-moving cucumbers
            if grid[i][j] == '>':
                east.append((i,j))
            # Find all south-moving cucumbers
            elif grid[i][j] == 'v':
                south.append((i,j))
    return east, south

def find_valid_east(grid, east):
    valid_east = []
    for i,j in east:
        # Special case: Right Boundary
        if j == RIGHT:
            if grid[i][0] == '.':
                valid_east.append((i,j,i,0,'>'))
        # Normal case
        else:
            if grid[i][j+1] == '.':
                valid_east.append((i,j,i,j+1,'>'))
    return valid_east

def find_valid_south(grid, south):
    valid_south = []
    for i,j in south:
        # Special case: Lower Boundary
        if i == BOTTOM:
            if grid[0][j] == '.':
                valid_south.append((i,j,0,j,'v'))
        # Normal case
        else:
            if grid[i+1][j] == '.':
                valid_south.append((i,j,i+1,j,'v'))
    return valid_south

def move(grid, moves):
    for move in moves:
        o_r, o_c, n_r, n_c, sym = move
        grid[o_r][o_c], grid[n_r][n_c] = '.', sym
    return grid

steps = 0
while True:
    # Find all possible moves
    east, south = find_all_east_south(grid)

    # Find all valid east
    valid_east = find_valid_east(grid, east)

    # Move all valid east-moving cucumbers
    grid = move(grid, valid_east)
    
    # Find all valid south
    valid_south = find_valid_south(grid, south)

    # Move all valid south-moving cucumbers
    grid = move(grid, valid_south)

    steps += 1
    
    if len(valid_east) == 0 and len(valid_south) == 0:
        break
    
print(steps)
        
