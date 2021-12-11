package csc.nonlinear.system;

import Jama.Matrix;
import csc.linear.system.domain.Vector;
import csc.linear.system.util.MatrixUtils;
import csc.linear.system.util.VectorUtils;

public class Main {

    public static void main(String[] args) throws Exception {
        demoNewtonMethod();
        System.out.println("\n------------------------------------------------------\n");
        demoDotProductMethod();
    }

    private static void demoNewtonMethod() throws Exception {
        String f1 = "5 * x - 6 * y + 20 * LN(x) + 16";
        String f2 = "2 * x + y -10 * LN(y) - 4";
        Matrix result = NewtonMethod.solve(f1, f2, 1, 1, 0.001);

        double x = result.get(0, 0);
        double y = result.get(1, 0);

        System.out.println("The system of equations:\n" + f1 + " = 0\n" + f2 + " = 0\n");
        System.out.println("Answer vector: (" + x + "; " + y + ")");
    }

    private static void demoDotProductMethod() {
        csc.linear.system.domain.Matrix a = MatrixUtils.generateDiagonallyDominantMatrix(4, 50, true);
        Vector x0 = VectorUtils.getIdentityVector(4);

        System.out.println("Matrix:\n" + a + "\n");
        System.out.println("Max eigenvalue: " + DotProductMethod.findMaxEigenValue(a, x0, 0.001));
        System.out.println("Min eigenvalue:" + DotProductMethod.findMinEigenValue(a, x0, 0.001));
    }
}