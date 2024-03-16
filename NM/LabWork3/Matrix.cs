using System.Text;

namespace LabWork3;

public class Matrix
{
    public List<List<double>> Containing { get; set; }
    
    public List<double> this[int i]
    {
        get => Containing[i];
        set => Containing[i] = value;
    }

    public double this[int i, int j]
    {
        get => Containing[i][j];
        set => Containing[i][j] = value;
    }

    public int NumberOfRows => Containing.Count;
    
    public int NumberOfColumns => Containing[0].Count;

    public Matrix(List<List<double>> containing)
    {
        Containing = containing;
    }


    public Matrix(int rows, int columns)
    {
        Containing = new List<List<double>>();
        for (int i = 0; i < rows; i++)
        {
            Containing.Add(new List<double>());
            for (int j = 0; j < columns; j++)
            {
                Containing[i].Add(0);
            }
        }
    }


    public Matrix(List<double> cont)
    {
        Containing = [cont];
    }


    public static Matrix CreateMatrixByColumn(List<double> col)
    {
        Matrix matrix = new (col);
        matrix.Transpose();
        return matrix;
    }


    public static Matrix CreateZeroMatrix(int rows, int columns)
    {
        List<List<double>> cont = [];
        
        for (int i = 0; i < rows; i++)
        {
            List<double> row = [];
            
            for (int j = 0; j < columns; j++)
            {
                row.Add(0);
            }
            
            cont.Add(row);
        }
        
        return new Matrix(cont);
    }


    public void Transpose()
    {
        var transposed = new List<List<double>>();

        for (int j = 0; j < Containing[0].Count; j++)
        {
            List<double> row = [];

            for (int i = 0; i < Containing.Count; i++)
            {
                row.Add(Containing[i][j]);
            }

            transposed.Add(row);
        }

        Containing = transposed;

    }
    
    
    public void Print()
    {
        foreach (var row in Containing)
        {
            foreach (var e in row)
            {
                Console.Write(e + "\t ");
            }
            Console.Write("\n");
        }
    }


    public void PrintInOneLine()
    {
        foreach (var row in Containing)
        {
            foreach (var e in row)
            {
                Console.Write(e + "\t ");
            }
        }
        Console.Write("\n");
    }


    public List<double> GetColumn(int i) => Containing.Select(row => row[i]).ToList();


    public Matrix Copy() => new (
        Containing.Select(row => new List<double>(row)).ToList());
    

    public static Matrix operator *(Matrix A, Matrix B)
    {
        List<List<double>> cont = [];

        foreach (List<double> rowA in A.Containing)
        {
            List<double> row = [];

            Matrix BCopied = B.Copy();
            BCopied.Transpose(); // for easier getting a columns as a row in transposed matrix

            foreach (var column in BCopied.Containing)
            {
                row.Add(VectorMultiplying(column, rowA));
            }

            cont.Add(row);
        }
        
        return new Matrix(cont);
    }


    public static Matrix operator -(Matrix A, Matrix B)
    {
        Matrix res = A.Copy();

        for(int i = 0; i < A.NumberOfRows; i++)
        {

            for(int j = 0; j < A.NumberOfColumns; j++)
            {
                res[i][j] -= B[i][j];
            }
        }

        return res;
    }
    
    
    public static Matrix operator +(Matrix A, Matrix B)
    {
        Matrix res = A.Copy();

        for(int i = 0; i < A.NumberOfRows; i++)
        {

            for(int j = 0; j < A.NumberOfColumns; j++)
            {
                res[i][j] += B[i][j];
            }
        }

        return res;
    }


    private static double VectorMultiplying(IReadOnlyList<double> A, IReadOnlyList<double> B)
    {
        if (A.Count != B.Count)
            throw new Exception("Length must be the same");
        
        return A.Select((t, i) => t * B[i]).Sum();
    }


    public override string ToString()
    {
        StringBuilder result = new ();

        foreach (var row in Containing)
        {
            foreach (var e in row)
            {
                result.Append(e);
                result.Append("\t ");
            }
            result.AppendLine();
        }

        return result.ToString();
    }
    
    
    public List<double> GetAllNumbersInLine()
    {
        List<double> res = [];

        foreach(var row in Containing)
        {
            res.AddRange(row);
        }

        return res;
    }
    
}