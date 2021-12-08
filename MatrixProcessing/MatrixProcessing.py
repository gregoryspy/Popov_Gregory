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

if __name__ == '__main__':
    m1 = read_matrix_keyboard()
    m2 = read_matrix_keyboard()
    m3 = get_sum_matrices(matrix1=m1, matrix2=m2)
    if m3:
        print('RESULT:')
        display_matrix(matrix=m3)
    else:
        print('ERROR')
