final = input()
s = input()

i = 0
f_n = []
j = -1
while i < len(s):
    if s[i] == '<':
        # left
        if s[i:i + 6] == '<left>':
            j = max(j - 1, -1)
            i += 6
        # right
        elif s[i:i + 7] == '<right>':
            j = min(j + 1, len(f_n) - 1)
            i += 7
        # bspace
        elif s[i:i + 8] == '<bspace>':
            if j > -1:
                f_n.pop(j)
                j -= 1
            i += 8
        # delete
        elif s[i:i + 8] == '<delete>':
            if len(f_n) > 0 and j < len(f_n) - 1:
                f_n.pop(j + 1)
            i += 8
        else:
            f_n.insert(j + 1, s[i])
            j += 1
            i += 1
    else:
        f_n.insert(j + 1, s[i])
        j += 1
        i += 1

if list(final) == f_n:
    print('Yes')
else:
    print('No')

final = input()
s = input()

i = 0
f_n = []
j = -1
while i < len(s):
    if s[i] == '<':
        # left
        if s[i + 1] == 'l':
            j = max(j - 1, -1)
            i += 6
        # right
        elif s[i + 1] == 'r':
            j = min(j + 1, len(f_n) - 1)
            i += 7
        # bspace
        elif s[i + 1] == 'b':
            if j > -1:
                f_n.pop(j)
                j -= 1
            i += 8
        # delete
        elif s[i + 1] == 'd':
            if len(f_n) > 0 and j < len(f_n) - 1:
                f_n.pop(j + 1)
            i += 8
    else:
        f_n.insert(j + 1, s[i])
        j += 1
        i += 1

if list(final) == f_n:
    print('Yes')
else:
    print('No')
