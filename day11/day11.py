lines = []
with open('puzzle.txt') as f:
    for line in f:
        x = list(line.strip())
        x = list(map(lambda y: int(y), x))
        lines.append(x)

f.close()

def update_neighbors(mat,i,j):
    # Left
    if j-1 >= 0:
        mat[i][j-1] += 1
        # Top-Left
        if i-1 >= 0:
            mat[i-1][j-1] += 1
        # Bottom-Left
        if i+1 <= len(mat)-1:
            mat[i+1][j-1] += 1
        
    # Right
    if j+1 <= len(mat[0])-1:
        mat[i][j+1] += 1
        # Top-Right
        if i-1 >= 0:
            mat[i-1][j+1] += 1
        # Bottom-Right
        if i+1 <= len(mat)-1:
            mat[i+1][j+1] += 1
    # Up
    if i-1 >= 0:
        mat[i-1][j] += 1
        
    # Down
    if i+1 <= len(mat)-1:
        mat[i+1][j] += 1

    return mat

def find_flash(mat):
    points = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] > 9:
                points.append((i,j))
    return points

def update_flash(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] > 9:
                mat[i][j] = 0 

num_flashed = 0
counter = 1
while True:
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = list(map(lambda x: x+1, line))
    queue = find_flash(lines)
    visited = queue.copy()
    all_flashed = 0 # Part 2
    while queue:
        pt = queue.pop()
        num_flashed += 1
        lines = update_neighbors(lines, pt[0], pt[1])
        visited.append(pt)
        all_flashed += 1
        
        new_pts = find_flash(lines)
        for x in new_pts:
            if x not in queue and x not in visited:
                queue.append(x)
    update_flash(lines)
    
    ## Part 1
    #if counter == 100:
    #    break

    # Part 2
    if all_flashed == (len(lines) * len(lines[0])):
        print("Occurred at Step {}".format(counter))
        break

    counter += 1
    
# Credits: https://stackoverflow.com/questions/13214809/pretty-print-2d-list/13214945#13214945
matrix = lines
s = [[str(e) for e in row] for row in matrix]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))

print("Number of flashes: {}".format(num_flashed))
