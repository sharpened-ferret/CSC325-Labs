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

class BoardState:
    empty_marker = -1    

    def __init__(self, parent, board):
        self.board = board
        self.parent = parent
        self.empty_pos = self.find_empty()
        # self.children = self.gen_children(self.empty_pos)

    def __str__(self):
        return "parent=[{}], board={}".format(self.parent, self.board)
    
    def __repr__(self):
        return self.__str__()+"\n"

    def find_empty(self):
        board_size = len(self.board)
        empty_pos = None
        for row in range(board_size):
            for col in range(board_size):
                if (self.board[row][col] == self.empty_marker):
                    empty_pos = (row, col)
        return empty_pos
    
    def gen_children(self, empty_pos):
        children = []
        neighbours = [
            (empty_pos[0], empty_pos[1]+1),
            (empty_pos[0], empty_pos[1]-1),
            (empty_pos[0]+1, empty_pos[1]),
            (empty_pos[0]-1, empty_pos[1])
        ]
        for neighbour in neighbours:
            try:
                board = [row[:] for row in self.board]
                pos_val = board[neighbour[0]][neighbour[1]]
                board[empty_pos[0]][empty_pos[1]] = pos_val
                board[neighbour[0]][neighbour[1]] = self.empty_marker
                children.append(BoardState(self, board))
            except:
                continue
        print(children)



test_puzzle = [[1,8,2], [-1, 4, 3], [7,6,5]]
test_board = generate_board(3)
print(test_board)
base_node = BoardState(None, test_board)
base_node.gen_children(base_node.empty_pos)
# print(count_inversion(test_puzzle))