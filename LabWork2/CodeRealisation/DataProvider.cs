namespace Labwork2;

public class DataProvider
{
    private const int n_var = 25;

    private readonly float k1 = Math.Abs(n_var - 25);

    private readonly float k2 = Math.Abs(n_var - 21);

    private float a;

    private float beta;

    public List<List<double>> containingA;

    public List<double> containingB;

    public Matrix A { get; private set; }

    public Matrix B { get; private set; }

    public DataProvider()
    {

        a = k1 / 4;

        beta = (float)(k2 * 0.35);

        containingA =
        [
            [5.18 + a, 1.12, 0.95, 1.32, 0.83],
            [1.12, 4.28 - a, 2.12, 0.57, 0.91],
            [0.95, 2.12, 6.13 + a, 1.29, 1.57],
            [1.32, 0.57, 1.29, 4.57 - a, 1.25],
            [0.83, 0.91, 1.57, 1.25, 5.21 + a]
        ];

        containingB = [6.19 + beta, 3.21, 4.28 - beta, 6.25, 4.95 + beta];

        A = new(containingA);

        B = Matrix.CreateMatrixByColumn(containingB);
    }
}