def check_winner(moves):
    board = {}
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # горизонталь, вертикаль, две диагонали

    def is_winner(player, r, c):
        for dr, dc in directions:
            count = 1
            for i in range(1, 5):  # Проверяем в одном направлении
                if (r + dr * i, c + dc * i) in board and board[(r + dr * i, c + dc * i)] == player:
                    count += 1
                else:
                    break
            for i in range(1, 5):  # Проверяем в противоположном направлении
                if (r - dr * i, c - dc * i) in board and board[(r - dr * i, c - dc * i)] == player:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

    winner = None
    for i, (r, c) in enumerate(moves):
        player = 'First' if i % 2 == 0 else 'Second'
        board[(r, c)] = player
        if is_winner(player, r, c):
            if winner and winner != player:
                return "Inattention"  # Игра продолжалась после победы другого игрока
            winner = player
            winning_move = i + 1

    if winner:
        if winning_move < len(moves):
            return "Inattention"  # Игра продолжалась после победы
        return winner
    return "Draw"


moves1 = [(4, 4), (4, 5), (2, 2), (2, 3), (3, 3), (3, 4), (1, 1), (1, 2), (5, 5)]
# Пример ввода 2
moves2 = [(5, 0), (1, 1), (4, 0), (2, 1), (3, 0), (3, 1), (2, 0), (4, 1), (1, 0), (5, 1)]

result1 = check_winner(moves1)
result2 = check_winner(moves2)

print(result1)
print(result2)
