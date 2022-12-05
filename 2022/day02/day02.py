with open('puzzle.txt') as f:
    lines = f.read().splitlines()
f.close()

lines = list(map(lambda x: x.split(" "), lines))

# Part 1
opp_moves = {"A": 0, "B": 1, "C": 2}
player_moves = {"X": 0, "Y": 1, "Z": 2}
score = 0
for opp, player in lines:
    opp = opp_moves[opp]
    player = player_moves[player]

    if (player-opp) == 0:  # Draw
        temp = (player+1) + 3
    elif ((player-opp) == 1) or ((player-opp) == -2):  # Win
        temp = (player+1) + 6
    else:  # Lose
        temp = (player+1)
    score += temp

print(score)

# Part 2
opp_moves = {"A": 0, "B": 1, "C": 2}
player_moves = {0: {"X": 2, "Y": 0, "Z": 1},
                1: {"X": 0, "Y": 1, "Z": 2},
                2: {"X": 1, "Y": 2, "Z": 0}}
score = 0
for opp, outcome in lines:
    opp = opp_moves[opp]
    player = player_moves[opp][outcome]

    if (player-opp) == 0:  # Draw
        temp = (player+1) + 3
    elif ((player-opp) == 1) or ((player-opp) == -2):  # Win
        temp = (player+1) + 6
    else:  # Lose
        temp = (player+1)
    score += temp

print(score)
