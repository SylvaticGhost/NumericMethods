namespace LabWork3;

public class NumericMethods
{
    private Matrix A;

    private Matrix b;

    private readonly double epsilon;

    public NumericMethods(Matrix matrixA, Matrix matrixB, double epsilon)
    {
        A = matrixA;
        b = matrixB;
        this.epsilon = epsilon;
    }
    
    
    public List<double> SolveByJacobi(Matrix beta, List<double> bList, double epsilon)
    {
        Matrix x = Matrix.CreateMatrixByColumn(bList);
        
        Matrix b = Matrix.CreateMatrixByColumn(bList);

        Matrix xNew = beta * x + b;
        
        int iterations = 0;
        
        while(!Operations.CalculateNorm(x, xNew, epsilon))
        {
            if (iterations is > 0 and <= 3)
            {
                PrintResultOnIterations(x, iterations);
            }
            PrintUnpackVectorOnIterations(ref x, iterations);
            
            x = xNew;
            xNew = beta * x + b;
            iterations++;
        }
        PrintUnpackVectorOnIterations(ref x, iterations);
        Console.WriteLine();
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Iterations: " + iterations);
        Console.ResetColor();
        
        return xNew.GetColumn(0);
    }


    public List<double> SolveBySeidel()
    {
        Matrix x = Matrix.CreateZeroMatrix(b.NumberOfRows, 1);

        Matrix xNew = x.Copy();

        Matrix oldX;
        int iterations = 0;
        do
        {
            if (iterations <= 3)
            {
                PrintResultOnIterations(x, iterations);
            }
            PrintUnpackVectorOnIterations(ref x, iterations);
            
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
        
        PrintUnpackVectorOnIterations(ref x, iterations);
        
        Console.ForegroundColor = ConsoleColor.Cyan;
        Console.WriteLine("Completed iterations: " + iterations);
        Console.ResetColor();
        
        return xNew.GetAllNumbersInLine();
    }


    private static void PrintResultOnIterations(Matrix x, int iterations)
    {
        Console.WriteLine("iterations: " + iterations);
        Console.WriteLine("Vector x:");
        x.PrintInOneLine();
        Console.WriteLine();
    }
    

    void PrintUnpackVectorOnIterations(ref Matrix x, int iteration)
    {
        if(iteration == 0)
            return;
        
        Matrix unpackVector = b - (A * x);

        Console.WriteLine($"Unpack vector on {iteration} iteration");
        unpackVector.PrintInOneLine();
        Console.WriteLine();
    }
}