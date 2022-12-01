import ast
lines = []
with open('test2.txt') as f:
    for line in f:
        line = ast.literal_eval(line.strip())
        lines.append(line)
f.close()

def depth(lst):
    if type(lst) == list:
        return 1 + max(depth(x) for x in lst)
    return 0

def find_explode(lst, curr_depth, pos):
    if curr_depth >= 5 and type(lst[0]) == int and type(lst[1]) == int:
        return pos

    for i in range(len(lst)):
        if depth(lst[i])+curr_depth >= 5 and depth(lst[i]) != 0:
            pos.append(i)
            return find_explode(lst[i], curr_depth+1, pos)
    
def find_explode_left_right(original, pos):
    # In the same level, there exist either left or right
    # Find Left
    if pos[-1] == 1:
        left = pos[:-1]
        left.append(0)

        temp = final[::]
        for i in left:
            temp = temp[i]

        if type(temp) == list:
            left.append(1)

        direction = False
    # Find Right
    else:
        right = pos[:-1]
        right.append(1)

        temp = final[::]
        for i in right:
            temp = temp[i]

        while type(temp) == list:
            temp = temp[0]
            right.append(0)
            
        direction = True

    temp = pos[:-1]
    if direction: # Find Left in different level if exist
        # Check whether is there any left
        while temp:
            last_pos = temp.pop()
            if last_pos != 0:
                # Copy original
                temp1 = original[::]
                # Get to current index using temp
                for i in temp:
                    temp1 = temp1[i]
                moves = temp[::]
                moves.append(last_pos-1)
                temp1 = temp1[last_pos-1]
                if type(temp1) != int:
                    while True:
                        moves.append(len(temp1)-1)
                        temp1 = temp1[len(temp1)-1]
                        if type(temp1) == int:
                            break
                left = moves
                    
                return left, right

        # Not found yet
        start = pos[0]
        left = None
        i = start-1
        while i >= 0:
            temp1 = original[i]
            moves = [i]

            while True:
                temp1 = temp1[len(temp1)-1]
                moves.append(len(temp1)-1)
                if type(temp1) == int:
                    found = True
                    break
                
            if found:
                left = moves
                break
        
    else: # Find Right in different level if exist
        while temp:
            last_pos = temp.pop()
            
            # Copy original
            temp1 = original[::]
            # Get to current index using temp
            for i in temp:
                temp1 = temp1[i]
            # Check whether is there any right
            curr_len = len(temp1)
            
            if last_pos+1 < curr_len:
                moves = temp
                moves.append(last_pos+1)
                temp1 = temp1[last_pos+1]
                if type(temp1) != int:
                    while True:
                        temp1 = temp1[0]
                        moves.append(0)
                        if type(temp1) == int:
                            break
                right = moves
                return left, right
        
        # Not found yet
        start = pos[0]
        right = None
        for i in range(start+1, len(original)):
            temp1 = original[i]
            moves = [i]

            while True:
                temp1 = temp1[0]
                moves.append(0)
                if type(temp1) == int:
                    found = True
                    break

            if found:
                right = moves
                break

    return left, right

def get_explode_left_right(exploding_lst, left, right):
    exploding_pair = final[::]
    for i in exploding_lst:
        exploding_pair = exploding_pair[i]
    
    if left is not None and right is not None:
        left_val = final[::]
        for i in left:
            left_val = left_val[i]

        right_val = final[::]
        for i in right:
            right_val = right_val[i]

        left_val += exploding_pair[0]
        right_val += exploding_pair[1]
        return left_val, right_val
    
    elif left is None:
        right_val = final[::]
        for i in right:
            right_val = right_val[i]

        right_val += exploding_pair[1]
        return None, right_val
    
    else:
        left_val = final[::]
        for i in left:
            left_val = left_val[i]
        left_val += exploding_pair[0]
        return left_val, None

def find_split(lst):
    # Set up Queue
    queue = []
    for i in range(len(lst)):
        queue.append([i])

    while queue:
        temp = lst[::]
        idx = queue.pop(0)
        for i in idx:
            temp = temp[i]
        if type(temp) == list:
            for i in range(len(temp)):
                x = idx + [i]
                queue.append(x)
        else:
            if temp >= 10:
                new_val = [temp//2, temp - temp//2]
                return (idx, new_val)
    return None

def magnitude(lst):
    if type(lst) == int:
        return lst
    else:
        return magnitude(lst[0])*3 + magnitude(lst[1])*2

final = [lines.pop(0)]
while lines:
    # Add next line
    next_val = lines.pop(0)
    final.append(next_val)

    while True:
        # Find position of exploding list
        exploding_lst = find_explode(final, 1, [])

        if exploding_lst != None:
            # Get left and right regular numbers
            left, right = find_explode_left_right(final, exploding_lst)

            # Get left and right updated values
            left_val, right_val = get_explode_left_right(exploding_lst, left, right)

            # Update Left Value, Right Value and exploding pair
            if left_val is not None:
                x = final
                while left:
                    pos = left.pop(0)
                    x = x[pos]
                    if len(left) == 1:
                        x[left[0]] = left_val
                        break
            
            if right_val is not None:
                x = final
                while right:
                    pos = right.pop(0)
                    x = x[pos]
                    if len(right) == 1:
                        x[right[0]] = right_val
                        break
            x = final
            while exploding_lst:
                pos = exploding_lst.pop(0)
                x = x[pos]
                if len(exploding_lst) == 1:
                    x[exploding_lst[0]] = 0
                    break

        # Find position of split list
        split_lst = find_split(final)
        if split_lst != None:
                pos, val = split_lst
                temp = final[::]
                while pos:
                    x = pos.pop(0)
                    temp = temp[x]
                    if len(pos) == 1:
                        temp[pos[0]] = val
                        break
   
        if exploding_lst == None and split_lst == None:
            break

print(final)
print(magnitude(final))




    



    
