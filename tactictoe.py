import random
import copy

game_grid = [[1,2,3],[4,5,6],[7,8,9]]

def possible_moves():
    return {move : (i,j) for i,row in enumerate(game_grid) for j,move in enumerate(row) if isinstance(move, int)}

class TacTicToe:
    def __init__(self, user_marker, system_marker):
        self.user_marker = user_marker
        self.system_marker = system_marker

    def display_board(self):
        print()
        for j,row in enumerate(game_grid):
            for i in range(3):
                print(f" {row[i]} " if i != 1 else f"| {row[i]} |", end = "")
            print("\n---|---|---" if j != 2 else "\n")

    def user_move(self, move):
        i, j = possible_moves()[move]
        game_grid[i][j] = self.user_marker

    def system_move(self):
        if not possible_moves(): return
        if not AdvanceSystemMove(self.user_marker, self.system_marker).make_the_move():
            moves_l = list(possible_moves().values())
            i, j = random.choice(moves_l)
            game_grid[i][j] = self.system_marker

    def check_conditions(self, marker):
        conditions = GameConditions(marker = marker, grid = game_grid)
        return any([conditions.check_rows(), conditions.check_columns(), conditions.check_diagonals()])

class AdvanceSystemMove:
    def __init__(self,user_marker,system_marker):
        self.user_marker = user_marker  
        self.system_marker = system_marker  

    def check_move(self,row,column, marker):
        temp_grid = copy.deepcopy(game_grid)
        temp_grid[row][column] = marker
        conditions = GameConditions(marker = marker, grid = temp_grid)
        return any([conditions.check_rows(), conditions.check_columns(), conditions.check_diagonals()])

    def make_the_move(self):
        wining_move = self.win_or_defend(marker = self.system_marker)
        defending_move = self.win_or_defend(marker = self.user_marker) if not wining_move else False
        if wining_move or defending_move:
            row, col = wining_move or defending_move
            game_grid[row][col] = self.system_marker
            return True
        return False

    def win_or_defend(self, marker):
        for indexes in possible_moves().values():
            if self.check_move(*indexes, marker = marker):
                return indexes
        return False
    
class GameConditions:
    def __init__(self, marker, grid):
        self.marker = marker
        self.grid = grid

    def check_rows(self):
        for i in range(3):
            if all(x == self.marker for x in self.grid[i]): return True
        return False

    def check_columns(self):
        for i in range(3):
            if all(row[i] == self.marker for row in self.grid): return True
        return False

    def check_diagonals(self):
        diagonal_1 = all(self.grid[i][j] == self.marker for i in range(3) for j in range(3) if i == j)
        diagonal_2 = all([self.grid[0][2] == self.marker, self.grid[1][1] == self.marker, self.grid[2][0] == self.marker])
        return any([diagonal_1,diagonal_2])

print("===== Tac-Tic-Toe =====")
user_marker = 'O'
system_marker = 'X'
Game = TacTicToe(user_marker = user_marker, system_marker = system_marker)
Game.display_board()

while True:
    if not possible_moves():
        print("~ Draw")
        break
    
    try:
        move = int(input("Enter Your Move (1-9), 0 to quit: "))
    except ValueError:
        print("Input Error: Not a number!\n")
        continue

    if move == 0: break
    if move not in range(10):
        print("Move Error: Invalid move!\n")
        continue

    elif move not in possible_moves().keys():
        print("Move Error: Move already been done!")
        continue
    
    Game.user_move(move)
    if Game.check_conditions(marker = user_marker):
        Game.display_board()
        print("~ You Win!")
        break

    Game.system_move()
    if Game.check_conditions(marker = system_marker):
        Game.display_board()
        print("~ You Lose!")
        break

    Game.display_board()