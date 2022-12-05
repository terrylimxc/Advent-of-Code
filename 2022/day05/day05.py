diagram, moves = [], []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = list(map(lambda x: x.strip(), line.split(" ")))

        if line==[""]:
            continue
        elif "move" in line:
            moves.append((int(line[1]), int(line[3]), int(line[5]))) 
        elif line[1] == "1":
            continue           
        else:
            # Clean spacing
            new_line = []
            i = 0
            while i < len(line):
                if line[i]:
                    new_line.append(line[i][1])
                    i += 1
                else:
                    new_line.append(" ")
                    i += 4
            diagram.append(new_line)
f.close()
diagram = list(zip(*diagram))
for i in range(len(diagram)):
    temp = []
    for j in diagram[i]:
        if j != " ":
            temp.append(j)
    diagram[i] = temp[::-1]

def execute(diagram, moves, flag):
    for num, src, dst in moves:
        if flag:
            transfer = (diagram[src-1][-num:])[::-1]
        else:
            transfer = (diagram[src-1][-num:])
        diagram[src-1] = diagram[src-1][:-num]
        diagram[dst-1] = diagram[dst-1] + transfer
    return diagram

# Part 1
diagram = execute(diagram, moves, True)
final = "".join(list(map(lambda x: x[-1], diagram)))
print(final)

# Part 2
diagram, moves = [], []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = list(map(lambda x: x.strip(), line.split(" ")))

        if line==[""]:
            continue
        elif "move" in line:
            moves.append((int(line[1]), int(line[3]), int(line[5]))) 
        elif line[1] == "1":
            continue           
        else:
            # Clean spacing
            new_line = []
            i = 0
            while i < len(line):
                if line[i]:
                    new_line.append(line[i][1])
                    i += 1
                else:
                    new_line.append(" ")
                    i += 4
            diagram.append(new_line)
f.close()
diagram = list(zip(*diagram))
for i in range(len(diagram)):
    temp = []
    for j in diagram[i]:
        if j != " ":
            temp.append(j)
    diagram[i] = temp[::-1]
diagram = execute(diagram, moves, False)
final = "".join(list(map(lambda x: x[-1], diagram)))
print(final)