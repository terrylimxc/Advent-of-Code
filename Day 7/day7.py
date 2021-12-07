lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())

f.close()
lines = lines[0]
lines = lines.split(",")
lines = list(map(lambda x: int(x), lines))

# Part 1 (Brute-force)
min_pos = min(lines)
max_pos = max(lines)

least_fuel = None

for i in range(min_pos, max_pos+1):
    temp = sum(map(lambda x: abs(x-i), lines))
    if least_fuel == None:
        least_fuel = temp
    if temp < least_fuel:
        least_fuel = temp

print(least_fuel)

# Part 1 (Alternative: Using median)
from statistics import median

med = int(median(lines))
least_fuel = sum(map(lambda x: abs(x-med), lines))
print(least_fuel)


# Part 2 (Brute force)
min_pos = min(lines)
max_pos = max(lines)

least_fuel = None

for i in range(min_pos, max_pos+1):
    temp = list(map(lambda x: abs(x-i), lines))
    temp = sum(map(lambda x: x*(x+1)//2, temp))
    if least_fuel == None:
        least_fuel = temp
    if temp < least_fuel:
        least_fuel = temp

print(least_fuel)
