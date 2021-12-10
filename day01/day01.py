with open('puzzle.txt') as f:
    lines = f.readlines()

f.close()
lines = list(map(lambda x: int(x.split("\n")[0]), lines))

def count_increase(x):
    counter = 0

    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            counter += 1
    return counter

# Part 1
print(count_increase(lines))

# Part 2
main = []
for i in range(len(lines)-2):
    main.append(lines[i]+lines[i+1]+lines[i+2])

print(count_increase(main))
