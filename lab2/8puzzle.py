from random import randint
import time

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
    goal_dict = {
        1 : (0, 0),
        2 : (0, 1),
        3 : (0, 2),
        4 : (1, 0),
        5 : (1, 1),
        6 : (1, 2),
        7 : (2, 0),
        8 : (2, 1),
        -1 : (2, 2),
    }
    empty_marker = -1    

    def __init__(self, parent, board):
        self.board = board
        self.parent = parent
        self.empty_pos = self.find_empty()
        self.g = None
        self.h = None
        self.f = None

    def __str__(self):
        return "parent=[{}], board={}".format(self.parent, self.board)
    
    def __repr__(self):
        return self.__str__()+"\n"

    def __eq__(self, other):
        return self.board == other.board

    def find_empty(self):
        board_size = len(self.board)
        empty_pos = None
        for row in range(board_size):
            for col in range(board_size):
                if (self.board[row][col] == self.empty_marker):
                    empty_pos = (row, col)
        return empty_pos
    
    def gen_children(self):
        children = []
        neighbours = [
            (self.empty_pos[0], self.empty_pos[1]+1),
            (self.empty_pos[0], self.empty_pos[1]-1),
            (self.empty_pos[0]+1, self.empty_pos[1]),
            (self.empty_pos[0]-1, self.empty_pos[1])
        ]
        for neighbour in neighbours:
            try:
                board = [row[:] for row in self.board]
                pos_val = board[neighbour[0]][neighbour[1]]
                board[self.empty_pos[0]][self.empty_pos[1]] = pos_val
                board[neighbour[0]][neighbour[1]] = self.empty_marker
                children.append(BoardState(self, board))
            except:
                continue
        self.children = children

    def manhattan_cost(self):
        cost = 0
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                tile_val = self.board[y][x]
                goal_pos = self.goal_dict.get(tile_val)
                cost += abs(y - goal_pos[0]) + abs(x - goal_pos[1])

        return cost


def a_star(board):
    start_state = BoardState(None, board)
    start_state.g = 0
    start_state.h = 0
    start_state.f = 0
    end_state = BoardState(None, [[1,2,3], [4,5,6], [7,8,-1]])
    end_state.g = 0
    end_state.h = 0
    end_state.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_state)

    # While there are still unexplored nodes
    while(len(open_list) > 0):
        current_state = open_list[0]
        current_index = 0
        for index, state in enumerate(open_list):
            if state.f < current_state.f:
                current_state = state
                current_index = index

        # print(current_state.board)
        
        open_list.pop(current_index)
        closed_list.append(current_state)

        if current_state == end_state:
            path = []
            current = current_state
            while current is not None:
                path.append(current.board)
                current = current.parent
            return path[::-1]
        
        current_state.gen_children()
        for child in current_state.children:
            new_state = True
            for closed_state in closed_list:
                if child == closed_state:
                    new_state = False
                    continue
            child.g = current_state.g + 1
            child.h = child.manhattan_cost()
            child.f = child.g + child.h
            
            for open_state in open_list:
                if child == open_state and child.g > open_state.g:
                    new_state = False
                    continue
            if new_state:
                open_list.append(child)

def greedy(board):
    start_state = BoardState(None, board)
    start_state.h = 0
    end_state = BoardState(None, [[1,2,3], [4,5,6], [7,8,-1]])
    end_state.h = 0

    open_list = []
    closed_list = []

    open_list.append(start_state)

    # While there are still unexplored nodes
    while(len(open_list) > 0):
        current_state = open_list[0]
        current_index = 0

        # print(str(current_state.board))
        open_list.remove(current_state)
        closed_list.append(current_state)

        if current_state == end_state:
            path = []
            current = current_state
            while current is not None:
                path.append(current.board)
                current = current.parent
            return path[::-1]
        
        current_state.gen_children()
        for child in current_state.children:
            new_state = True

            for closed_state in closed_list:
                if child == closed_state:
                    new_state = False
                    break
            child.h = child.manhattan_cost()
            
            for open_state in open_list:
                if child == open_state:
                    new_state = False
                    break
            if new_state:
                open_list.append(child)
        open_list.sort(key=heuristic_sort)

def heuristic_sort(e):
    return e.h





def main():
    test_puzzle = [[1,8,2], [-1, 4, 3], [7,6,5]]
    test_board = generate_board(3)
    print(test_board)
    base_node = BoardState(None, test_puzzle)
    print(base_node.manhattan_cost())

    print("\nA*:\n")
    a_start = time.time()
    path = a_star(test_board)
    a_end = time.time()
    for board in path:
        for row in board:
            print(row)
        print("\n")


    print("\nGreedy:\n")
    g_start = time.time()
    greedy_path = greedy(test_board)
    g_end = time.time()
    for board in greedy_path:
        for row in board:
            print(row)
        print("\n")

    print("\nA* Run Details:\nMove Number: {}, Runtime: {}".format(len(path), (a_end - a_start)))
    print("\nGreedy Run Details:\nMove Number: {}, Runtime: {}".format(len(greedy_path), (g_end - g_start)))


    print("\n---Average Runs---")
    NUM_LOOPS = 10
    a_star_total = 0
    greedy_total = 0
    for i in range(NUM_LOOPS):
        curr_board = generate_board(3)
        time1 = time.time()
        a_star(curr_board)
        time2 = time.time()
        greedy(curr_board)
        time3 = time.time()
        a_star_total += time2 - time1
        greedy_total += time3 - time2
    print("A* Avg. Time: {}\nGreedy Avg. Time: {}".format((a_star_total/NUM_LOOPS), (greedy_total/NUM_LOOPS)))

    # print(count_inversion(test_puzzle))

main()