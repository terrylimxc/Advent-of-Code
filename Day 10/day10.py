from statistics import median

lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())

f.close()

# Part 1
# Stack
def push(x,y):
    x.append(y)

def pop(x):
    return x.pop()

def peek(x):
    return x[-1]

SCORE  = {')': 3, ']': 57, '}': 1197, '>': 25137}
points = 0
for line in lines:
    stack = []
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            push(stack, char)
        else:
            if peek(stack) == '(' and char == ')':
                pop(stack)
            elif peek(stack) == '[' and char == ']':
                pop(stack)
            elif peek(stack) == '{' and char == '}':
                pop(stack)
            elif peek(stack) == '<' and char == '>':
                pop(stack)
            else:
                points += SCORE[char]
                break
print(points)

# Part 2
# Stack
SCORE  = {'(': 1, '[': 2, '{': 3, '<': 4}
points = []
for line in lines:
    stack = []
    flag = True
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            push(stack, char)
        else:
            if peek(stack) == '(' and char == ')':
                pop(stack)
            elif peek(stack) == '[' and char == ']':
                pop(stack)
            elif peek(stack) == '{' and char == '}':
                pop(stack)
            elif peek(stack) == '<' and char == '>':
                pop(stack)
            else:
                flag = False
                break
    if flag and stack:
        temp = 0
        for char in stack[::-1]:
            temp *= 5
            temp += SCORE[char]
        points.append(temp)
        
print(int(median(points)))
