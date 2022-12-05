with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

# Part 1
total = 0
for sack in lines:
    first, second = sack[:len(sack)//2], sack[len(sack)//2:]
    (common, ) = set(list(first)).intersection(set(list(second)))
    if 65 <= ord(common) <= 90:
        val = ord(common) - 38
    else:
        val = ord(common) - 96
    total += val
print(total)

# Part 2
total = 0
for i in range(0,len(lines),3):
    elf1, elf2, elf3 = set(list(lines[i])), set(list(lines[i+1])), set(list(lines[i+2]))
    (common,) = elf1 & elf2 & elf3
    if 65 <= ord(common) <= 90:
        val = ord(common) - 38
    else:
        val = ord(common) - 96
    total += val

print(total)
