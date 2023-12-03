with open("puzzle.txt") as f:
    lines = f.read().splitlines()
f.close()

## Part 1
ans = 0
for idx, line in enumerate(lines):
    flag = True
    sets = line.split(": ")[1]
    for subset in sets.split("; "):
        combi = subset.split(", ")
        combi = list(map(lambda x: x.split(" "), combi))
        for i in combi:
            if i[1] == "red" and int(i[0]) > 12:
                flag = False
            elif i[1] == "green" and int(i[0]) > 13:
                flag = False
            elif i[1] == "blue" and int(i[0]) > 14:
                flag = False
    if flag:
        ans += (idx + 1)
print(ans)

## Part 2
ans = 0
for line in lines:
    r, g, b = 0, 0, 0
    sets = line.split(": ")[1]
    for subset in sets.split("; "):
        combi = subset.split(", ")
        combi = list(map(lambda x: x.split(" "), combi))
        for i in combi:
            if i[1] == "red" and int(i[0]) > r:
                r = int(i[0])
            elif i[1] == "green" and int(i[0]) > g:
                g = int(i[0])
            elif i[1] == "blue" and int(i[0]) > b:
                b = int(i[0])
    ans += r * g * b
print(ans)
