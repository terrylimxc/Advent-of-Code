lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().split(",")
        line = tuple(map(lambda x: int(x), line))
        lines.append(line)
f.close()

# Part 1
def adj_cubes(cube):
    x,y,z = cube
    return (x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z-1), (x,y,z+1)
area = 0
checked = set()
for cube in lines:
    area += 6 # Each cube got 6 sides
    # Check whether current cube is adjacent to other cubes
    for a in adj_cubes(cube):
        if a in checked:
            area -= 2
    # Add current cube to checked list
    checked.add(cube)
print(area)

# Part 2
all_cubes = {(i,j,k) for i in range(30) for j in range(30) for k in range(30)}
remaining_cubes = all_cubes - checked

# BFS
queue = [(0,0,0)]
while queue:
    curr = queue.pop()
    if curr in remaining_cubes:
        remaining_cubes.remove(curr)
        queue.extend(adj_cubes(curr))

for cube in remaining_cubes:
    area += 6 # Each cube got 6 sides
    # Check whether current cube is adjacent to other cubes
    for a in adj_cubes(cube):
        if a in checked:
            area -= 2
    # Add current cube to checked list
    checked.add(cube)
print(area)

# Credits: https://github.com/AllanTaylor314/AdventOfCode/blob/main/2022/18.py
    

