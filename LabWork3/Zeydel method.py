import numpy as np

def zeidel(A, b, max_iterations=100, tolerance=1e-10):
    # Initialize x with zeros
    x = np.zeros_like(b)

    for _ in range(max_iterations):
        x_new = np.copy(x)

        # Iterate through each row
        for i in range(A.shape[0]):
            # Sum of the product of A and x for the current row
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])

            # Update x_new using the Zeidel method formula
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        # Check for convergence
        if np.allclose(x, x_new, rtol=tolerance):
            break

        x = x_new

    return x

# Define the matrices A and b
A = np.array([
    [ 1.0, -0.19385542, 0.42807229, 0.08325301],
    [ 0.0, 0.58180723, 0.06590361, 0.14566265],
    [ 0.0, 0.5293494, 5.5186747, -0.03963855],
    [ 0.0, 2.79262651, 0.59831325, 6.48409639]
])
b = np.array([1.16439759, -2.44753012, 44.16271084, -5.51427711])

# Call the Zeidel method
x = zeidel(A, b)

print("Solution:", x)