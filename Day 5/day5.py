from collections import Counter

lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())

f.close()

lines = list(map(lambda x: x.split(" -> "), lines))
for i in range(len(lines)):
    temp = lines[i]
    temp = list(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])),temp))
    lines[i] = temp

### Part 1
### Create horizontal and vertical line_segments
##def valid_points(lines):
##    points = []
##    for p1,p2 in lines:
##        # Vertical line segment
##        if p1[0] == p2[0]:
##            if p1[1] > p2[1]:
##                for i in range(p2[1], p1[1]+1):
##                    points.append((p1[0],i))
##            else:
##                for i in range(p1[1], p2[1]+1):
##                    points.append((p1[0],i))
##                
##        # Horizontal line segment
##        elif p1[1] == p2[1]:
##            if p1[0] > p2[0]:
##                for i in range(p2[0], p1[0]+1):
##                    points.append((i, p1[1]))
##            else:
##                for i in range(p1[0], p2[0]+1):
##                    points.append((i, p1[1]))           
##
##    return points
##        
##def count_overlaps(counter):
##    num = 0
##    for k,v in counter.items():
##        if v > 1:
##            num += 1
##    return num
##            
##points = valid_points(lines)
##counter = Counter(points)
##ans = count_overlaps(counter)
##print(ans)

# Part 2
# Create horizontal, vertical and diagonal line_segments
def valid_points(lines):
    points = []
    for p1,p2 in lines:
        # Vertical line segment
        if p1[0] == p2[0]:
            if p1[1] > p2[1]:
                for i in range(p2[1], p1[1]+1):
                    points.append((p1[0],i))
            else:
                for i in range(p1[1], p2[1]+1):
                    points.append((p1[0],i))
                
        # Horizontal line segment
        elif p1[1] == p2[1]:
            if p1[0] > p2[0]:
                for i in range(p2[0], p1[0]+1):
                    points.append((i, p1[1]))
            else:
                for i in range(p1[0], p2[0]+1):
                    points.append((i, p1[1]))

        # Diagonal line segment
        else:
            # Swap the 2 points if point_1_x > point_2_x
            if p1[0] > p2[0]:
                p1, p2 = p2, p1
            check, d_points = check_vertical(p1,p2)
            if check:
                points.extend(d_points)
                
    return points

def check_vertical(p1, p2):
    p2 = list(p2)
    
    # p1 < p2
    points = [p1]
    temp = list(p1)
    while temp[0] <= p2[0]:
        temp[0] += 1
        temp[1] += 1
        points.append(tuple(temp))
        if temp == p2:
            return (True, points)

    # p1 > p2
    points = [p1]
    temp = list(p1)
    while temp[0] <= p2[0]:
        temp[0] += 1
        temp[1] -= 1
        points.append(tuple(temp))
        if temp == p2:
            return (True, points)

    return (False, [])
        
        
        
def count_overlaps(counter):
    num = 0
    for k,v in counter.items():
        if v > 1:
            num += 1
    return num

points = valid_points(lines)
counter = Counter(points)
ans = count_overlaps(counter)
print(ans)

    
    
