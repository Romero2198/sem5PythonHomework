def print_board(board):
    print('-' * 13)
    for i in range(3):
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print('-' * 13)
def take_input(player_token):
    player_answer = int(input(f'Куда поставим {player_token}?'))
    if (player_answer >= 1) and (player_answer <= 9):
        if(str(board[player_answer - 1]) not in "XO"):
            board[player_answer - 1] = player_token
        else:
            print('Эта клетка уже занята')
    else:
        print('Введите число от 1 до 9')
def check_win(board):
    winning_options = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in winning_options:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False
def main(board):
    counter = 0
    win = False
    while not win:
        print_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            if check_win(board):
                print(f'{check_win(board)} Ты выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья')
            break
    print_board(board)
board = list(range(1,10))
main(board)