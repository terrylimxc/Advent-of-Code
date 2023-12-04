with open("puzzle.txt") as f:
    lines = f.read().splitlines()
f.close()

## Part 1
def process_lines(lines):
    main = []
    for line in lines:
        line = line.split(": ")[1]
        nums, ans = line.split(" | ")
        nums = list(map(lambda x: int(x), list(filter(lambda x: x!="", nums.split(" ")))))
        ans = list(map(lambda x: int(x), list(filter(lambda x: x!="", ans.split(" ")))))

        count = len(set(nums).intersection(ans))
        main.append(count)
    
    return main

def calculate_points(count):
    return count if count in [0, 1, 2] else 2**(count-1)
    
counts = process_lines(lines)
ans = sum(map(lambda x: calculate_points(x), counts))
print(ans)

## Part 2
main = {i:1 for i in range(len(counts))}
ans = 0
for i,v in enumerate(counts):
    ans += main[i]

    if v != 0:
        for x in range(i+1, i+v+1):
            main[x] += main[i]

print(ans)