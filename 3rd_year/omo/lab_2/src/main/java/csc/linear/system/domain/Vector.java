package csc.linear.system.domain;

public class Vector {

    private final Matrix vector;

    public Vector(double[] vector) {
        double[][] matrix = new double[vector.length][1];
        for (int i = 0; i < vector.length; i++) {
            matrix[i][0] = vector[i];
        }
        this.vector = new Matrix(matrix);
    }

    public Vector(double[][] vector) {
        if (vector == null || vector.length == 0 || vector[0].length != 1) {
            throw new IllegalArgumentException("The vector cannot be null or have more than 1 row");
        }
        this.vector = new Matrix(vector);
    }

    public Vector(int size) {
        this.vector = new Matrix(size, 1);
    }

    public Vector multiply(double num) {
        for (int i = 0; i < getSize(); i++) {
            set(i, get(i) * num);
        }

        return this;
    }

    public double dotProduct(Vector vector) {
        if (vector.getSize() != this.getSize()) {
            throw new IllegalArgumentException("Both vector must have the same size");
        }

        double res = 0;
        for (int i = 0; i < vector.getSize(); i++) {
            res += this.get(i) * vector.get(i);
        }

        return res;
    }

    public double get(int row) {
        return vector.get(row, 0);
    }

    public void set(int row, double value) {
        vector.set(row, 0, value);
    }

    public int getSize() {
        return vector.getRow();
    }

    @Override
    public String toString() {
        return vector.toString();
    }
}
