import random
GameGrid = [[1,2,3],[4,5,6],[7,8,9]]

class TacTicToe:
    def __init__(self, user_marker, system_marker):
        self.user_marker = user_marker
        self.system_marker = system_marker

    def display_board(self):
        print()
        for j,row in enumerate(GameGrid):
            for i in range(3):
                print(f" {row[i]} " if i != 1 else f"| {row[i]} |", end = "")
            print("\n---|---|---" if j != 2 else "\n")

    def available_moves(self):
        return {move : (i,j) for i,row in enumerate(GameGrid) for j,move in enumerate(row) if isinstance(move, int)}
    
    def user_move(self, move):
        i, j = self.available_moves()[move]
        GameGrid[i][j] = self.user_marker

    def system_move(self):
        if not self.available_moves(): return
        moves_l = list(self.available_moves().values())
        i, j = random.choice(moves_l)
        GameGrid[i][j] = self.system_marker

    def check_conditions(self, marker):
        conditions = GameConditions(marker = marker)
        return any([conditions.check_rows(), conditions.check_columns(), conditions.check_diagnols()])

class GameConditions:
    def __init__(self, marker):
        self.marker = marker

    def check_rows(self):
        for i in range(3):
            if all(x == self.marker for x in GameGrid[i]): return True
        return False

    def check_columns(self):
        for i in range(3):
            if all(row[i] == self.marker for row in GameGrid): return True
        return False

    def check_diagnols(self):
        diagnol_1 = all(GameGrid[i][j] == self.marker for i in range(3) for j in range(3) if i == j)
        diagnol_2 = all([GameGrid[0][2] == self.marker, GameGrid[1][1] == self.marker, GameGrid[2][0] == self.marker])
        return any([diagnol_1,diagnol_2])

class AdvanceSystemMove:
    def __init__(self, moves: dict):
        self.possible_moves = moves

    def make_move(self,row,column):
        if not (row, column) in self.possible_moves.values(): return False
        GameGrid[row][column] = 'X'
        return True
    
    def defend(self):
        for i in range(3):
            row_remain_move = [j for j ,move in enumerate(GameGrid[i]) if isinstance(move, int) or move == 'X']
            if len(row_remain_move) == 1: 
                if self.make_move(row = i, column = row_remain_move[0]): return True
                
        for i in range(3):
            column_remain_move = [j for j ,row in enumerate(GameGrid) if isinstance(row[i], int) or row[i] == 'X']
            if len(column_remain_move) == 1: 
                if self.make_move(row = column_remain_move[0], column = i): return True

        d1_remain_move = [(i,j) for i in range(3) for j in range(3) 
                          if i == j and (isinstance(GameGrid[i][j], int) or GameGrid[i][j] == 'X')]
        if len(d1_remain_move) == 1:
            i, j = d1_remain_move[0]
            if self.make_move(row = i, column = j): return True

        d2_remain_move = [(i,j) for i, j in zip([0,-1,1],range(-1,2)) if isinstance(GameGrid[i][j], int) or GameGrid[i][j] == 'X']
        if len(d2_remain_move) == 1: 
            i, j = d2_remain_move[0]
            if self.make_move(row = i, column = j): return True

        return False 

    
print("===== Tac-Tic-Toe =====")
Game = TacTicToe(user_marker = 'O', system_marker = 'X')
Game.display_board()

while True:
    if not Game.available_moves():
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

    elif move not in Game.available_moves().keys():
        print("Move Error: Move already been done!")
        continue
    
    Game.user_move(move)
    if Game.check_conditions(marker = 'O'):
        Game.display_board()
        print("~ You Win!")
        break
    if not AdvanceSystemMove().defend():
        Game.system_move()
    if Game.check_conditions(marker = 'X'):
        Game.display_board()
        print("~ You Lose!")
        break
    Game.display_board()