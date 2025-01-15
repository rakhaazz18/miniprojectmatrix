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

def subtract_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Dimensi matriks tidak sesuai untuk pengurangan.")
    rows, cols = len(A), len(A[0])
    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
    return result

if __name__ == "__main__":
    print("Operasi Pengurangan Matriks")
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
        result = subtract_matrices(A, B)
        print("Hasil Pengurangan Matriks:")
        print_matrix(result)
    except ValueError as e:
        print(e)     
        
