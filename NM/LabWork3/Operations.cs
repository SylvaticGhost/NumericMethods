namespace LabWork3;


public static class Operations
{
    public static bool IsDiagonalDominant(IList<List<double>> matrix)
    {
        for (int i = 0; i < matrix.Count; i++)
        {
            double sumMainDiag = 0;
            double sumPerifDiag = 0;
            for (int j = 0; j < matrix.Count; j++)
            {
                if (i != j)
                {
                    sumMainDiag += Math.Abs(matrix[i][j]);
                }

                if (matrix.Count - 1 - i != j)
                {
                    sumPerifDiag += Math.Abs(matrix[i][j]);
                }
            }

            if (Math.Abs(matrix[i][i]) < sumMainDiag && Math.Abs(matrix[i][matrix.Count - 1 - i]) < sumPerifDiag)
            {
                return false;
            }
        }

        return true;
    }
    

    public static Matrix CalculateBeta(Matrix A)
    {
        Matrix beta = Matrix.CreateZeroMatrix(A.NumberOfRows, A.NumberOfColumns);
        
        for (int i = 0; i < A.NumberOfRows; i++)
        {
            for (int j = 0; j < A.NumberOfColumns; j++)
            {
                if (i != j)
                {
                    beta[i, j] =  - A[i, j] / A[i, i];
                }
            }
        }
        
        return beta;
    }


    public static List<double> CalculateX(List<double> b, Matrix A)
    {
        List<double> x = [];

        for (int i = 0; i < b.Count; i++)
        {
            x.Add(b[i]/ A[i][i]);
        }
        
        return x;
    }


    public static bool CheckConvergence(Matrix A)
    {
        double l1 = 0;

        for (int i = 0; i < A.NumberOfRows; i++)
        {
            l1 += Math.Abs(A[i][i]);
        }

        double l2 = 0;

        for (int i = 0; i < A.NumberOfRows; i++)
        {
            l2 += Math.Abs(A[i][A.NumberOfRows - 1 - i]);
        }
        
        return l1 < 0 || l2 < 0;
    }


    public static bool CalculateNorm(Matrix x, Matrix xNew, double epsilon)
    {
        for(int i = 0; i < x.NumberOfRows; i++)
        {
            if(Math.Abs(x[i][0] - xNew[i][0]) > epsilon)
                return false;
        }
        
        return true;
    }

}