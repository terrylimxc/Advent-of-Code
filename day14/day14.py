from collections import Counter

def add_letter(x, dic, count):
    if x not in dic:
        dic[x] = 0
    dic[x] += count
    
rules = {}
letter_count = {}
change = False
with open('puzzle.txt') as f:
    for line in f:
        x = line.strip()
        if x == '':
            change = True
            continue
        if change:
            x = x.split(' -> ')
            rules[x[0]] = x[1]
        else:
            inp = x
            for i in inp:
                add_letter(i, letter_count, 1)
            
            template = {}
            for i in range(len(inp)-1):
                a = inp[i:i+2]
                if a not in template:
                    template[a] = 0
                template[a] += 1 
f.close()

def process(template, rules, letter_count):
    new = {}
    to_remove = []
    for k,v in template.items():
        if k in rules:
            # Get new letter
            val = rules[k]
            # Form 2 new pairs
            new_val_1 = k[0]+val
            new_val_2 = val+k[1]

            # Add to new dictionary
            if new_val_1 not in new:
                new[new_val_1] = 0
            if new_val_2 not in new:
                new[new_val_2] = 0
            new[new_val_1] += v
            new[new_val_2] += v

            # Add original to deletion list
            to_remove.append(k)

            # Add letter to letter_count
            add_letter(val, letter_count, v)
            
    # Remove old pairs in deletion list
    for i in to_remove:
        del template[i]
        
    template = template | new

    return template

NUM_STEPS = 40
for _ in range(NUM_STEPS):
    template = process(template, rules, letter_count)


x = Counter(letter_count)
count = x.most_common(len(x))
ans = count[0][1] - count[-1][1]
print(ans)
