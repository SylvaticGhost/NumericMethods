// ReSharper disable all MathAbsMethodIsRedundant
using Labwork2;

class Program
{
    static void Main()
    {
        DataProvider dataProvider = new DataProvider();

        Matrix A = dataProvider.A;

        Matrix B = dataProvider.B;

        Solve(A, B);
    }

    
    static void Solve(Matrix A, Matrix B)
    {
        Matrix U = Operations.CreatingUMatrix(A);

        Console.WriteLine("Matrix U:");
        U.Print();

        Matrix UTransposed = U.Copy();
        UTransposed.Transpose();

        Matrix Y = Operations.SolveSystemWithUpperTriangleMatrix(UTransposed, B);

        Console.WriteLine("Founded Y:");
        Y.Print();

        List<double> x = Operations.SolveSystemWithDownTriangleMatrix(U, Y);

        Matrix X = Matrix.CreateMatrixByColumn(x);

        Console.WriteLine("Result X:");
        X.Print();

        Console.WriteLine("vectorNeViazky:");
        Matrix vectorNeViazky = B - (A * X);
        Console.WriteLine(vectorNeViazky);
    }
}

