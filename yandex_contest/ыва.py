def valid(nickname):
    if len(nickname) < 8:
        return 'NO'
    a = any(char.isdigit() for char in nickname)
    b = any(char.islower() for char in nickname)
    c = any(char.isupper() for char in nickname)
    if a and b and c:
        return 'YES'
    return 'NO'


nickname = input()

print(valid(nickname))
