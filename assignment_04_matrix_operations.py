# =============================================================================
# HELPER FUNCTIONS (Input & Display)
# =============================================================================

def read_matrix(rows, cols, matrix_name=""):
    """Reads a matrix of size rows x cols from user input."""
    prompt_prefix = f"for {matrix_name} " if matrix_name else ""
    matrix = []
    for i in range(rows):
        row_str = input(f"Enter row {i + 1} {prompt_prefix}({cols} values separated by spaces): ")
        row = [float(x) for x in row_str.strip().split()]
        
        # Validation for row length
        while len(row) != cols:
            print(f"Error: Expected {cols} values. Try again.")
            row_str = input(f"Enter row {i + 1} {prompt_prefix}: ")
            row = [float(x) for x in row_str.strip().split()]
            
        matrix.append(row)
    return matrix


def print_matrix(matrix, title="Matrix"):
    """Prints a 2D list formatted nicely in a aligned grid."""
    print(f"\n--- {title} ---")
    for row in matrix:
        for val in row:
            # Displays integers cleanly (e.g., 5 instead of 5.0) or formatted floats
            val_str = f"{int(val)}" if val.is_integer() else f"{val:.2f}"
            print(f"{val_str:>6}", end=" ")
        print()
    print()


# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================

def transpose_matrix(matrix):
    """
    Computes the transpose of an M x N matrix.
    Rows become columns, and columns become rows.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an empty N x M result matrix
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed


# =============================================================================
# PART B — Add Two Matrices
# =============================================================================

def add_matrices(matrix_a, matrix_b):
    """
    Computes the element-wise sum of two M x N matrices.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for i in range(rows):
        row_sum = []
        for j in range(cols):
            row_sum.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row_sum)
        
    return result


# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================

def multiply_matrices(matrix_a, matrix_b):
    """
    Computes the dot product of matrix_a (M x N) and matrix_b (N x P).
    Returns an M x P matrix.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    # Result size will be M x P
    result = []
    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            # Compute dot product for position (i, j)
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            row_result.append(dot_product)
        result.append(row_result)
        
    return result


# =============================================================================
# MAIN PROGRAM DRIVER
# =============================================================================

def main():
    print("==================================================")
    print("          MATRIX OPERATIONS PROGRAM               ")
    print("==================================================")
    
    # -------------------------------------------------------------------------
    # PART A DEMO: Transpose
    # -------------------------------------------------------------------------
    print("\n>>> PART A: Transpose Matrix")
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))
    
    mat = read_matrix(m, n)
    print_matrix(mat, "Original Matrix")
    
    transposed = transpose_matrix(mat)
    print_matrix(transposed, "Transposed Matrix")

    # -------------------------------------------------------------------------
    # PART B DEMO: Addition
    # -------------------------------------------------------------------------
    print("\n>>> PART B: Add Two Matrices (M x N)")
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))
    
    print("\n-- Enter Matrix A --")
    mat_a = read_matrix(m, n, "Matrix A")
    
    print("\n-- Enter Matrix B --")
    mat_b = read_matrix(m, n, "Matrix B")
    
    print_matrix(mat_a, "Matrix A")
    print_matrix(mat_b, "Matrix B")
    
    sum_result = add_matrices(mat_a, mat_b)
    print_matrix(sum_result, "Sum (A + B)")

    # -------------------------------------------------------------------------
    # PART C DEMO: Multiplication
    # -------------------------------------------------------------------------
    print("\n>>> PART C: Multiply Two Matrices (A: M x N, B: N x P)")
    m = int(input("Enter rows for Matrix A (M): "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter columns for Matrix B (P): "))
    
    print("\n-- Enter Matrix A --")
    mat_a = read_matrix(m, n, "Matrix A")
    
    print("\n-- Enter Matrix B --")
    mat_b = read_matrix(n, p, "Matrix B")
    
    print_matrix(mat_a, "Matrix A")
    print_matrix(mat_b, "Matrix B")
    
    prod_result = multiply_matrices(mat_a, mat_b)
    print_matrix(prod_result, "Product (A × B)")


if __name__ == "__main__":
    main()