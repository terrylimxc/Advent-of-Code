with open('puzzle.txt') as f:
    lines = f.readlines()

f.close()
lines = list(map(lambda x: x.split("\n")[0], lines))

# Part 1
x,y = 0,0
for line in lines:
    dirc, amt = line.split(" ")
    amt = int(amt)
    if dirc == "up":
        y -= amt
    elif dirc == "down":
        y += amt
    else:
        x += amt

print(x*y)

# Part 2
x,y,aim = 0,0,0
for line in lines:
    dirc, amt = line.split(" ")
    amt = int(amt)
    if dirc == "up":
        aim -= amt
    elif dirc == "down":
        aim += amt
    else:
        x += amt
        y += aim * amt

print(x*y)
    
