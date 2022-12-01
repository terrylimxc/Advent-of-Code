from math import prod
lines = []
with open('puzzle.txt') as f:
    for line in f:
        x = list(line.strip())
        x = list(map(lambda y: int(y), x))
        lines.append(x)

f.close()

# Part 1
ans = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        # First row
        if i == 0:
            # First column
            if j == 0:
                if (lines[0][0] < lines[1][0]) and (lines[0][0] < lines[0][1]):
                    ans += lines[0][0] + 1
            # Last column
            elif j == len(lines[i])-1:
                if (lines[0][-1] < lines[1][-1]) and (lines[0][-1] < lines[0][-2]):
                    ans += lines[0][-1] + 1
            # Middle columns
            else:
                if (lines[i][j] < lines[i][j-1]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i+1][j]):
                    ans += lines[i][j] + 1              
        # Last row
        elif i == len(lines)-1:
            # First column
            if j == 0:
                if (lines[-1][0] < lines[-2][0]) and (lines[-1][0] < lines[-1][1]):
                    ans += lines[-1][0] + 1
            # Last column
            elif j == len(lines[i])-1:
                if (lines[-1][-1] < lines[-1][-2]) and (lines[-1][-1] < lines[-2][-1]):
                    ans += lines[-1][-1] + 1
            # Middle columns
            else:
                if (lines[i][j] < lines[i][j-1]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i-1][j]):
                    ans += lines[i][j] + 1     
        # Middle rows
        else:
            # First column
            if j == 0:
                if (lines[i][j] < lines[i-1][j]) and (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i][j+1]):
                    ans += lines[i][j] + 1 
            # Last column
            elif j == len(lines[i])-1:
                if (lines[i][j] < lines[i-1][j]) and (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i][j-1]):
                    ans += lines[i][j] + 1 
            # Middle columns
            else:
                if (lines[i][j] < lines[i][j-1]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i-1][j]):
                    ans += lines[i][j]+1

print(ans)

# Part 2
points = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        # First row
        if i == 0:
            # First column
            if j == 0:
                if (lines[0][0] < lines[1][0]) and (lines[0][0] < lines[0][1]):
                    points.append((0,0))
            # Last column
            elif j == len(lines[i])-1:
                if (lines[0][-1] < lines[1][-1]) and (lines[0][-1] < lines[0][-2]):
                    points.append((0,len(lines[i])-1))
            # Middle columns
            else:
                if (lines[i][j] < lines[i][j-1]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i+1][j]):
                    points.append((i,j))            
        # Last row
        elif i == len(lines)-1:
            # First column
            if j == 0:
                if (lines[-1][0] < lines[-2][0]) and (lines[-1][0] < lines[-1][1]):
                    points.append((len(lines)-1,0))
            # Last column
            elif j == len(lines[i])-1:
                if (lines[-1][-1] < lines[-1][-2]) and (lines[-1][-1] < lines[-2][-1]):
                    points.append((len(lines)-1,len(lines[i])-1))
            # Middle columns
            else:
                if (lines[i][j] < lines[i][j-1]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i-1][j]):
                    points.append((i,j))   
        # Middle rows
        else:
            # First column
            if j == 0:
                if (lines[i][j] < lines[i-1][j]) and (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i][j+1]):
                    points.append((i,j))
            # Last column
            elif j == len(lines[i])-1:
                if (lines[i][j] < lines[i-1][j]) and (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i][j-1]):
                    points.append((i,j))
            # Middle columns
            else:
                if (lines[i][j] < lines[i][j-1]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i-1][j]):
                    points.append((i,j))

def add_neighbours(pt, visited):
    x, y = pt
    temp = []
    # Left Bound
    if x-1 >= 0:
        new = (x-1,y)
        if new not in visited and lines[x-1][y] != 9 and lines[x-1][y] > lines[x][y]:
            temp.append(new)

    # Right Bound
    if x+1 <= len(lines)-1:
        new = (x+1,y)
        if new not in visited and lines[x+1][y] != 9 and lines[x+1][y] > lines[x][y]:
            temp.append(new)

    # Upper Bound
    if y-1 >= 0:
        new = (x,y-1)
        if new not in visited and lines[x][y-1] != 9 and lines[x][y-1] > lines[x][y]:
            temp.append(new)

    # Lower Bound
    if y+1 <= len(lines[0])-1:
        new = (x,y+1)
        if new not in visited and lines[x][y+1] != 9 and lines[x][y+1] > lines[x][y]:
            temp.append(new)

    return temp
    
size = []
for pt in points:
    visited = [pt]
    queue = add_neighbours(pt, visited) # Set up Queue

    # Set up basin
    basin = [pt] 
    basin.extend(queue)
    
    while queue:
        test = queue.pop()
        # Add all valid neighbours around point to a queue
        temp = add_neighbours(test,visited)
        visited.append(test)
        for i in temp:
            if i not in basin:
                basin.append(i)
        queue.extend(temp)
    size.append(len(basin))

size.sort(reverse=True)
ans = prod(size[:3])
print(ans)
