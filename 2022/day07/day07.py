from functools import reduce  # forward compatibility for Python 3
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

# Part 1
main = {}
moves = []
flag = True
i = 0
while i < len(lines):
    command = lines[i].split(" ")
    i += 1
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "/":
                moves = []
            elif command[2] == "..":
                moves.pop()
            else:
                moves.append(command[2])
        else: #ls
            continue
    else: # listing directory
        if moves == []: # At root
            if flag:
                i-=1
                while lines[i].split(" ")[0] != "$":
                    command = lines[i].split(" ")  
                    print(command)
                    if command[0] == "dir":
                        main[command[-1]] = {}
                    else:
                        size, file = command
                        main[file] = int(size) 
                    i += 1
                i -= 1
                flag = False                  
        else:
            temp = getFromDict(main, moves)
            if command[0] == "dir":
                temp[command[-1]] = {}
            else:
                size, file = command
                temp[file] = int(size)            

def get_keys(dictionary):
    result = []
    for key, value in dictionary.items():
        if type(value) is dict:
            new_keys = get_keys(value)
            result.append(key)
            for innerkey in new_keys:
                result.append(f'{key}/{innerkey}')
        else:
            result.append(key)
    return result

aa = get_keys(main)
to_del = []
for i in aa:
    x = i.split("/")
    aaa = getFromDict(main, x)
    if type(aaa) != dict:
        to_del.append(i)
ans = [x for x in aa if x not in to_del]

def search_directory(dic):
    total = 0
    for k,v in dic.items():
        if type(v) != dict:
            total += v
        else:
            temp = search_directory(v)
            total += temp
    return total

final = {}
for i in ans:
    x = i.split("/")
    aaa = getFromDict(main, x)
    val = search_directory(aaa)
    final[tuple(x)] = val
total = search_directory(main)
final["/"] = total

print(sum(list(filter(lambda x: x <= 100000, final.values()))))

# Part 2
space = 30000000 - (70000000 - final["/"])
directories = sorted(list(final.values()))
ans = 70000000
for i in directories:
    if i >= space and i < ans:
        ans = i
print(ans)