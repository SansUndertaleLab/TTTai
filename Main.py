exampleBoard="---------"
def print_board(board):
    print(board[0:3]+"\n"+board[3:6]+"\n"+board[6:9])
def check_for_win(board):
    for i in ["o","x"]:
        if board[0:3]==i*3:
            return i
        elif board[3:6]==i*3:
            return i
        elif board[6:9]==i*3:
            return i
        elif board[0:11:3]==i*3:
            return i
        elif board[1:11:3]==i*3:
            return i
        elif board[2:11:3]==i*3:
            return i
        elif board[0]+board[4]+board[8]==i*3:
            return i
        elif board[2]+board[4]+board[6]==i*3:
            return i
    return "-"
def analyse_board(board):
    pass
print(check_for_win(exampleBoard))
print_board(exampleBoard)