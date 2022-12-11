import numpy as np

lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line)
f.close()

lines = list(map(lambda x: x.strip(), lines))
lines = list(filter(lambda x: x != "", lines))

def setup(lines):
    monkeys = {}
    for i in range(0,len(lines),6):
        num = int(lines[i].split(" ")[-1][:-1])

        st_items = (lines[i+1].split(": ")[-1]).split(", ")
        st_items = list(map(lambda x: int(x), st_items))

        op = lines[i+2].split("= ")[-1]

        test = int(lines[i+3].split(" ")[-1])

        true = int(lines[i+4].split(" ")[-1])

        false = int(lines[i+5].split(" ")[-1])

        monkeys[num] = {"items": st_items, "op": op, "test": test, "true": true, "false": false}

    counts = {}
    for k in sorted(list(monkeys.keys())):
        counts[k] = 0
    return monkeys, counts


# Part 1
monkeys, counts = setup(lines)
rd = 0
while rd != 20:
    for k in sorted(list(monkeys.keys())):
        item, op, test, true, false = monkeys[k]["items"], monkeys[k]["op"], monkeys[k]["test"], monkeys[k]["true"], monkeys[k]["false"]
        counts[k] += len(item)
        for old in item:
            new = eval(op)
            new //= 3
            if new%test==0:
                monkeys[true]["items"].append(new)
            else:
                monkeys[false]["items"].append(new)
        monkeys[k]["items"] = []
    rd += 1

highest2 = sorted(list(counts.values()), reverse=True)[:2]
print(highest2[0]* highest2[1])

# Part 2
monkeys, counts = setup(lines)
rd = 0
superModuolo = np.prod([val.get('test') for val in monkeys.values()]) # Chinese Remainder Theorem
while rd != 10000:
    for k in sorted(list(monkeys.keys())):
        item, op, test, true, false = monkeys[k]["items"], monkeys[k]["op"], monkeys[k]["test"], monkeys[k]["true"], monkeys[k]["false"]
        counts[k] += len(item)

        op = op.replace("old", "{}")
        old_count = op.count("{}")
        if old_count == 1:
            val = list(map(lambda x: eval(op.format(x))%superModuolo, item))
        else:
            val = list(map(lambda x: eval(op.format(x, x))%superModuolo, item))

        temp = list(filter(lambda x: x%test==0, val))
        temp2 = list(filter(lambda x: x%test!=0, val))

        monkeys[true]["items"].extend(temp)
        monkeys[false]["items"].extend(temp2)

        monkeys[k]["items"] = []

    rd += 1

highest2 = sorted(list(counts.values()), reverse=True)[:2]
print(highest2[0]* highest2[1])