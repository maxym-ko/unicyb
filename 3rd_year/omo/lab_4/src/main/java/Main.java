import csc.linear.system.algorithm.TridiagonalMatrixAlgorithm;
import csc.linear.system.domain.Matrix;
import csc.linear.system.domain.NonlinearEquation;
import csc.linear.system.domain.Vector;

import java.util.*;

public class Main {

    private final static int NODES_NUMBER = 7;

    public static void main(String[] args) {
        System.out.println("SPLINE:");
        demoSpline();

        System.out.println("\nLAGRANGE WITH CHEBYSHOV ZEROS:");
        demoLagrange(chebyshevZeros(NODES_NUMBER));

        System.out.println("\nLAGRANGE WITH EQUIDISTANT POINTS:");
        demoLagrange(equidistantPoints(-5, 5));
    }

    public static void demoSpline() {
        TridiagonalMatrixAlgorithm algorithm = new TridiagonalMatrixAlgorithm();

        // left-hand side
        double[][] lhs = new double[NODES_NUMBER][];
        for (int i = 0; i < lhs.length; i++) {
            lhs[i] = new double[lhs.length];
            for (int j = 0; j < lhs.length; j++) {
                lhs[i][j] = 0;
            }
        }

        double[] hs = findHs();
        for (int i = 1; i < NODES_NUMBER - 1; i++) {
            lhs[i][i - 1] = hs[i] / 6;
            lhs[i][i]  = (hs[i] + hs[i + 1]) / 3;
            lhs[i][i + 1] = hs[i + 1] / 6;
        }
        lhs[0][0] = 1;
        lhs[1][0] = 0;
        lhs[lhs.length - 2][lhs.length - 1] = 0;
        lhs[lhs.length - 1][lhs.length - 1] = 1;

        // right-hand side
        double[] rhs = new double[NODES_NUMBER];

        double[] nodes = chebyshevZeros(NODES_NUMBER + 1);
        double[] fs = Arrays.stream(nodes).map(Main::f).toArray();
        for (int i = 1; i < NODES_NUMBER - 1; i++) {
            rhs[i] = (fs[i + 1] - fs[i]) / hs[i] - (fs[i] - fs[i - 1]) / hs[i];
        }

        Matrix matrix = new Matrix(lhs);
        Vector vector = new Vector(rhs);

        NonlinearEquation nonlinearEquation = new NonlinearEquation(matrix, vector);

        Vector ms = algorithm.solve(nonlinearEquation);

        double[][] result = new double[NODES_NUMBER - 1][];
        for (int i = 0; i < result.length; i++) {
            result[i] = new double[4];
            for (int j = 0; j < 4; j++) {
                result[i][j] = 0;
            }
        }
        for (int i = 1; i < NODES_NUMBER; i++) {
            result[i - 1][0] = ms.get(i - 1) / (6 * hs[i]);
            result[i - 1][1] = ms.get(i) / (6 * hs[i]);
            result[i - 1][2] = (fs[i - 1] - ms.get(i - 1) * Math.pow(hs[i], 2) / 6) / hs[i];
            result[i - 1][3] = (fs[i] - ms.get(i) * Math.pow(hs[i], 2) / 6) / hs[i];
        }

        for (int i = 1; i < result.length + 1; i++) {
            System.out.println(result[i - 1][0] + "(" + nodes[i] + " - x)^3 + " +
                               result[i - 1][1] + "(x - " + nodes[i - 1] + ")^3 + " +
                               result[i - 1][2] + "(" + nodes[i] + " - x) + " +
                               result[i - 1][3] + "(x - " + nodes[i - 1] + "), x is [" + nodes[i - 1] + ", " + nodes[i] + "]");
        }
    }

    public static void demoLagrange(double[] nodes) {
        double[] fs = Arrays.stream(nodes).map(Main::f).toArray();
        double[] results = new double[NODES_NUMBER];
        for (int i = 0; i < results.length; i++) {
            double product = 1;
            for (int j = 0; j < results.length; j++) {
                if (i != j) {
                    product *= (nodes[i] - nodes[j]);
                }
            }
            results[i] = fs[i] / product;
        }

        for (int i = 0; i < results.length; i++) {
            String product = "";
            for (int j = 0; j < results.length; j++) {
                if (i != j) {
                    product += "(x - " + nodes[j] + ")";
                }
            }
            System.out.println(results[i] + product + "+");
        }
    }

    private static double f(double x) {
        return x / 38;
    }

    private static double[] findHs() {
        double[] nodes = chebyshevZeros(NODES_NUMBER + 1);
        double[] hs = new double[nodes.length];
        for (int i = 1; i < nodes.length; i++) {
            hs[i] = nodes[i]  - nodes[i - 1];
        }

        return hs;
    }

    private static double[] chebyshevZeros(int n) {
        double[] res = new double[n];
        for (int i = 0; i < n; i++) {
            res[i] = (Math.cos(2 * (i + 1) - 1) * Math.PI) / 2 * (n);
        }

        Arrays.sort(res);

        return res;
    }

    private static double[] equidistantPoints(double a, double b) {
        double h = (b - a) / (NODES_NUMBER - 1);
        double[] res = new double[NODES_NUMBER];
        double tmp = a;
        for (int i = 0; i < NODES_NUMBER; i++) {
            res[i] = tmp;
            tmp += h;
        }

        return res;
    }
}
