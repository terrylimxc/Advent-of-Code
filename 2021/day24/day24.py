lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip().split(" "))
        
f.close()

### 14 unknowns
##X = IntVector('x', 14)
##
### Constraints
##constraints = []
##
### Add integer constraints
##for i in range(14):
##    constraints.append(0 < X[i])
##    constraints.append(X[i] < 10)
##
##
##def eval_line(line):
##    w = 0, x = 0, y = 0, z = 0
##    if len(line) == 2:
##        op, val = line
##    else:

def op(ins,a,b):
    a,b = eval(a), eval(b)
    if ins == "add":
        return a+b
    elif ins == "mul":
        return a*b
    elif ins == "div":
        return a//b
    elif ins == "mod":
        return a%b
    else:
        return int(a == b)


inp = "99999999999999"
w = 0
x = 0
y = 0
z = 0
counter = 0

for line in lines:
    ins, *val = line
    if ins == "inp":
        print(f"Input {counter+1}: w={w}, x={x}, y={y}, z={z}")
        w = int(inp[counter])
        counter += 1
    else:
        new = op(ins,val[0], val[1])
        if val[0] == "w":
            w = new
        elif val[0] == "x":
            x = new
        elif val[0] == "y":
            y = new
        else:
            z = new
    #print(line)
    print(f"Iteration {counter}: w={w}, x={x}, y={y}, z={z}")

        
    

