package csc.linear.system.domain;


public class NonlinearEquation {

    private final Matrix matrix;

    private final Vector vector;

    private double accuracy;

    public NonlinearEquation(Matrix matrix, Vector vector) {
        this.matrix = matrix;
        this.vector = vector;
        this.accuracy = 0;
    }

    public NonlinearEquation(Matrix matrix, Vector vector, double accuracy) {
        this.matrix = matrix;
        this.vector = vector;
        this.accuracy = accuracy;
    }

    public Matrix getMatrix() {
        return matrix;
    }

    public Vector getVector() {
        return vector;
    }

    public double getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(double accuracy) {
        this.accuracy = accuracy;
    }

    @Override
    public String toString() {
        return "Matrix:\n" + matrix + "\nVector:\n" + vector;
    }
}
