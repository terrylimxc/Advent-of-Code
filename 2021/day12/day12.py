lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())
f.close()

lines = list(map(lambda x: x.split('-'), lines))

# Credits: https://github.com/mebeim/aoc/blob/master/2021/README.md#day-12---passage-pathing

# Set-up graph
graph = {}
for line in lines:
    node1, node2 = line
    if node1 != 'start':
        if node2 not in graph:
            graph[node2] = []
        graph[node2].append(node1)

    if node2 != 'start':
        if node1 not in graph:
            graph[node1] = []
        graph[node1].append(node2)

# Part 1
def num_paths(graph, src, dst):
    queue = [(src, {src})]
    total = 0

    while queue:
        node, visited = queue.pop()

        # Reach end node = Valid path
        if node == dst:
            total += 1
            continue

        for neigh in graph[node]:
            # Visit neighbour if it is either not visited or an uppercase
            if neigh not in visited or neigh.isupper():
                queue.append((neigh, visited | {neigh}))

    return total

print(num_paths(graph,'start','end'))

# Part 2
def num_paths(graph, src, dst):
    queue = [(src, {src}, False)]
    total = 0

    while queue:
        node, visited, twice = queue.pop()
        
        # Reach end node = Valid path
        if node == dst:
            total += 1
            continue

        for neigh in graph[node]:
            # Visit neighbour if it is either not visited or an uppercase
            if neigh not in visited or neigh.isupper():
                queue.append((neigh, visited | {neigh}, twice))
                continue
            # Lowercase visited twice cannot visit again
            if twice:
                continue
            # Visit a lowercase and marked it as twice
            queue.append((neigh, visited | {neigh}, True))

    return total

print(num_paths(graph,'start','end'))
