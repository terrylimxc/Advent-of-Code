with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

## Part 1
highest, elf, curr = -1, -1, 1
temp = 0
for v in lines:
    if v:
        temp += int(v)
    else:
        if temp >= highest:
            highest = temp
            elf = curr
        temp = 0
        curr += 1

if temp >= highest:
    highest = temp
    elf = curr

print(highest)

## Part 2
main = {}
highest, curr = -1, 1
temp = 0
for v in lines:
    if v:
        temp += int(v)
    else:
        main[curr] = temp
        temp = 0
        curr += 1
main = sorted(main.items(), key=lambda x: x[1], reverse=True)
print(sum(list(map(lambda x: x[1], main[:3]))))