pos = []
with open('puzzle.txt') as f:
    for line in f:
        line = line.strip()
        line = int(line.split(": ")[1])
        pos.append(line)
        
f.close()

p1_pos, p2_pos = pos
p1_score, p2_score = 0,0

# Part 1
def move(counter, pos):
    roll = 3*(counter+1)
    pos += roll
    while pos > 10:
        pos -= 10
    return pos
    
counter = 1
flag = None
while True:
    # P1
    p1_pos = move(counter, p1_pos)
    p1_score += p1_pos
    counter += 3
    if p1_score >= 1000:
        flag = True
        break

    # P2
    p2_pos = move(counter, p2_pos)
    p2_score += p2_pos
    counter += 3
    if p2_score >= 1000:
        flag = False
        break

print(p1_score)
print(p2_score)

if flag:
    ans = p2_score * (counter-1)
else:
    ans = p1_score * (counter-1)

print(ans)


# Part 2
from collections import Counter
from functools import lru_cache

# Credits to Reddit for introducing the idea of caching to speed up code

@lru_cache(maxsize=None)
def game(p1_pos, p2_pos, p1_score, p2_score):
    if p1_score >= 21:
        return (1,0)
    if p2_score >= 21:
        return (0,1)
    
    win = [0,0]
    for roll, freq in rolls.items():
        new_p1_pos = p1_pos + roll
        while new_p1_pos > 10:
            new_p1_pos -= 10
        new_p1_score = p1_score + new_p1_pos

        p2_win, p1_win = game(p2_pos, new_p1_pos, p2_score, new_p1_score)

        win[0] += p1_win * freq
        win[1] += p2_win * freq
        
    return win

p1_pos, p2_pos = pos
p1_score, p2_score = 0,0
# Roll dice three times => 27 universe created
rolls = Counter([3,4,5,4,5,6,5,6,7,4,5,6,5,6,7,6,7,8,5,6,7,6,7,8,7,8,9])
print(game(p1_pos, p2_pos, p1_score, p2_score))
