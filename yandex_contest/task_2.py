def is_valid_input(exam, input_str):
    i = 0
    res = []
    curs = -1
    while i < len(input_str):
        if input_str[i] == '<':
            # left
            if input_str[i + 1] == 'l':
                curs = max(curs - 1, -1)
                i += 6
            # right
            elif input_str[i + 1] == 'r':
                curs = min(curs + 1, len(res) - 1)
                i += 7
            # bspace
            elif input_str[i + 1] == 'b':
                if curs > -1:
                    res.pop(curs)
                    curs -= 1
                i += 8
            # delete
            elif input_str[i + 1] == 'd':
                if len(res) > 0 and curs < len(res) - 1:
                    res.pop(curs + 1)
                i += 8
        else:
            res.insert(curs + 1, input_str[i])
            curs += 1
            i += 1

    print(exam)
    print(res)
    return 'Yes' if exam == res else 'No'


exam = 'delete'
user_input = 'delx<left><delete>ete'

print(is_valid_input(exam, user_input))


def test_is_valid_input():
    test_cases = [
        ("test", "test", "Yes"),
        ("backspace", "backspa<bspace>ce", "No"),
        ("delete", "delx<left><delete>ete", "Yes"),
        ("leftright", "left<right>r<left>ight", "No"),
        ("nodelet", "<delete>nodelete<bspace>", "Yes"),
        ("olexmp", "comp<left><left><left><left><delete><bspace><right>lex", "Yes"),
        # Этот тест предполагает, что программа может обрабатывать строки длиннее 1000 символов,
        # хотя согласно условию задачи она не должна. Это просто пример.

    ]

    for i, (exam, user_input, expected) in enumerate(test_cases, start=1):
        result = is_valid_input(list(exam), user_input)
        assert result == expected, f"Тест {i} провален: ожидается {expected}, получено {result}"
        print(f"Тест {i} пройден успешно.")


# Запускаем тесты
test_is_valid_input()
