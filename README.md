# Implement Matrix Class

A Python implementation of a Matrix class with support for core matrix operations. This project provides a lightweight, dependency-free matrix implementation suitable for educational purposes and small-scale numerical computations.

## Features

The `Matrix` class supports the following operations:

### Core Methods

- **`determinant()`** - Calculates the determinant of a 1×1 or 2×2 matrix
- **`trace()`** - Calculates the trace (sum of diagonal entries)
- **`inverse()`** - Calculates the inverse of a 1×1 or 2×2 matrix
- **`T()`** - Returns a transposed copy of the matrix
- **`is_square()`** - Checks if the matrix is square

### Operator Overloading

- **`+`** - Matrix addition (`A + B`)
- **`-`** - Matrix negation (`-A`) and subtraction (`A - B`)
- **`*`** - Matrix multiplication (`A * B`) and scalar multiplication (`c * A`)

### Helper Functions

- **`zeroes(height, width)`** - Creates a matrix of zeros with specified dimensions
- **`identity(n)`** - Creates an n×n identity matrix

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```python
from matrix import Matrix, zeroes, identity

# Create matrices
A = Matrix([
    [2, 4],
    [3, 1]
])

B = Matrix([
    [1, 2],
    [3, 4]
])

# Basic operations
print("Matrix A:")
print(A)

print("Transpose of A:")
print(A.T())

print("A + B:")
print(A + B)

print("A * B:")
print(A * B)

print("2 * A:")
print(2 * A)

# Determinant and trace
print("Determinant of A:", A.determinant())
print("Trace of A:", A.trace())

# Inverse
print("Inverse of A:")
print(A.inverse())

# Verify A * A^-1 = I
print("A * A.inverse():")
print(A * A.inverse())

# Helper functions
print("3x3 Identity matrix:")
print(identity(3))

print("2x3 Zero matrix:")
print(zeroes(2, 3))
```

## Project Files

| File | Description |
|------|-------------|
| `matrix.py` | Main Matrix class implementation |
| `test.py` | Unit tests for the Matrix class |
| `matrix_playground.ipynb` | Jupyter notebook for interactive experimentation |
| `matrix_cheat_sheet.ipynb` | Reference notebook with matrix formulas and equations |
| `kalman_filter_demo.ipynb` | Demo showing the Matrix class used in a Kalman Filter |
| `datagenerator.py` | Helper for generating simulated sensor data |
| `requirements.txt` | Python dependencies |

## Running Tests

To verify that all matrix operations work correctly:

```bash
python test.py
```

Expected output:
```
Congratulations! All tests pass. Your Matrix class is working as expected.
```

## Mathematical Formulas

### Determinant (2×2)

For a matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:

$$\det(A) = ad - bc$$

### Trace

For an n×n matrix, the trace is the sum of diagonal elements:

$$\text{tr}(A) = \sum_{i=1}^{n} a_{ii}$$

### Inverse (2×2)

$$A^{-1} = \frac{1}{\det(A)} \left[ \text{tr}(A) \cdot I - A \right]$$

### Matrix Multiplication

For matrices A (m×n) and B (n×p):

$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

### Transpose

$$[A^T]_{ij} = [A]_{ji}$$

## Demo: Kalman Filter

Once the Matrix class is working, you can run the Kalman Filter demo in `kalman_filter_demo.ipynb`. This demonstrates a practical application of the Matrix class for sensor fusion and state estimation in autonomous vehicle tracking.

## Requirements

- Python 3.7+
- NumPy (for Kalman Filter demo)
- Pandas (for Kalman Filter demo)
- Matplotlib (for Kalman Filter demo)
