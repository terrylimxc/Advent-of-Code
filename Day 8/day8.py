lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())

f.close()

inpt = list(map(lambda x: x.split(" | ")[0], lines))
inpt = list(map(lambda x: x.split(" "), inpt))
out = list(map(lambda x: x.split(" | ")[1], lines))
out = list(map(lambda x: x.split(" "), out))

# Part 1
counts = []
for i in out:
    temp = map(lambda x: len(x), i)
    counts.append(len(list(filter(lambda x: x not in (5,6),temp))))

print(sum(counts))

# Part 2
len_map = {2:1, 3:7, 4:4, 7:8}

def process_input(x):
    temp_dict = {}
    for j in x:
        if len(j) not in temp_dict:
            temp_dict[len(j)] = []
        temp_dict[len(j)].append(j)
    return temp_dict

def sort_string(x):
    return ''.join(sorted(x))

def set_diff_single(x,y):
    return next(iter((set(x) - set(y))))

def decode(temp):
    top, top_left, top_right, mid, bot_left, bot_right, bot = None, None, None, None, None, None, None
    num = [None, None, None, None, None, None, None, None, None, None]

    for j in range(len(temp[6])):
        temp[6][j] = sort_string(temp[6][j])

    for j in range(len(temp[5])):
        temp[5][j] = sort_string(temp[5][j])

    num[1] = sort_string(temp[2][0])
    num[4] = sort_string(temp[4][0])
    num[7] = sort_string(temp[3][0])
    num[8] = sort_string(temp[7][0])

    ##(A) Using only 1 and 7: Set difference between 7 and 1 is top
    top = set_diff_single(num[7], num[1])

    ##(B) Using only 1, 4 and 7: Set difference all letters and 1+4+7 is bottom left corner
    bottom_left_corner = sort_string(list(set('abcdefg') - set(num[1]+num[4]+num[7])))
    
    ##(C) Among all the possible 6-letter strings, the string that contains letters from B and 7 is 0
    find = set(bottom_left_corner + num[7])
    for j in temp[6]:
        extra = set(j)-find
        
        if len(extra) == 1:
            temp[6].remove(j)
            num[0] = j
            ##(D) From C, the extra letter that is not in B and 7 combined is top left
            top_left = next(iter(extra))
            break

    ##(E) Using only C: Set difference all letters and C is middle
    middle = sort_string(list(set('abcdefg') - set(num[0])))
    
    ##(F) 6-letter string with letters from A, B, D, E is 6
    find = set(top+bottom_left_corner+top_left+middle)
    for j in temp[6]:
        extra = set(j)-find

        if len(extra) == 1:
            temp[6].remove(j)
            num[6] = j
            ##(G) From F, the extra letter is bottom right
            bottom_right = next(iter(extra))
            break

    ##(H) Using only F: Set difference all letters and F is top right
    top_right = sort_string(list(set('abcdefg') - set(num[6])))
    
    ##(I) Last 6-letter string is 9 ('cefabd')
    num[9] = temp[6][0]
    
    ##(J) Using only A, D, E, G, H: Set difference all letters and A+D+E+G+H is bottom
    bottom = set_diff_single(num[9], top+top_left+middle+bottom_right+top_right)
    
    ##(K) From all deduced letters find bottom left
    bottom_left = sort_string(list(set('abcdefg') - set(top+top_left+top_right+middle+bottom_right+bottom)))
    
    # num2
    num[2] = sort_string(top+top_right+middle+bottom_left+bottom)
    # num3
    num[3] = sort_string(top+top_right+middle+bottom_right+bottom)
    # num5
    num[5] = sort_string(top+top_left+middle+bottom_right+bottom)
    # num9
    num[9] = sort_string(top+top_left+top_right+middle+bottom_right+bottom) 

    return num

final = 0
for i in range(len(inpt)):
    temp = process_input(inpt[i])
    
    num = decode(temp)
    
    out_temp = map(lambda x: sort_string(x), out[i])
    ans = map(lambda x: str(num.index(x)), out_temp)
    final += int(''.join(ans))

print(final)
    
    
    




