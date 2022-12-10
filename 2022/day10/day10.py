with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

lines = list(map(lambda x: x.split(" "), lines))

# Part 1
cycle = 0
X = 1
main = []
for cmd in lines:
    if len(cmd) == 1: #noop command
        cycle += 1
        if (cycle==20) or ((cycle-20)%40==0):
            main.append(X)
    else: #addx command
        _, value = cmd
        value = int(value)
        cycle += 2
        X += value
        if (cycle==20) or ((cycle-20)%40==0):
            main.append(X-value)
        elif ((cycle-1)==20) or ((cycle-21)%40==0):
            main.append(X-value)

total = 0
for i in range(len(main)):
    if i == 0:
        total += main[i] * 20
    else:
        total += main[i] * ((i*40)+20)

print(total)

# Part 2
cycle = 0
X = 1
main = []
sprite = "#"*3 + "."*37
row = ""
for cmd in lines:
    if len(cmd) == 1: #noop command
        cycle += 1
        row += sprite[cycle-1]
    else: #addx command
        _, value = cmd
        value = int(value)

        cycle += 1
        row += sprite[cycle-1]

        if len(row) == 40:
            main.append(row)
            row = ""
            cycle = 0

        cycle += 1
        X += value
        row += sprite[cycle-1]

        sprite = list("."*40)
        if X == 39:
            sprite[X], sprite[X-1], sprite[0] = "#", "#", "#"
        else:
            sprite[X], sprite[X-1], sprite[X+1] = "#", "#", "#"
        sprite = "".join(sprite)

    if len(row) == 40:
        main.append(row)
        row = ""
        cycle = 0

for i in main:
    print(i)
