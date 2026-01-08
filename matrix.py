import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            return self.g[0][0]
        else:
            # 2x2 matrix: det = ad - bc
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a * d - b * c

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        total = 0
        for i in range(self.h):
            total += self.g[i][i]
        return total

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if self.h == 1:
            # For 1x1 matrix, inverse is simply 1/a
            return Matrix([[1.0 / self.g[0][0]]])
        else:
            # For 2x2 matrix: A^-1 = (1/det(A)) * (tr(A)*I - A)
            det = self.determinant()
            tr = self.trace()
            I = identity(2)
            
            # Calculate tr(A)*I - A
            result = []
            for i in range(2):
                row = []
                for j in range(2):
                    row.append(tr * I.g[i][j] - self.g[i][j])
                result.append(row)
            
            # Multiply by 1/det
            for i in range(2):
                for j in range(2):
                    result[i][j] = result[i][j] / det
            
            return Matrix(result)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # Transpose: result[i][j] = self[j][i]
        result = []
        for j in range(self.w):
            row = []
            for i in range(self.h):
                row.append(self.g[i][j])
            result.append(row)
        return Matrix(result)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            result.append(row)
        return Matrix(result)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        result = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self.g[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + (-other)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        # Matrix multiplication: (AB)_ij = sum over k of a_ik * b_kj
        # A is m x n, B is n x p, result is m x p
        if self.w != other.h:
            raise(ValueError, "Matrix dimensions incompatible for multiplication")
        
        result = []
        for i in range(self.h):
            row = []
            for j in range(other.w):
                # Calculate dot product of row i of self and column j of other
                total = 0
                for k in range(self.w):
                    total += self.g[i][k] * other.g[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            result = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(other * self.g[i][j])
                result.append(row)
            return Matrix(result)