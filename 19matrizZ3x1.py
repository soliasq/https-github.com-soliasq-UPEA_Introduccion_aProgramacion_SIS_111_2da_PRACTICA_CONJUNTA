def generate_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        matrix[0][j] = j + 1

    for j in range(n - 2):
        matrix[1][j] = 1
    if n > 1:
        matrix[1][n - 2] = n + 1

    for j in range(n - 3):
        matrix[2][j] = 1
    if n > 2:
        matrix[2][n - 3] = n + 2

    for j in range(n - 4):
        matrix[3][j] = 1
    if n > 3:
        matrix[3][n - 4] = n + 3

    if n > 4:
        matrix[4][0] = 1
        matrix[4][1] = n + 4

    if n > 5:
        matrix[5] = [n + i for i in range(12, 12 + n)]

    return matrix

n = 6  # Cambia este valor para matrices de diferentes tamaños
result_matrix = generate_matrix(n)

for row in result_matrix:
    print(row)
