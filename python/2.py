def rotate_matrix_90_degrees(matrix):
    # Транспонирование матрицы
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # Переворачивание строк транспонированной матрицы
    rotated_matrix = [row[::-1] for row in transposed_matrix]
    return rotated_matrix


def task_2(n, m):
    if n > 0 and m > 0:
        matrix = [list(map(int, input().split())) for _ in range(n)]
        return rotate_matrix_90_degrees(matrix)
    return []


# Чтение размеров матрицы
n, m = list(map(int, input().split()))

# Выполнение поворота и вывод результата
for line_matrix in task_2(n, m):
    print(*line_matrix)
