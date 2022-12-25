from z3 import *

lines = []
with open('puzzle.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip().split(" costs ")
        _, ore, clay, obsidian, geode = line
        #blueprint = int(blueprint.split(" ")[1].split(":")[0])
        ore, clay = int(ore.split(" ")[0]), int(clay.split(" ")[0])
        obsidian_o, obsidian_c = obsidian.split(" and ")
        obsidian_o, obsidian_c = int(obsidian_o.split(" ")[0]), int(obsidian_c.split(" ")[0])
        geode_ore, geode_obs = geode.split(" and ")
        geode_ore, geode_obs = int(geode_ore.split(" ")[0]), int(geode_obs.split(" ")[0])
        lines.append([ore, clay, obsidian_o, obsidian_c, geode_ore, geode_obs])
f.close()

def solve(blueprint, t):
    ore_o, clay_o, obs_o, obs_c, geo_o, geo_obs = blueprint
    
    ore = [Int(f"ore_{i}") for i in range(t+1)]
    clay = [Int(f"clay_{i}") for i in range(t+1)]
    obs = [Int(f"obs_{i}") for i in range(t+1)]
    geo = [Int(f"geo_{i}") for i in range(t+1)]

    ore_r = [Int(f"ore_r_{i}") for i in range(t+1)]
    clay_r = [Int(f"clay_r_{i}") for i in range(t+1)]
    obs_r = [Int(f"obs_r_{i}") for i in range(t+1)]
    geo_r = [Int(f"geo_r_{i}") for i in range(t+1)]

    buy_ore_r = [Int(f"buy_ore_r_{i}") for i in range(t+1)]
    buy_clay_r = [Int(f"buy_clay_r_{i}") for i in range(t+1)]
    buy_obs_r = [Int(f"buy_obs_r_{i}") for i in range(t+1)]
    buy_geo_r = [Int(f"buy_geo_r_{i}") for i in range(t+1)]

    constraints = []
    constraints.append(ore[0]==0)
    constraints.append(clay[0]==0)
    constraints.append(obs[0]==0)
    constraints.append(geo[0]==0)

    for i in range(1,t+1):
        constraints.append(ore[i]==ore[i-1] + ore_r[i-1] - (buy_ore_r[i-1]*ore_o) - (buy_clay_r[i-1]*clay_o) - (buy_obs_r[i-1]*obs_o) - (buy_geo_r[i-1]*geo_o))

        constraints.append(clay[i]==clay[i-1] + clay_r[i-1] - (buy_obs_r[i-1]*obs_c))
        constraints.append(obs[i]==obs[i-1] + obs_r[i-1] - (buy_geo_r[i-1]*geo_obs))
        constraints.append(geo[i]==geo[i-1] + geo_r[i-1])
    
    for i in range(1,t+1):
        constraints.append(buy_ore_r[i]*ore_o <= ore[i])
        constraints.append(buy_clay_r[i]*clay_o <= ore[i])
        constraints.append(buy_obs_r[i]*obs_o <= ore[i])
        constraints.append(buy_geo_r[i]*geo_o <= ore[i])

        constraints.append(buy_obs_r[i]*obs_c <= clay[i])

        constraints.append(buy_geo_r[i]*geo_obs <= obs[i])

    for i in range(1,t+1):
        constraints.append(ore_r[i] == ore_r[i-1] + buy_ore_r[i-1])
        constraints.append(clay_r[i] == clay_r[i-1] + buy_clay_r[i-1])
        constraints.append(obs_r[i] == obs_r[i-1] + buy_obs_r[i-1])
        constraints.append(geo_r[i] == geo_r[i-1] + buy_geo_r[i-1])

    for i in range(t+1):
        constraints.append(buy_ore_r[i] <= 1)
        constraints.append(buy_clay_r[i] <= 1)
        constraints.append(buy_obs_r[i] <= 1)
        constraints.append(buy_geo_r[i] <= 1)

        constraints.append(ore[i] >= 0)
        constraints.append(clay[i] >= 0)
        constraints.append(obs[i] >= 0)
        constraints.append(geo[i] >= 0)

        constraints.append(ore_r[i] >= 0)
        constraints.append(clay_r[i] >= 0)
        constraints.append(obs_r[i] >= 0)
        constraints.append(geo_r[i] >= 0)

        constraints.append(buy_ore_r[i] >= 0)
        constraints.append(buy_clay_r[i] >= 0)
        constraints.append(buy_obs_r[i] >= 0)
        constraints.append(buy_geo_r[i] >= 0)

        constraints.append(buy_ore_r[i] + buy_clay_r[i] + buy_obs_r[i] + buy_geo_r[i] <= 1)

    # Initial conditions
    constraints.append(ore_r[0] == 1)
    constraints.append(clay_r[0] == 0)
    constraints.append(obs_r[0] == 0)
    constraints.append(geo_r[0] == 0)

    constraints.append(buy_ore_r[0] == 0)
    constraints.append(buy_clay_r[0] == 0)
    constraints.append(buy_obs_r[0] == 0)
    constraints.append(buy_geo_r[0] == 0)

    constraints.append(ore[0] == 0)
    constraints.append(clay[0] == 0)
    constraints.append(obs[0] == 0)
    constraints.append(geo[0] == 0)

    obj = geo[t]

    solver = Optimize()
    solver.add(constraints)
    solver.maximize(obj)
    if solver.check() == sat:
        model = solver.model()
        return model[geo[t]].as_long()

# Part 1
ans = 0
for i,line in enumerate(lines):
    num = solve(line,24)
    ans += num * (i+1)
print(ans)

# Part 2
ans = 1
for line in lines[:3]:
    ans *= solve(line,32)
print(ans)

# Credits: https://topaz.github.io/paste/#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