package csc.linear.system.util;

import csc.linear.system.domain.Matrix;

public class MatrixUtils {

    public static Matrix generateTridiagonalMatrix(int size, double max, boolean castToInt) {
        return new Matrix(generateTridiagonalMatrixArray(size, max, castToInt));
    }

    public static Matrix generateDiagonallyDominantMatrix(int size, double max, boolean castToInt) {
        double[][] matrix = new double[size][size];
        for (int i = 0; i < size; i++) {
            matrix[i] = new double[size];
            for (int j = 0; j < size; j++) {
                matrix[i][j] = castToInt ? (int) (Math.random() * max + 1) : (Math.random() * max);
            }
        }

        domanateMatrix(size, max, matrix);

        return new Matrix(matrix);
    }

    public static Matrix generateTridiagonalDominantMatrix(int size, double max, boolean castToInt) {
        double[][] matrix = generateTridiagonalMatrixArray(size, max, castToInt);

        domanateMatrix(size, max, matrix);

        return new Matrix(matrix);
    }

    public static Matrix getIdentityMatrix(int size) {
        double[][] matrix = new double[size][size];

        for (int i = 0; i < size; i++) {
            matrix[i] = new double[size];
            matrix[i][i] = 1;
        }

        return new Matrix(matrix);
    }

    private static double[][] generateTridiagonalMatrixArray(int size, double max, boolean castToInt) {
        double[][] matrix = new double[size][size];
        for (int i = 0; i < size; i++) {
            matrix[i] = new double[size];
        }
        for (int i = 0; i < size - 1; i++) {
            matrix[i][i] = castToInt ? (int) (Math.random() * max + 1) : (Math.random() * max);
            matrix[i][i + 1] = castToInt ? (int) (Math.random() * max + 1) : (Math.random() * max);
            matrix[i + 1][i] = castToInt ? (int) (Math.random() * max + 1) : (Math.random() * max);
        }
        matrix[size - 1][size - 1] = castToInt ? (int) (Math.random() * max + 1) : (Math.random() * max);
        return matrix;
    }

    private static void domanateMatrix(int size, double max, double[][] matrix) {
        for (int i = 0; i < size; i++) {
            matrix[i][i] = (absSumByRow(matrix, i) - matrix[i][i]) * ((int) (Math.random() * max + 1));
        }
    }

    private static int absSumByRow(double[][] matrix, int row) {
        int res = 0;
        for (int i = 0; i < matrix.length; i++) {
            res += Math.abs(matrix[row][i]);
        }

        return res;
    }

}
