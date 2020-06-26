import numpy as np

class Matrix:
    def __init__(self, matrix, shape = (0, 0)):
        self.matrix = matrix 
        self.shape = matrix.shape
    
    def show_matrix(self):
        print(self.matrix) 

    def transposed(self):
        transposta = np.zeros((self.shape[1], self.shape[0]))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                transposta[j][i] = self.matrix[i][j] 
        return transposta

    def determinant(self):
        if self.shape[0] != self.shape[1]:
            print('the matrix is not square and therefore does not have a determinant')
            return None
        else:
            return np.linalg.det(self.matrix)

    def inverse(self):
        if self.shape[0] != self.shape[1]:
            print('the matrix is not square and therefore does not have a inverse')
            return None
        else:
            return np.linalg.inv(self.matrix)
            

test = np.array([[1,2,3], [4,5,6], [3,2,5]])
exemplo = Matrix(test)
exemplo.show_matrix()
print(exemplo.transposed())
print(exemplo.determinant())
print(exemplo.inverse())