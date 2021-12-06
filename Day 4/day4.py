lines = []
with open('puzzle.txt') as f:
    for line in f:
        lines.append(line.strip())

f.close()

order, lines = list(map(lambda x: int(x), lines[0].split(','))), lines[2:]
lines = list(filter(lambda x: x != '', lines))
boards = []
for i in range(0,len(lines),5):
    temp = lines[i:i+5]

    board = []
    for j in temp:
        temp2 = j.split(' ')
        temp2 = list(map(lambda x: int(x), filter(lambda x: x!= '', temp2)))
        board.append(temp2)
    boards.append(board)

# Helper
def create_checker_board():
    b = []
    for i in range(5):
        temp = []
        for j in range(5):
            temp.append(False)
        b.append(temp)
    return b

def check_num(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return (i,j)
    return False

def check_win(board):
    # Check rows
    for row in board:
        if row == [True, True, True, True, True]:
            return True
    # Check columns by tranposing matrix
    t_board = list(zip(*board))
    t_board = list(map(lambda x: list(x), t_board))
    for row in t_board:
        if row == [True, True, True, True, True]:
            return True
    return False

def calculate_unmarked(check_board, board):
    pos = []
    for i in range(5):
        for j in range(5):
            if check_board[i][j] == False:
                pos.append((i,j))

    total = 0
    for i,j in pos:
        total += board[i][j]

    return total

# Part 1
def part_1(order, boards):
    checker = {}

    # Create Boolean Checker Board
    for i in range(len(boards)):
        checker[i] = create_checker_board()

    for num in order: # Iterate through every number in order
        for b_num in range(len(boards)): # Check number in every board
            board = boards[b_num]
            pos = check_num(board,num) # Find number in current board
            if pos != False: # Number is present
                checker[b_num][pos[0]][pos[1]] = True
                win = check_win(checker[b_num]) # Check if won
                if win:
                    score = calculate_unmarked(checker[b_num], board) * num
                    return score
                
print(part_1(order, boards))

# Part 2   
def part_2(order, boards):
    checker = {}

    # Create Boolean Checker Board
    for i in range(len(boards)):
        checker[i] = create_checker_board()

    last = False
    for num in order: # Iterate through every number in order
        for b_num in range(len(boards)): # Check number in every board
            # Check if board is still valid
            if b_num in checker:
                board = boards[b_num]
                pos = check_num(board,num) # Find number in current board
                if pos != False: # Number is present
                    checker[b_num][pos[0]][pos[1]] = True
                    win = check_win(checker[b_num]) # Check if won
                    if win:
                        if last:
                            score = calculate_unmarked(v, board) * num
                            return score
                        else:
                            del checker[b_num]
                            if len(checker) == 1:
                                k,v = list(checker.items())[0]
                                last = True

print(part_2(order, boards))

    
    
