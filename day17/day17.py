with open('puzzle.txt') as f:
    inpt = f.read().strip()
f.close()

def process(inpt):
    inpt = inpt.split(": ")[1]
    x_rng, y_rng = inpt.split(", ")
    
    x_rng = x_rng.split('=')[1]
    x_rng = list(map(lambda x: int(x), x_rng.split("..")))

    y_rng = y_rng.split('=')[1]
    y_rng = list(map(lambda x: int(x), y_rng.split("..")))

    return x_rng, y_rng

x_rng, y_rng = process(inpt)

# Part 1
# When probe reaches back to y=0, it needs to reach exactly at lowest bound of target area box to maximise height
# From example, lowest point is -10.
# Thus, vy = 9
# Max height = 9(9+1)/2 = 45
ans = y_rng[0] * (y_rng[0]+1) // 2
print(ans)

# Part 2
def test(x,y,x_rng,y_rng):
    pos_x, pos_y = 0, 0
    x_rng = list(range(x_rng[0], x_rng[1]+1))
    y_rng = list(range(y_rng[0], y_rng[1]+1))
        
    while pos_y > y_rng[0]:
        pos_x += x
        pos_y += y
            
        if x > 0:
            x -= 1
        y -= 1

        # Found a valid solution
        if pos_x in x_rng and pos_y in y_rng:
            return True

    return False

counter = 0
for i in range(1, x_rng[-1]+1):
    for j in range(y_rng[0], -y_rng[0]):
        guess = test(i,j,x_rng,y_rng)
        if guess:
            counter += 1
        
print(counter)
        
        


        
