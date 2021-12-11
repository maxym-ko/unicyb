package csc.linear.system.domain;

import java.util.*;

public class Matrix {

    private final int row;

    private final int column;

    private final double[][] matrix;

    public Matrix(double[][] matrix) {
        if (matrix == null || matrix.length == 0) {
            throw new IllegalArgumentException("The matrix cannot be null or have 0 size");
        }
        this.row = matrix.length;
        this.column = matrix[0].length;
        this.matrix = matrix;
    }

    public Matrix(int size) {
        this.row = size;
        this.column = size;
        this.matrix = new double[size][size];
    }

    public Matrix(int row, int column) {
        this.row = row;
        this.column = column;
        this.matrix = new double[row][column];
    }

    public double get(int row, int column) {
        return matrix[row][column];
    }

    public void set(int row, int column, double value) {
        matrix[row][column] = value;
    }

    public boolean isQuadratic() {
        return row == column;
    }

    public boolean isTridiagonal() {
        double [][] matrixClone = new double[row][column];
        for(int i = 0; i < matrix.length; i++) {
            matrixClone[i] = matrix[i].clone();
        }

        for (int i = 0; i < row - 1; i++) {
            matrixClone[i][i] = 0;
            matrixClone[i][i + 1] = 0;
            matrixClone[i + 1][i] = 0;
        }

        if (matrixClone[row - 1][row - 1] == 0) {
            return false;
        }
        matrixClone[row - 1][row - 1] = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (matrixClone[i][j] != 0) {
                    return false;
                }
            }
        }

        return true;
    }

    public boolean isDiagonallyDominant() {
        for (int i = 0; i < row; i++) {
            if (matrix[i][i] < absSumByRow(i) - matrix[i][i]) {
                return false;
            }
        }

        return true;
    }

    public boolean canBeDiagonalized() {
        if (!isQuadratic()) {
            return false;
        }

        for (int i = 0; i < column; i++) {
            if (countColumnPositiveNumbers(i) == 0) {
                return false;
            }
        }

        for (int i = 0; i < row; i++) {
            if (countRawPositiveNumbers(i) == 0) {
                return false;
            }
        }

        return true;
    }

    private int countColumnPositiveNumbers(int column) {
        int res = 0;
        for (int i = 0; i < row; i++) {
            res += matrix[i][column] != 0 ? 1 : 0;
        }

        return res;
    }

    private int countRawPositiveNumbers(int raw) {
        int res = 0;
        for (int i = 0; i < column; i++) {
            res += matrix[raw][i] != 0 ? 1 : 0;
        }

        return res;
    }

    private int absSumByRow(int row) {
        int res = 0;
        for (int i = 0; i < row; i++) {
            res += Math.abs(matrix[row][i]);
        }

        return res;
    }

    public void transformToDiagonal() {
         // To be implemented
    }

    public Matrix subtract(Matrix m) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                matrix[i][j] -= m.get(i, j);
            }
        }

        return this;
    }

    public Matrix multiply(double num) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                matrix[i][j] *= num;
            }
        }

        return this;
    }

    public Vector multiply(Vector vector) {
        if (row != vector.getSize()) {
            throw new IllegalArgumentException("The number of matrix's row should equal the Vector size");
        }

        double[][] resultVector = new double[vector.getSize()][1];
        for (int i = 0; i < row; i++) {
            resultVector[i] = new double[1];
            for (int j = 0; j < column; j++) {
                resultVector[i][0] += matrix[i][j] * vector.get(j);
            }
        }

        return new Vector(resultVector);
    }

    public int getRow() {
        return row;
    }

    public int getColumn() {
        return column;
    }

    @Override
    public String toString() {
        return Arrays.deepToString(matrix).replace(", [", ",\n [");
    }
}
