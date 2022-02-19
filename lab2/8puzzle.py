from random import randint

# N-puzzles are solvable if the number of inversions (required swaps) is even
# Therefore, to check validity, we must count the number of inversions and check if even or odd

def count_inversion(board):
    temp_board = []
    inversion_count = 0 
    empty_marker = -1

    for row in range(len(board)):
        for col in range(len(board[row])):
            pos = board[row][col]
            if pos != empty_marker:
                temp_board.append(pos)
    for pos1 in range(len(temp_board)):
        for pos2 in range(pos1, len(temp_board)):
            if temp_board[pos1] > temp_board[pos2]:
                inversion_count += 1
    return inversion_count

def is_solvable(board):
    if (count_inversion(board) % 2) == 0:
        return True
    else:
        return False

def generate_board(size):
    solvable = False
    board = [[None for y in range(size)] for x in range(size)]
    while not solvable:
        # Generates a list of all numbers that are needed to fill the board
        # Using -1 to denote the empty position
        numbers = [n for n in range(size*size)]
        numbers[0] = -1

        board = [[None for y in range(size)] for x in range(size)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                assigned = False
                while not assigned:
                    rand_pos = randint(0, (size*size)-1)
                    if numbers[rand_pos] != None:
                        board[row][col] = numbers[rand_pos]
                        numbers[rand_pos] = None
                        assigned = True
        solvable = is_solvable(board)
    return board


test_puzzle = [[1,8,2], [-1, 4, 3], [7,6,5]]
print(generate_board(3))
# print(count_inversion(test_puzzle))