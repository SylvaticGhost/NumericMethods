import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return 5*x**5 - x**2 - 3*x + 6

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate y values
y = f(x)

# Create the plot
plt.plot(x, y)

# Set the labels for x and y axis
plt.xlabel('x')
plt.ylabel('f(x)')

plt.axvline(x=0, color='black', lw=0.5)
plt.axhline(y=0, color='black', lw=0.5)

# Set the title of the graph
plt.title('Plot of f(x) = 5*x^5 - x^2 - 3*x + 6')

# Display the plot
plt.show()

coefficients = [5, 0, 0, -1, -3, 6]

# Compute the roots of the polynomial
roots = np.roots(coefficients)

# Print the roots
print(roots)