with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

def find_marker(num):
    for line in lines:
        marker, line = line[:num], line[num:]
        counter = num
        while len(marker) != len(set(marker)):
            marker = marker[1:] + line[0]
            line = line[1:]
            counter += 1
        print(counter)


# Part 1
find_marker(4)

# Part 2
find_marker(14)