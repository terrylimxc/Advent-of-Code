lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(int(line.strip()))
f.close()

# Part 1
lines = list(enumerate(lines))
copied = lines.copy()
for i in lines:
    _, val = i
    idx = copied.index(i)
    target = (idx+val)%(len(copied)-1)
    copied.insert(target, copied.pop(idx))

temp = list(filter(lambda x: x[1] == 0, copied))[0]
zero_idx = copied.index(temp)
decrypted = [v for k,v in (copied[zero_idx:] + copied[:zero_idx])]

val = sum(decrypted[(i+1)*1000%len(decrypted)] for i in range(3))
print(val)

# Part 2
lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(int(line.strip()))
f.close()
lines = list(map(lambda x: x*811589153, lines))
lines = list(enumerate(lines))
copied = lines.copy()
for _ in range(10):
    for i in lines:
        _, val = i
        idx = copied.index(i)
        target = (idx+val)%(len(copied)-1)
        copied.insert(target, copied.pop(idx))

temp = list(filter(lambda x: x[1] == 0, copied))[0]
zero_idx = copied.index(temp)
decrypted = [v for k,v in (copied[zero_idx:] + copied[:zero_idx])]

val = sum(decrypted[(i+1)*1000%len(decrypted)] for i in range(3))
print(val)

# Credits: https://github.com/dkarneman/AdventOfCode/blob/main/2022/Day20part2.py