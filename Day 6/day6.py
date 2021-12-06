lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())

f.close()
lines = lines[0]
lines = lines.split(",")
lines = list(map(lambda x: int(x), lines))

### Part 1 & 2 (Naive attempt)
### Fails for Part 2 due to increasing memory used
##NUM_DAYS = 80
##for i in range(NUM_DAYS):
##    temp = []
##    for j in range(len(lines)):
##        lines[j] -= 1
##        if lines[j] < 0:
##            lines[j] = 6
##            temp.append(8)
##    lines.extend(temp)
##
##
##print(len(lines))

# Part 1 & 2 (Optimised attempt)
# Restrict to a single list of 8 items
main = []
for i in range(9):
    main.append(0)

for i in lines:
    main[i] += 1

NUM_DAYS = 256
flag = False
for i in range(NUM_DAYS):
    temp = 0
    for j in range(len(main)-1):
        if j == 0 and main[j] > 0:
            temp = main[j]
        main[j] = main[j+1]

    main[8] = 0

    if temp != 0:
        main[8] += temp
        main[6] += temp
    
print(sum(main))
    
    
