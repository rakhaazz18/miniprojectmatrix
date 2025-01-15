def input_matrix(rows, cols):
    print(f"Masukkan elemen matriks berukuran {rows}x{cols}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Baris {i+1}: ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(size):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det

def inverse_matrix(matrix):
    size = len(matrix)
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matriks tidak memiliki invers (determinannya nol).")
    cofactors = []
    for r in range(size):
        cofactor_row = []
        for c in range(size):
            minor = [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]
            cofactor_row.append(((-1) ** (r + c)) * determinant(minor))
        cofactors.append(cofactor_row)
    adjoint = [[cofactors[j][i] for j in range(size)] for i in range(size)]
    inverse = [[adjoint[i][j] / det for j in range(size)] for i in range(size)]
    return inverse

if __name__ == "__main__":
    print("Operasi Invers Matriks")
    size = int(input("Ukuran matriks persegi (maksimal 4): "))
    if size > 4:
        raise ValueError("Ukuran matriks tidak boleh lebih dari 4x4.")

    matrix = input_matrix(size, size)

    try:
        result = inverse_matrix(matrix)
        print("Invers Matriks:")
        print_matrix(result)
    except ValueError as e:
        print(e)
