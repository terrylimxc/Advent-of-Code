lines = []
with open('puzzle.txt') as f:
    packet = []
    while True:
        line = f.readline()
        if not line:
            break
        if line == "\n":
            lines.append(packet)
            packet = []
        else:
            packet.append(eval(line))
f.close()
lines.append(packet)

# Part 1
def compare(l1,l2):
    if type(l1) == int and type(l2) == int:
        return l1 < l2
    else:
        if type(l1) == int and type(l2) == list:
            l1 = [l1]
        elif type(l1) == list and type(l2) == int:
            l2 = [l2]
    
        for i in range(len(l2)):
            try: # len(l1) < len(l2)
                l1[i]
            except IndexError:
                return True
            if type(l1[i]) == int and type(l2[i]) == int: # Both int
                if l1[i] < l2[i]:
                    return True
                elif l1[i] > l2[i]:
                    return False
            elif type(l1[i] == list) and type(l2[i]) == list: # Both list
                x = compare(l1[i], l2[i])
                if x == False:
                    return False
            elif type(l1[i]) == int and type(l2[i]) == list: # Left is int, Right is list
                x = compare([l1[i]], l2[i])
                if x == False:
                    return False
            elif type(l1[i]) == list and type(l2[i]) == int: # Left is list, Right is int
                x = compare(l1[i], [l2[i]])
                if x == False:
                    return False          

        if len(l2) < len(l1):
            return False  
    return True

def compare(l1,l2):
    if type(l1) == int and type(l2) == int:
        if l1 < l2:
            return 1
        elif l1 == l2:
            return 0
        else:
            return -1

    l1 = [l1] if type(l1) == int else l1
    l2 = [l2] if type(l2) == int else l2

    i = 0
    while i < len(l1) and i < len(l2):
        x = compare(l1[i],l2[i])
        if x == -1:
            return -1
        elif x == 1:
            return 1
        i += 1
    if i == len(l1) and i < len(l2): # len(l1) < len(l2)
        return 1
    elif i == len(l2) and i < len(l1): # len(l2) < len(l1)
        return -1
    else:
        return 0

counter = []
for i, v in enumerate(lines):
    left, right = v
    if compare(left, right)==1:
        counter.append(i+1)

print(sum(counter))

# Part 2
from functools import cmp_to_key
lines = [item for sublist in lines for item in sublist]
lines.append([[2]])
lines.append([[6]])
lines.sort(key=cmp_to_key(compare), reverse=True)
a, b = lines.index([[2]])+1, lines.index([[6]])+1
print(a*b)
