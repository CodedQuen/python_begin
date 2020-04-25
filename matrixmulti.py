class DenseMatrix(Matrix):

    def __mul__(self, mat):
        assert self.numberOfColumns == mat.numberOfRows
        result = DenseMatrix(
            self.numberOfRows, mat.numberOfColumns)

        for i in range(self.numberOfRows):
            for j in range(mat.numberOfColumns):
                sum = 0
                for k in range(self.numberOfColumns):
                    sum += self[i,k] * mat[k,j]
                result[i,j] = sum

        return result
