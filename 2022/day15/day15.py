lines = []
with open('puzzle.txt') as f:
    packet = []
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())
f.close()

lines = list(map(lambda x: [x.split(":")[0].split(" at ")[1], x.split(":")[1].split(" at ")[1]], lines))
sensors = []
beacons = []
for i in range(len(lines)):
    a,b = lines[i]
    x1,y1 = a.split("=")[1].split(",")[0], a.split("=")[-1]
    x2,y2 = b.split("=")[1].split(",")[0], b.split("=")[-1]
    x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
    sensors.append((y1,x1))
    beacons.append((y2,x2))

main = list(zip(sensors, beacons))
# Part 1

# Y = 10
Y = 2000000
def distance(p1,p2):
    return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])

def merge(a, b):
    if a[1] < b[0] or b[1] < a[0]:
        return False
    else:
        return (min(a[0], b[0]), max(a[1], b[1]))

def merge_intervals(intervals):
    ints = sorted(intervals)
    i = 0
    while i < len(ints) - 1:
        m = merge(ints[i], ints[i+1])
        if m:
            ints[i] = m
            ints.pop(i+1)
        else:
            i += 1
    return ints

cov = []
for s,b in main:
    dist = distance(s,b)
    dist2 = abs(Y-s[0])
    if dist2 <= dist: # Area would cover Line Y
        xmin, xmax = s[1]-(dist-dist2), s[1]+(dist-dist2)
        cov.append([xmin,xmax])

cov = merge_intervals(cov)[0]
num = cov[1]-cov[0]+1
deleted = set()

for b in beacons:
    if (b[0]==Y) and (cov[0] <= b[1] <= (cov[1]+1)) and b not in deleted:
        num -= 1
        deleted.add(b)

print(num)

# Part 2
def search(ymin, ymax):
    for y in range(ymin, ymax+1):
        cov, Y = [], y
        for s,b in main:
            dist = distance(s,b)
            dist2 = abs(Y-s[0])
            if dist2 <= dist: # Area would cover Line Y
                xmin, xmax = s[1]-(dist-dist2), s[1]+(dist-dist2)
                cov.append([xmin,xmax])

        cov = merge_intervals(cov)
        if len(cov)>1:
            x = cov[0][1]+1
            return x,y

# x,y = search(0,20)
x,y = search(0,4000000)
print(x*4000000+y)

# Credits: https://github.com/marcodelmastro/AdventOfCode2022/blob/main/Day15.ipynb