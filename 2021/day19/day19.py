import ast
lines = []
with open('test.txt') as f:
    x = []
    for line in f:
        line = line.strip()
        if ' ' in line:
            continue
        if line != '':
            x.append(ast.literal_eval(line))
        else:
            lines.append(x)
            x = []
        
        
f.close()

print(lines)


    
