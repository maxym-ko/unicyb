package csc.nonlinear.system;

import csc.linear.system.domain.Matrix;
import csc.linear.system.domain.Vector;
import csc.linear.system.util.MatrixUtils;

public class DotProductMethod {

    public static double findMaxEigenValue(Matrix a, Vector x0, double accuracy) {
        double lambda0 = 0;
        double lambda = Double.MAX_VALUE;
        while (Math.abs(lambda - lambda0) > accuracy) {
            Vector x1 = a.multiply(normalization(x0));
            lambda0 = lambda;
            lambda = x0.dotProduct(x1) / x0.dotProduct(x0);
            x0 = x1;
        }
        return lambda;
    }

    public static double findMinEigenValue(Matrix a, Vector x0, double accuracy) {
        double maxEigenValueForA = findMaxEigenValue(a, x0, accuracy);
        Matrix b = MatrixUtils.getIdentityMatrix(a.getRow()).multiply(maxEigenValueForA).subtract(a);

        return maxEigenValueForA - findMaxEigenValue(b, x0, accuracy);
    }

    private static Vector normalization(Vector vector) {
        double max = Double.MIN_VALUE;

        for (int i = 0; i < vector.getSize(); i++) {
            if (vector.get(i) > max) {
                max = vector.get(i);
            }
        }

        return vector.multiply(1 / max);
    }
}
