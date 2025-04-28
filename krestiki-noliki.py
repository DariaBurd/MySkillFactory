def display_board(board):   #отображаем текущее состояние игрового поля
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):  #проверяем текущее состояние игрового поля и определяем, завершилась ли игра
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # горизонтали
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  # вертикали
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # диагонали
        [(0, 2), (1, 1), (2, 0)]
    ]

    for condition in win_conditions:
        if all([board[x][y] == player for x, y in condition]):
            return True
    return False


def is_full(board):  #проверяем, заполнено ли поле полностью(ничья)
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True


def get_valid_move():  #Обеспечиваем проверку корректности ввода пользователем координат для хода.
    while True:
        move = input("Введите позицию (1-9): ").strip()
        if move.isdigit():
            move_num = int(move)
            if 1 <= move_num <= 9:
                return move_num
            else:
                print("Число должно быть от 1 до 9. Попробуйте снова.")
        else:
            print("Введите число от 1 до 9.")

def my_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    players = ('X', 'O')
    turn = 0

    while True:
        display_board(board)
        player = players[turn % 2]
        print(f"Ход {player}:")

        move = get_valid_move() - 1  # Приведение индекса к диапазону 0-8
        x, y = divmod(move, 3)       # Перевод номера в координаты

        if board[x][y] != ' ':
            print("Позиция уже занята. Попробуйте снова.")
            continue

        board[x][y] = player

        if check_winner(board, player):
            display_board(board)
            print(f"{player} победил!")
            break

        if is_full(board):
            display_board(board)
            print("Ничья.")
            break

        turn += 1

if __name__ == "__main__":
    my_game()