import numpy as np

# Vector Operations
def vector_operations():
    # Creating a vector
    vec = np.array([1, 2, 3, 4, 5])
    print(f"Original Vector: {vec}")

    # Indexing the vector
    print(f"Element at index 2: {vec[2]}")

    # Slicing the vector
    sliced_vec = vec[1:4]
    print(f"Sliced Vector (1:4): {sliced_vec}")

# Matrix Operations
def matrix_operations():
    # Creating a matrix
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Original Matrix:\n{mat}")

    # Indexing the matrix
    print(f"Element at row 1, col 2: {mat[1, 2]}")

    # Slicing the matrix (submatrix)
    sliced_mat = mat[1:, 1:]
    print(f"Sliced Matrix (1:, 1:):\n{sliced_mat}")

    # Determinant of the matrix (only possible for square matrices)
    det = np.linalg.det(mat)
    print(f"Determinant of the matrix: {det:.2f}")

# Stacking Operations
def stacking_operations():
    # Creating two vectors
    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])

    # Vertical stacking (rows)
    vert_stack = np.vstack((vec1, vec2))
    print(f"Vertical Stack of Vectors:\n{vert_stack}")

    # Horizontal stacking (columns)
    horz_stack = np.hstack((vec1, vec2))
    print(f"Horizontal Stack of Vectors:\n{horz_stack}")

    # Creating two matrices for stacking
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])

    # Vertical stacking of matrices
    vert_stack_mat = np.vstack((mat1, mat2))
    print(f"Vertical Stack of Matrices:\n{vert_stack_mat}")

    # Horizontal stacking of matrices
    horz_stack_mat = np.hstack((mat1, mat2))
    print(f"Horizontal Stack of Matrices:\n{horz_stack_mat}")

if __name__ == "__main__":
    print("Vector Operations:")
    vector_operations()
    print("\nMatrix Operations:")
    matrix_operations()
    print("\nStacking Operations:")
    stacking_operations()
