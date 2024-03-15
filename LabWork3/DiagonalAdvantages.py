import numpy as np

def get_diag_advantage_matrix(matrix):
  """
  This function takes a square matrix and returns a new matrix where the diagonal elements
  are the maximum values in their respective rows and columns, and all other elements are zero.

  Args:
      matrix: A square NumPy array.

  Returns:
      A new NumPy array with the diagonal advantage.
  """
  rows, cols = matrix.shape
  diag_adv_matrix = matrix.copy()
  diag_adv_matrix[:] = 0

  row_maxs = np.max(matrix, axis=1)
  col_maxs = np.max(matrix, axis=0)

  for i in range(rows):
    diag_adv_matrix[i, i] = max(row_maxs[i], col_maxs[i])

  return diag_adv_matrix

# Example usage

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diag_adv_matrix = get_diag_advantage_matrix(matrix)

print(diag_adv_matrix)

k= 3
a = k / 5

beta = k / 5

matrix = np.array([
            [8.30, 2.62 + a, 4.10, 1.90],
            [3.92, 8.45, 8.78 - a, 2.46],
            [3.77, 7.21 + a, 8.04, 2.28],
            [2.21, 3.65 - a, 1.69, 6.99]
        ])

advg = get_diag_advantage_matrix(matrix)
print(advg)
print(advg[1][3])