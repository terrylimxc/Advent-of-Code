lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)
f.close()

lines = list(map(lambda x: x.strip(), lines))
lines = list(filter(lambda x: x != "", lines))
lines = list(map(lambda x: list(x), lines))

# Part 1

# Find start and end
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "S":
            start = (i,j)
        elif lines[i][j] == "E":
            end = (i,j)

# Pre-processing
lines[start[0]][start[1]] = "a"
lines[end[0]][end[1]] = "z"
for i in range(len(lines)):
    for j in range(len(lines[0])):
        lines[i][j] = ord(lines[i][j])-ord("a")

def check_valid(lines, old_i, old_j, new_i, new_j,  visited):
    curr_val = lines[old_i][old_j]
    new_val = lines[new_i][new_j]

    if (new_i,new_j) not in visited: # Yet to visit
        if (new_val-curr_val)<=1: # Possible move
            return True
    return False

# Source: https://github.com/terrylimxc/Advent-of-Code/blob/main/2021/day15/day15.py
from queue import PriorityQueue
def dijsktra(graph, initial, end):
    pq = PriorityQueue()
    pq.put((0, initial))
    
    visited = set()
    visited.add(initial)
    while pq:
        curr_dist, curr_node = pq.get()

        # Terminate if end is reached
        if curr_node == end:
            return curr_dist

        x,y = curr_node
        if y+1 <= len(graph[0])-1: # Go right
            new_node = (x,y+1)
            if check_valid(lines, x, y, x, y+1,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if x+1 <= len(graph)-1: # Go down
            new_node = (x+1,y)
            if check_valid(lines, x, y, x+1, y,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if x-1 >= 0: # Go up
            new_node = (x-1,y)
            if check_valid(lines, x, y, x-1, y,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if y-1 >= 0: # Go left
            new_node = (x,y-1)
            if check_valid(lines, x, y, x, y-1,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        
print(dijsktra(lines, start, end))

# Part 2
# Find all a
starts = []
for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i][j] == 0:
            starts.append((i,j))

# Reverse-search from end point to a possible shortest start point
def check_valid(lines, old_i, old_j, new_i, new_j,  visited):
    curr_val = lines[old_i][old_j]
    new_val = lines[new_i][new_j]

    if (new_i,new_j) not in visited: # Yet to visit
        if (new_val-curr_val)>=-1: # Possible move
            return True
    return False

def dijsktra(graph, initial, ends):
    pq = PriorityQueue()
    pq.put((0, initial))
    
    visited = set()
    visited.add(initial)
    while pq:
        curr_dist, curr_node = pq.get()

        # Terminate if end is reached
        if curr_node in ends:
            return curr_dist

        x,y = curr_node
        if y+1 <= len(graph[0])-1: # Go right
            new_node = (x,y+1)
            if check_valid(lines, x, y, x, y+1,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if x+1 <= len(graph)-1: # Go down
            new_node = (x+1,y)
            if check_valid(lines, x, y, x+1, y,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if x-1 >= 0: # Go up
            new_node = (x-1,y)
            if check_valid(lines, x, y, x-1, y,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if y-1 >= 0: # Go left
            new_node = (x,y-1)
            if check_valid(lines, x, y, x, y-1,  visited):
                new_dist = 1 + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)

print(dijsktra(lines, end, starts))