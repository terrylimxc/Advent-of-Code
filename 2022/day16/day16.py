lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())
f.close()

main = {}
for i in range(len(lines)):
    fr, valves = lines[i].split("; ")
    src, fr = fr.split(" ")[1], int(fr.split("=")[-1])
    if "valves" in valves:
        valves = (valves.split(" valves ")[-1]).split(", ")
    else:
        valves = [valves.split(" valve ")[-1]]
    main[src] = (fr, valves)

class Valve:
    def __init__(self, name, fr, neighbours):
        self.name = name
        self.fr = fr
        self.neighbours = neighbours

for k,v in main.items():
    main[k] = Valve(k, v[0], v[1])
    
# Part 1
def floyd_warshall(valves):
    # Set up distance matrix
    dist = {}
    for k1 in valves:
        temp = {}
        for k2 in valves:
            temp[k2] = float("inf")
        dist[k1] = temp

    for k in valves:
        dist[k][k] = 0 # Travelling to itself: distance 0
        for child in valves[k].neighbours: # Travelling to immediate neighbour: distance 1
            dist[k][child] = 1
    
    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def all_paths(pos, opened_valves, time):
    for i in possible_valves:
        if i not in opened_valves and distances[pos][i] < time:
            opened_valves.append(i)
            yield from all_paths(i,opened_valves,time-distances[pos][i]-1)
            opened_valves.pop()
    yield opened_valves.copy()

def calc_pressure(path, time):
    curr, total = "AA", 0
    for i in path:
        time -= distances[curr][i] + 1
        total += main[i].fr*time
        curr = i
    return total

distances = floyd_warshall(main)
possible_valves = [k for k,v in main.items() if v.fr>0]

paths = list(all_paths("AA", [], 30))
print(max(map(lambda x: calc_pressure(x, 30), paths)))

# Part 2
paths = list(all_paths("AA", [], 26))

x = {}
for p in paths:
    val = calc_pressure(p, 26)
    k = tuple(sorted(p))
    if k not in x:
        x[k] = val
    else:
        x[k] = max(x[k], val)

x = list(x.items())

ans = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        me_opened, me_pressure = x[i]
        el_opened, el_pressure = x[j]

        if not set(me_opened).intersection(el_opened):
            ans = max(ans, me_pressure+el_pressure)
print(ans)
