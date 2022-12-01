lines = []
with open('puzzle.txt') as f:
    for line in f:
        x = list(line.strip())
        x = list(map(lambda y: int(y), x))
        lines.append(x)

f.close()

# Part 1
# Credits: https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/
##def dijsktra(graph, initial, end):
##    shortest_paths = {initial: (None, 0)}
##    current_node = initial
##    visited = set()
##
##    while current_node != end:
##        visited.add(current_node)
##        x,y = current_node
##        dest = []
##        if y+1 <= len(graph[0])-1:
##            dest.append((x, y+1)) # Go right
##        if x+1 <= len(graph)-1:
##            dest.append((x+1, y)) # Go down
##        curr_weight = shortest_paths[current_node][1]
##
##        for node in dest:
##            x,y = node
##            weight = graph[x][y] + curr_weight
##            if node not in shortest_paths:
##                shortest_paths[node] = (current_node, weight)
##            else:
##                current_smallest_weight = shortest_paths[node][1]
##                if current_smallest_weight > weight:
##                    shortest_paths[node] = (current_node, weight)
##        
##        next_dest = {}
##        for k,v in shortest_paths.items():
##            if k not in visited:
##                next_dest[k] = v
##
##        current_node = min(next_dest, key=lambda x: next_dest[x][1])
##
##    # Back-track
##    path = []
##    while current_node is not None:
##        path.append(graph[current_node[0]][current_node[1]])
##        current_node = shortest_paths[current_node][0]
##    path.pop()
##    
##    return sum(path)

# Part 1 (Revised using PQ)
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
            if new_node not in visited:
                new_dist = graph[x][y+1] + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if x+1 <= len(graph)-1: # Go down
            new_node = (x+1,y)
            if new_node not in visited:
                new_dist = graph[x+1][y] + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if x-1 >= 0: # Go up
            new_node = (x-1,y)
            if new_node not in visited:
                new_dist = graph[x-1][y] + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        if y-1 >= 0: # Go left
            new_node = (x,y-1)
            if new_node not in visited:
                new_dist = graph[x][y-1] + curr_dist
                pq.put((new_dist, new_node))
                visited.add(new_node)
        
print(dijsktra(lines, (0,0), (len(lines)-1, len(lines[0])-1)))

# Part 2
# Split 5x5 grid into the following sections:
##ABCDE
##BCDEF
##CDEFG
##DEFGH
##EFGHI

def create_row(grid, start, ref):
    for i in range(start, start+4):
        next_mat = ref[i]
        for j in range(len(grid)):
            grid[j].extend(next_mat[j])
    return grid

def create_map(tile):
    # Starting from Top Left, the bottom right tile would be +8 of it
    ref = {0:tile}
    
    # Create variations
    for counter in range(1,9):
        new_mat = []
        for i in range(len(tile)):
            curr_row = tile[i]
            new_row = map(lambda x: x+1, curr_row) # Add 1 to every value in row
            new_row = list(map(lambda x: 1 if x>9 else x, new_row)) # Convert >9 to 1
            new_mat.append(new_row)
        ref[counter] = new_mat
        tile = new_mat

    # Piece variations together to 5x5 grid
    final = []
    for i in range(5):
        curr_start = ref[i]
        new_row = create_row(curr_start, i+1, ref)
        final.extend(new_row)
    return final
    
grid = create_map(lines)

print(dijsktra(grid, (0,0), (len(grid)-1, len(grid[0])-1)))
