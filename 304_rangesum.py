
#304: Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

import numpy as np

matrix= [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]]

class NumMatrix(object):
    def __init__(self, matrix):

        self.matrix= np.array(matrix)

    def sumRegion(self, row1, col1, row2, col2):
        new= self.matrix[row1:row2+1, col1:col2+1]
        sum= np.sum(new)

        return sum



numMatrix= NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(0, 1, 2, 3)
print numMatrix.sumRegion(1, 2, 3, 4)


