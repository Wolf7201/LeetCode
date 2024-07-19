def is_valid_input(exam, user_input):
    i = 0
    res = []
    curs = -1
    while i < len(user_input):
        if user_input[i] == '<':
            if user_input[i + 1] == 'd':  # Удаление после курсора
                i += 8
                if curs + 1 <= len(res) - 1:
                    res.pop(curs + 1)
            elif user_input[i + 1] == 'b':  # Удаление перед курсором
                i += 8
                if curs >= 0:
                    res.pop(curs)
                    curs -= 1  # Уменьшаем позицию курсора после удаления
            elif user_input[i + 1] == 'l':  # Курсор влево
                i += 6
                curs = max(-1, curs - 1)
            elif user_input[i + 1] == 'r':  # Курсор вправо
                i += 7
                curs = min(len(res), curs + 1)
            continue

        # Добавление символа
        res.insert(curs + 1, user_input[i])
        curs += 1
        i += 1

    # Сравнение с целевой строкой
    return "Yes" if res == exam else "No"


exam = list(input())
user_input = input()

print(is_valid_input(exam, user_input))
print(exam, user_input)

