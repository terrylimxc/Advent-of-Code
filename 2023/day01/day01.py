import re

with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

## Part 1
ans = 0
for line in lines:
    front, end = re.search(r'[0-9]+', line), re.search(r'[0-9]+', line[::-1])
    num = "".join([front.group()[0], end.group()[0]])
    ans += int(num)

print(ans)

## Part 2
ans = 0
for line in lines:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")

    front, end = re.search(r'[0-9]+', line), re.search(r'[0-9]+', line[::-1])
    num = "".join([front.group()[0], end.group()[0]])
    ans += int(num)

print(ans)