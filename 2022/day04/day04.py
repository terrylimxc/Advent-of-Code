with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

lines = list(map(lambda x: x.split(","), lines))

def convert_to_range(string):
    temp = list(map(lambda x: int(x), string.split("-")))
    return list(range(temp[0], temp[1]+1))

# Part 1
counter = 0
for i in lines:
    first, second = i
    first, second = convert_to_range(first), convert_to_range(second)
    diff_1, diff_2 = set(first)-set(second), set(second)-set(first)
    if len(diff_1) == 0 or len(diff_2) == 0:
        counter += 1
print(counter)

# Part 2
counter = 0
for i in lines:
    first, second = i
    first, second = convert_to_range(first), convert_to_range(second)
    if set(first).intersection(second):
        counter += 1
print(counter)