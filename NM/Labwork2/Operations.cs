namespace Labwork2;

public class Operations
{
    public static Matrix CreatingUMatrix(Matrix matrixA)
    {
        Matrix matrixU = new(matrixA.Containing.Count, matrixA.Containing[0].Count);

        for (int i = 0; i < matrixA.NumberOfRows; i++)
        {
            for (int j = 0; j < matrixA.NumberOfColumns; j++)
            {
                if(i == j)
                    matrixU[i][j] = Math.Sqrt(matrixA[i][i] - SumOfUki(matrixU, i, j));
                else
                {
                    if (j < i)
                        matrixU[i][j] = 0;
                    else
                        matrixU[i][j] = 1/matrixU[i,i] * (matrixA[i, j] - SumOfUkiUkj(matrixU, i, j));
                }
                    
            }
        }
        
        return matrixU;
    }
    
    
    private static double SumOfUki(Matrix matrixU, int i, int n)
    {
        double sum = 0;
        
        for (int k = 0; k < n; k++)
        {
            sum += Math.Pow(matrixU[k, i], 2);
        }

        return sum;
    }
    
    
    private static double SumOfUkiUkj(Matrix matrixU, int i, int j)
    {
        double sum = 0;
        
        for (int k = 0; k < i; k++)
        {
            sum += matrixU[k, i] * matrixU[k, j];
        }

        return sum;
    }


    //A * X = B
    //X = A^(-1) * B
    public static Matrix SolveSystemWithUpperTriangleMatrix(Matrix A, Matrix B)
    {
        Matrix AInversed = A.GetInverse();
    
        Matrix X = AInversed * B;
   

        return X;
    }


    public static List<double> SolveSystemWithDownTriangleMatrix(Matrix A, Matrix B)
    {
        Matrix AReversed = A.GetMatrixWithReversedRow(), BReversed = B.GetMatrixWithReversedRow();

        Matrix res = SolveSystemWithUpperTriangleMatrix(AReversed, BReversed);

        var r = res.GetAllNumbersInLine();

        r.Reverse();

        return r;
    }
}