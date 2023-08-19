board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def game_board(board):
    print(' ',board[0][0],'  |  ',board[0][1],'  |   ',board[0][2],' ')
    print('----------------------')
    print(' ',board[1][0],'  |  ',board[1][1],'  |   ',board[1][2],' ')
    print('----------------------')
    print(' ',board[2][0],'  |  ',board[2][1],'  |   ',board[2][2],' ')     
 
def winner(board, current):
    for i in range(0, 3):
        if all(board[i][j] == current for j in range(0, 3)) or all(board[j][i] == current for j in range(0, 3)):
            return True
        if  (all(board[i][i] == current for i in range(0, 3)) or all(board[i][2 - i] == current for i in range(0, 3))):
            return True
    return False
    
def handel_player_move(board,current):
    print('player ',current)
    row=int(input('Enter row (0-2) '))
    column=int(input('Enter column (0-2) '))
    if(row>=0 and row<=2 and column>=0 and column<=2):
        if board[row][column] != ' ':
                print('This cell is already occupied. Try again.')
                handel_player_move(board,current)
        else:
                board[row][column] = current
                game_board(board)
  
    else:
        print('You have enter invaild place try again.')
        handel_player_move(board,current)
game_board(board)
x=0
o=0
while True:
    if x>o:
        current='O'
        o+=1
    else:
        current='X' 
        x+=1
    handel_player_move(board,current)
    if winner(board,current):
        print("The Winner Is Player ",current)
        break
    if x+o==9 :
        print("NO One Win!!")
        break