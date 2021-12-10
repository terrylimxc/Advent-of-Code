from collections import Counter

with open('puzzle.txt') as f:
    lines = f.readlines()

f.close()
lines = list(map(lambda x: x.split("\n")[0], lines))

### Part 1
##gamma = []
##epsilon = []
##x = lines[0]
##for i in range(len(x)):
##    temp = list(map(lambda y: y[i], lines))
##    count = Counter(temp)
##    if count['0'] > count['1']:
##        gamma.append('0')
##        epsilon.append('1')
##    else:
##        gamma.append('1')
##        epsilon.append('0')
##
##gamma = int(''.join(gamma), 2)
##epsilon = int(''.join(epsilon), 2)
##
##print(gamma*epsilon)

# Part 2
def finder(x, pos, flag):
    if len(x) == 1:
        return x
    
    temp = list(map(lambda y: y[pos], x))
    count = Counter(temp)

    if flag: # Finding o2
        if count['0'] > count['1']:
            x = list(filter(lambda a: a[pos] == '0', x))
        else:
            x = list(filter(lambda a: a[pos] == '1', x))
    else:
        if count['0'] > count['1']:
            x = list(filter(lambda a: a[pos] == '1', x))
        else:
            x = list(filter(lambda a: a[pos] == '0', x))

    return finder(x, pos+1, flag)

o2 = int(finder(lines,0,True)[0], 2)
co2 = int(finder(lines,0,False)[0], 2)

print(o2*co2)
    

    
