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

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua.")
    result = [[sum(A[i][k] * B[k][j] for k in range(cols_A)) for j in range(cols_B)] for i in range(rows_A)]
    return result

if __name__ == "__main__":
    print("Operasi Perkalian Matriks")
    rows_A = int(input("Jumlah baris matriks pertama (maksimal 4): "))
    cols_A = int(input("Jumlah kolom matriks pertama (maksimal 4): "))
    if rows_A > 4 or cols_A > 4:
        raise ValueError("Ukuran matriks tidak boleh lebih dari 4x4.")

    A = input_matrix(rows_A, cols_A)

    rows_B = int(input("Jumlah baris matriks kedua (maksimal 4): "))
    cols_B = int(input("Jumlah kolom matriks kedua (maksimal 4): "))
    if rows_B > 4 or cols_B > 4:
        raise ValueError("Ukuran matriks tidak boleh lebih dari 4x4.")

    B = input_matrix(rows_B, cols_B)

    try:
        result = multiply_matrices(A, B)
        print("Hasil Perkalian Matriks:")
        print_matrix(result)
    except ValueError as e:
        print(e)


