using LabWork3;

DataProvider dataProvider = new ();

Matrix A = new (dataProvider.ContainingA);

Matrix B = Matrix.CreateMatrixByColumn(dataProvider.ContainingB);

double epsilon = dataProvider.Epsilon;

Console.WriteLine("Matrix A:");
A.Print();

Console.WriteLine("Matrix B:");
B.Print();

Console.WriteLine(Operations.IsDiagonalDominant(dataProvider.ContainingA) ? "Matrix is diagonal dominant" : "Matrix is not diagonal dominant\n");

Matrix beta = Operations.CalculateBeta(A);

List<double> x = Operations.CalculateX(dataProvider.ContainingB, A);

Console.WriteLine("beta:");
beta.Print();

Console.WriteLine("x:");
x.ForEach(Console.WriteLine);
Console.WriteLine();

NumericMethods numericMethods = new NumericMethods(A, B, epsilon);


Console.ForegroundColor = ConsoleColor.DarkBlue;
Console.WriteLine("Solving by Jacobi method:");
Console.ResetColor();

var ans = numericMethods.SolveByJacobi(beta, x, epsilon);
PrintWordAnswer();
ans.ForEach(Console.WriteLine);

Console.WriteLine();

Console.ForegroundColor = ConsoleColor.DarkBlue;
Console.WriteLine("Solving by Seidel method:");
Console.ResetColor();

ans = numericMethods.SolveBySeidel();

PrintWordAnswer();
ans.ForEach(Console.WriteLine);


void PrintWordAnswer()
{
    Console.ForegroundColor = ConsoleColor.DarkYellow;
    Console.WriteLine("Answer:");
    Console.ResetColor();
}