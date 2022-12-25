from sympy import Symbol, sympify, solve, Eq
from copy import deepcopy

lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())
f.close()

# Part 1
num = {}
expr = {}
for line in lines:
    name, x = line.split(": ")
    if name == "root": # Separate root
        root = x
    elif "+" in x or "-" in x or "*" in x or "/" in x:
        expr[name] = x
    else:
        num[name] = x

main = list(expr.items())
temp = []
while main:
    name, expr = main.pop()
    a, sign, b = expr.split(" ")
    if a in num and b in num: # Both exists -> Evaluate
        new_val = eval(num[a]+sign+num[b])
        if type(new_val) == float:
            new_val = int(new_val)
        num[name] = str(new_val)
    elif (a in num) or (b in num): # Only 1 exist
        temp.insert(0, [name, expr])
    else: # Both don't exist yet
        temp.append([name, expr])
    
    if len(main) == 0:
        main.extend(temp)
        temp = []

final = root.split(" ")
print(int(eval(num[final[0]] + final[1] + num[final[2]])))

# Part 2
num = {}
expr = {}
for line in lines:
    name, x = line.split(": ")
    if name == "root": # Separate root
        root = x
    elif name == "humn":
        continue
    elif "+" in x or "-" in x or "*" in x or "/" in x:
        expr[name] = x
    else:
        num[name] = x

main = list(expr.items())
temp = []
counter = 0
while main:
    name, expr = main.pop()
    a, sign, b = expr.split(" ")
    if a in num and b in num: # Both exists -> Evaluate
        new_val = eval(num[a]+sign+num[b])
        if type(new_val) == float:
            new_val = int(new_val)
        num[name] = str(new_val)
    elif a in num: # Only 1 exist
        expr = expr.replace(a, num[a])
        temp.insert(0, [name, expr])
    elif b in num:
        expr = expr.replace(b, num[b])
        temp.insert(0, [name, expr])
    else: # Both don't exist yet
        temp.append([name, expr])
    
    if len(main) == 0:
        if counter == len(temp):
            break
        main.extend(temp)
        temp = []
        counter = 0
    counter += 1

def prepare_root(root, num):
    a,_,b = root.split(" ")
    if a in num:
        a = num[a]
    if b in num:
        b = num[b]
    return a, b

def recursively_add_root(root, eqns):
    temp = []
    root = sympify(root)
    counter = 0
    while eqns:
        name, expr = eqns.pop()
        new = root.subs(Symbol(name), "("+expr+")")
        if root == new: # Nothing subbed
            temp.append([name,expr])
        else:
            root = new
            root = sympify(root)
        if len(eqns) == 0:
            if counter == len(temp):
                break
            eqns.extend(temp)
            temp = []
            counter = 0
        counter += 1
    return root

root, target = prepare_root(root, num)
temp2 = deepcopy(temp)
root = recursively_add_root(root, temp)
target = recursively_add_root(target, temp2)
print(root) # 43962603717448 - 33*humn/4
print(target) # 19157252549620
# Ans: 
# 43962603717448 - 33*humn/4 = 19157252549620
# 33*humn/4 = 24805351167828
# humn = 3006709232464