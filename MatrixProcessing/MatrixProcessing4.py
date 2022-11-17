from copy import deepcopy
from itertools import combinations, product

def read_matrix_keyboard():
    m, n = (int(e) for e in input('number of matrix rows and cols = ').split())
    matrix = []
    for i in range(m):
        line = input(f'row={i+1}: enter {n} numbers separated by a space: ')
        matrix.append([float(el) for el in line.strip().split()])
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(''.join(f'{el:^10.3f}' for el in row))

def get_sum_matrices(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        res = []
        for row1, row2 in zip(matrix1, matrix2):
            res.append([e1 + e2 for e1, e2 in zip(row1, row2)])
        return res
    else:
        return None

def multiply_matrix_by_value(matrix, value):
    res = deepcopy(matrix)
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] *= value
    return res



def matrix_mult_matrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    res = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
    return res

def get_transp_matrix(matrix, type='main'):
    if type == 'main':
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i, j in product(range(len(res)), range(len(res[0]))):
            res[i][j] = matrix[j][i]
    if type == 'side':
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i, j in product(range(len(res)), range(len(res[0]))):
            res[i][j] = matrix[len(matrix) - 1 - j][len(matrix[0]) - 1 - i]
    if type == 'vert':
        res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i, j in product(range(len(res)), range(len(res[0]))):
            res[i][j] = matrix[i][len(matrix[i])-1-j]
    if type == 'hor':
        res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i, j in product(range(len(res)), range(len(res[0]))):
            res[i][j] = matrix[len(matrix)-1 - i][j]
    return res


menu_txt = '''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit'''

menu_txt2 = '''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line'''


if __name__ == '__main__':
    while True:
        print(menu_txt)
        choice = input('> ')
        if choice == '0':
            break
        if choice == '1':
            m1 = read_matrix_keyboard()
            m2 = read_matrix_keyboard()
            m3 = get_sum_matrices(matrix1=m1, matrix2=m2)
            if m3:
                print('RESULT:')
                display_matrix(matrix=m3)
            else:
                print('ERROR')
        if choice == '2':
            m1 = read_matrix_keyboard()
            v1 = float(input('value = '))
            m3 = multiply_matrix_by_value(matrix=m1, value=v1)
            if m3:
                print('RESULT:')
                display_matrix(matrix=m3)
            else:
                print('ERROR')
        if choice == '3':
            m1 = read_matrix_keyboard()
            m2 = read_matrix_keyboard()
            m3 = matrix_mult_matrix(matrix1=m1, matrix2=m2)
            if m3:
                print('RESULT:')
                display_matrix(matrix=m3)
            else:
                print('ERROR')
        if choice == '4':
            print(menu_txt2)
            choice2 = input('> ')
            type = {'1': 'main', '2': 'side', '3': 'vert', '4': 'hor'}.get(choice2)
            m1 = read_matrix_keyboard()
            m3 = get_transp_matrix(matrix=m1, type=type)
            if m3:
                print('RESULT:')
                display_matrix(matrix=m3)
            else:
                print('ERROR')




