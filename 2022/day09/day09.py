with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()
lines = list(map(lambda x: x.split(" "), lines))
lines = list(map(lambda x: [x[0], int(x[1])], lines))

# Part 1
visited = []
head = [0,0]
tail = [0,0]
visited.append(tail.copy())

def move(dir, amt, head, tail, visited):
    if dir == "L":
        for _ in range(amt):
            head[0] -= 1
            tail, visited = check(head, tail, visited)
    elif dir == "R":
        for _ in range(amt):
            head[0] += 1
            tail, visited = check(head, tail, visited)
    elif dir == "U":
        for _ in range(amt):
            head[1] += 1
            tail, visited = check(head, tail, visited)
    elif dir == "D":
        for _ in range(amt):
            head[1] -= 1
            tail, visited = check(head, tail, visited)
    return head, tail, visited

def check(head, tail, visited):
    if head[1] == tail[1]: # Same row
        if (head[0] - tail[0]) == 2: # Head 2 steps on the left of tail
            tail[0] += 1
            visited.append(tail.copy())
        elif (head[0] - tail[0]) == -2: # Head 2 steps on the right of tail
            tail[0] -= 1
            visited.append(tail.copy()) 
    elif head[0] == tail[0]: # Same column
        if (head[1] - tail[1]) == 2: # Head 2 steps on the top of tail
            tail[1] += 1
            visited.append(tail.copy())
        elif (head[1] - tail[1]) == -2: # Head 2 steps on the bottom of tail
            tail[1] -= 1
            visited.append(tail.copy()) 
    else:
        if ((head[0]-tail[0]) == 1 and head[1]-tail[1] == 2) or ((head[0]-tail[0]) == 2 and head[1]-tail[1] == 1):
            # Move diagonally right-up
            tail[0] += 1
            tail[1] += 1
            visited.append(tail.copy())
        elif ((head[0]-tail[0]) == -1 and head[1]-tail[1] == 2) or ((head[0]-tail[0]) == -2 and head[1]-tail[1] == 1):
            # Move diagonally left-up
            tail[0] -= 1
            tail[1] += 1
            visited.append(tail.copy())
        elif ((head[0]-tail[0]) == 1 and head[1]-tail[1] == -2) or ((head[0]-tail[0]) == 2 and head[1]-tail[1] == -1):
            # Move diagonally right-down
            tail[0] += 1
            tail[1] -= 1
            visited.append(tail.copy())
        elif ((head[0]-tail[0]) == -1 and head[1]-tail[1] == -2) or ((head[0]-tail[0]) == -2 and head[1]-tail[1] == -1):
            # Move diagonally left-down
            tail[0] -= 1
            tail[1] -= 1
            visited.append(tail.copy())
    return tail, visited

for line in lines:
    head, tail, visited = move(line[0], line[1], head, tail, visited)

print(len(set(map(lambda x: tuple(x), visited))))

# Part 2
visited = []
head = [0,0]
k1,k2,k3,k4,k5,k6,k7,k8 = [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
tail = [0,0]
visited.append(tail.copy())

def move(dir, amt, head, k1, k2, k3, k4, k5, k6, k7, k8, tail, visited):
    if dir == "L":
        for _ in range(amt):
            head[0] -= 1
            k1, visited = check(head, k1, visited, False)
            k2, visited = check(k1, k2, visited, False)
            k3, visited = check(k2, k3, visited, False)
            k4, visited = check(k3, k4, visited, False)
            k5, visited = check(k4, k5, visited, False)
            k6, visited = check(k5, k6, visited, False)
            k7, visited = check(k6, k7, visited, False)
            k8, visited = check(k7, k8, visited, False)
            tail, visited = check(k8, tail, visited, True)
    elif dir == "R":
        for _ in range(amt):
            head[0] += 1
            k1, visited = check(head, k1, visited, False)
            k2, visited = check(k1, k2, visited, False)
            k3, visited = check(k2, k3, visited, False)
            k4, visited = check(k3, k4, visited, False)
            k5, visited = check(k4, k5, visited, False)
            k6, visited = check(k5, k6, visited, False)
            k7, visited = check(k6, k7, visited, False)
            k8, visited = check(k7, k8, visited, False)
            tail, visited = check(k8, tail, visited, True)
    elif dir == "U":
        for _ in range(amt):
            head[1] += 1
            k1, visited = check(head, k1, visited, False)
            k2, visited = check(k1, k2, visited, False)
            k3, visited = check(k2, k3, visited, False)
            k4, visited = check(k3, k4, visited, False)
            k5, visited = check(k4, k5, visited, False)
            k6, visited = check(k5, k6, visited, False)
            k7, visited = check(k6, k7, visited, False)
            k8, visited = check(k7, k8, visited, False)
            tail, visited = check(k8, tail, visited, True)
    elif dir == "D":
        for _ in range(amt):
            head[1] -= 1
            k1, visited = check(head, k1, visited, False)
            k2, visited = check(k1, k2, visited, False)
            k3, visited = check(k2, k3, visited, False)
            k4, visited = check(k3, k4, visited, False)
            k5, visited = check(k4, k5, visited, False)
            k6, visited = check(k5, k6, visited, False)
            k7, visited = check(k6, k7, visited, False)
            k8, visited = check(k7, k8, visited, False)
            tail, visited = check(k8, tail, visited, True)
    return head, k1, k2, k3, k4, k5, k6, k7, k8, tail, visited

def check(head, tail, visited, flag):
    if head[1] == tail[1]: # Same row
        if (head[0] - tail[0]) == 2: # Head 2 steps on the left of tail
            tail[0] += 1
            if flag:
                visited.append(tail.copy())
        elif (head[0] - tail[0]) == -2: # Head 2 steps on the right of tail
            tail[0] -= 1
            if flag:
                visited.append(tail.copy())
    elif head[0] == tail[0]: # Same column
        if (head[1] - tail[1]) == 2: # Head 2 steps on the top of tail
            tail[1] += 1
            if flag:
                visited.append(tail.copy())
        elif (head[1] - tail[1]) == -2: # Head 2 steps on the bottom of tail
            tail[1] -= 1
            if flag:
                visited.append(tail.copy())
    else:
        if ((head[0]-tail[0]) == 1 and head[1]-tail[1] == 2) or ((head[0]-tail[0]) == 2 and head[1]-tail[1] == 1) or ((head[0]-tail[0]) == 2 and head[1]-tail[1] == 2):
            # Move diagonally right-up
            tail[0] += 1
            tail[1] += 1
            if flag:
                visited.append(tail.copy())
        elif ((head[0]-tail[0]) == -1 and head[1]-tail[1] == 2) or ((head[0]-tail[0]) == -2 and head[1]-tail[1] == 1) or ((head[0]-tail[0]) == -2 and head[1]-tail[1] == 2):
            # Move diagonally left-up
            tail[0] -= 1
            tail[1] += 1
            if flag:
                visited.append(tail.copy())
        elif ((head[0]-tail[0]) == 1 and head[1]-tail[1] == -2) or ((head[0]-tail[0]) == 2 and head[1]-tail[1] == -1) or ((head[0]-tail[0]) == 2 and head[1]-tail[1] == -2):
            # Move diagonally right-down
            tail[0] += 1
            tail[1] -= 1
            if flag:
                visited.append(tail.copy())
        elif ((head[0]-tail[0]) == -1 and head[1]-tail[1] == -2) or ((head[0]-tail[0]) == -2 and head[1]-tail[1] == -1) or ((head[0]-tail[0]) == -2 and head[1]-tail[1] == -2):
            # Move diagonally left-down
            tail[0] -= 1
            tail[1] -= 1
            if flag:
                visited.append(tail.copy())
    return tail, visited

counter = 1
for line in lines:
    head, k1, k2, k3, k4, k5, k6, k7, k8, tail, visited = move(line[0], line[1], head, k1, k2, k3, k4, k5, k6, k7, k8, tail, visited)

print(len(set(map(lambda x: tuple(x), visited))))

