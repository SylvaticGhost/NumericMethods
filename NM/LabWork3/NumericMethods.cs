namespace LabWork3;

public static class NumericMethods
{
    public static List<double> SolveByJacobi(Matrix beta, List<double> bList, double epsilon)
    {
        Matrix x = Matrix.CreateMatrixByColumn(bList);
        
        Matrix b = Matrix.CreateMatrixByColumn(bList);

        Matrix xNew = beta * x + b;
        
        int iterations = 0;
        
        while(!Operations.CalculateNorm(x, xNew, epsilon))
        {
            x = xNew;
            xNew = beta * x + b;
            iterations++;
        }

        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Iterations: " + iterations);
        Console.ResetColor();
        
        return xNew.GetColumn(0);
    }


    public static List<double> SolveBySeidel(Matrix A, List<double> bList, double epsilon)
    {
        Matrix x = Matrix.CreateZeroMatrix(bList.Count, 1);
        
        Matrix b = Matrix.CreateMatrixByColumn(bList);

        Matrix xNew = x.Copy();

        Matrix oldX;
        int iterations = 0;
        do
        {
            xNew = x.Copy();
            for (int i = 0; i < x.NumberOfRows; i++)
            {
                double sum1 = 0;
                double sum2 = 0;
                for (int j = 0; j < i; j++)
                {
                    sum1 += A[i][j] * xNew[j][0];
                }

                for (int j = i + 1; j < x.NumberOfRows; j++)
                {
                    sum2 += A[i][j] * x[j][0];
                }

                xNew[i][0] = (b[i][0] - sum1 - sum2) / A[i][i];
            }

            iterations++;
            oldX = x.Copy();
            x = xNew;
        } while (!Operations.CalculateNorm(oldX, xNew, epsilon));
        
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Iterations: " + iterations);
        Console.ResetColor();
        
        return xNew.GetAllNumbersInLine();
    }
}