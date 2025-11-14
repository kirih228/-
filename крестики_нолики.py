#Крестики нолики
#
#1) Вывод поля enter_board()
#2) Ход игрока player_move()
#3) Проверка победителя check_win()
#4) Проверка заполнения поля is_board_full()
#5) ВВод хода get_move()
'''
def enter_board(board):
    for row in board:
        print("|".join(row))
        print("-"*11)
        
def player_move(board,row,col,player):
    if board[row][col] == " - ":
        board[row][col] = player
    else:
        print("Эта клетка занята, попробуй другую")
        get_move(board,player)

def get_move(board,player):
    get = input("Введите индекс строки и столбца через пробел:").split()
    answer = []
    answer.append(int(get[0]))
    answer.append(int(get[1]))
    player_move(board,answer[0],answer[1],player)

def is_board_full(board):
    for row in board:
        if " - " in row:
            return False
    return True

def check_win(board):
    #проверка строк
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " - ":
            return board[0][i]
    #проверка столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " - ":
            return board[i][0]
    #проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " - ":
            return board[1][1]
    if board[2][0] == board[1][1] == board[0][2] != " - ":
            return board[1][1]


player = " X " #первый игрок
board = [[" - "," - "," - "],
         [" - "," - "," - "],
         [" - "," - "," - "]]

while True:
    enter_board(board)
    print(f"Ход игрока:{player}")
    get_move(board,player)

    if check_win(board):
        enter_board(board)
        print(f"Победил {check_win(board)}")
        break
    if is_board_full(board):
        enter_board(board)
        print(f"Ничья!!!")
        break
    if player == " X ":
        player = " O "
    else:
        player = " X "
'''

#Крестики нолики против бота
import random

def enter_board(board):
    for row in board:
        print("|".join(row))
        print("-"*11)
        
def player_move(board,row,col,player):
    if board[row][col] == " - ":
        board[row][col] = player
    else:
        print("Эта клетка занята, попробуй другую")
        get_move(board,player)

def get_move(board,player):
    get = input("Введите индекс строки и столбца через пробел:").split()
    answer = []
    answer.append(int(get[0]))
    answer.append(int(get[1]))
    player_move(board,answer[0],answer[1],player)

def is_board_full(board):
    for row in board:
        if " - " in row:
            return False
    return True

def check_win(board):
    #проверка строк
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " - ":
            return board[0][i]
    #проверка столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " - ":
            return board[i][0]
    #проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " - ":
            return board[1][1]
    if board[2][0] == board[1][1] == board[0][2] != " - ":
            return board[1][1]
        
def comp_move(board,player):
    row = random.randint(0,2)
    col = random.randint(0,2)
    print(f"Ход компьютера: {row} {col}")
    if board[row][col] == " - ":
        board[row][col] = player
    else:
        print("Oh...")
        comp_move(board,player)

player = " X " #первый игрок
board = [[" - "," - "," - "],
         [" - "," - "," - "],
         [" - "," - "," - "]]
while True:
    enter_board(board)
    print(f"Ход игрока:{player}")
    
    if player == " X ":
        get_move(board,player)
    else:
        comp_move(board,player)

    if check_win(board):
        enter_board(board)
        print(f"Победил {check_win(board)}")
        break
    
    if is_board_full(board):
        enter_board(board)
        print(f"Ничья!!!")
        break
    
    if player == " X ":
        player = " O "
    else:
        player = " X "
    
    



