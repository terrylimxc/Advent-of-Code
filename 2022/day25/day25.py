lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        lines.append(line.strip())
f.close()

# Part 1
def snafu_to_decimal(line):
    # Reverse the string
    line = line[::-1]
    ans = 0
    for i,v in enumerate(line):
        if v == "-":
            v = -1
        elif v == "=":
            v = -2
        else:
            v = int(v)
        ans += v * (5**(i))
    return ans

def decimal_to_snafu(val):
    ans = ""
    while val > 0:
        r = val%5
        if r == 4:
            ans += "-"
            val += 1
        elif r == 3:
            ans += "="
            val += 2           
        else:
            ans += str(r)
        val //= 5
    return ans[::-1]
    
val = 0
for line in lines:
    val += snafu_to_decimal(line)

print(decimal_to_snafu(val))

