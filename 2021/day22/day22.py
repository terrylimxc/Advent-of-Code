from collections import Counter

steps = []
with open('puzzle.txt') as f:
    for line in f:
        line = line.strip()
        switch, coord = line.split(" ")
        switch = True if switch == "on" else False
        x,y,z = coord.split(",")
        x = tuple(map(lambda a: int(a), (x.split("=")[1]).split("..")))
        y = tuple(map(lambda a: int(a), (y.split("=")[1]).split("..")))
        z = tuple(map(lambda a: int(a), (z.split("=")[1]).split("..")))
        x0, x1 = x
        y0, y1 = y
        z0, z1 = z
        steps.append([switch,x0,x1,y0,y1,z0,z1])
        
f.close()

cubes = Counter()
for step in steps:
    switch,x0,x1,y0,y1,z0,z1 = step

##    if ((x0 < -50) or (x1 > 50)) and ((y0 < -50) or (y1 > 50)) and ((z0 < -50) or (z1 > 50)):
##        continue
    temp = Counter()

    # Add new region
    if switch:
        temp[ (x0,x1,y0,y1,z0,z1) ] += 1

    for k,v in cubes.items():
        # Find intersection in x,y,z
        int_x0 = max(x0,k[0])
        int_x1 = min(x1,k[1])
        int_y0 = max(y0,k[2])
        int_y1 = min(y1,k[3])
        int_z0 = max(z0,k[4])
        int_z1 = min(z1,k[5])
        if (int_x0 <= int_x1) and (int_y0 <= int_y1) and (int_z0 <= int_z1): # Remove double-counted region
            temp[ (int_x0, int_x1, int_y0, int_y1, int_z0, int_z1) ] -= v

    cubes.update(temp)

total = 0
for k,v in cubes.items():
    x = k[1] - k[0] + 1
    y = k[3] - k[2] + 1
    z = k[5] - k[4] + 1
    total += x*y*z*v

print(total)


