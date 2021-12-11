package csc.linear.system;

import csc.linear.system.algorithm.JacobiAlgorithm;
import csc.linear.system.algorithm.TridiagonalMatrixAlgorithm;
import csc.linear.system.domain.Matrix;
import csc.linear.system.domain.Vector;
import csc.linear.system.domain.NonlinearEquation;
import csc.linear.system.util.MatrixUtils;
import csc.linear.system.util.VectorUtils;

public class Main {

    public static void main(String[] args) {
        NonlinearEquation nonlinearEquation = new NonlinearEquation(
            MatrixUtils.generateTridiagonalDominantMatrix(4, 50, true),
            VectorUtils.generateVector(4, 50, true),
            0.001);
        System.out.println(nonlinearEquation);

        TridiagonalMatrixAlgorithm tridiagonalMatrixAlgorithm = new TridiagonalMatrixAlgorithm();
        JacobiAlgorithm jacobiAlgorithm = new JacobiAlgorithm();

        Vector solveVector = tridiagonalMatrixAlgorithm.solve(nonlinearEquation);
        Vector solveVector2 = jacobiAlgorithm.solve(nonlinearEquation);

        System.out.println("\nResult [TridiagonalMatrixAlgorithm]:\n" + solveVector);
        System.out.println("\nResult [JacobiAlgorithm]:\n" + solveVector2);
    }

    public static void demoTridiagonalMatrixAlgorithmExample() {
        Matrix matrix = new Matrix(new double[][]{{1, -1, 0, 0, 0},
                                                  {-1, 2, -1, 0, 0},
                                                  {0, -1, 2, -1, 0},
                                                  {0, 0, -1, 2, -1},
                                                  {0, 0, 0, -1, 2}});
        Vector vector = new Vector(new double[][]{{1},
                                                  {-2},
                                                  {-3},
                                                  {-4},
                                                  {3}});
        NonlinearEquation nonlinearEquation = new NonlinearEquation(matrix, vector);
        TridiagonalMatrixAlgorithm tridiagonalMatrixAlgorithm = new TridiagonalMatrixAlgorithm();
        Vector solveVector = tridiagonalMatrixAlgorithm.solve(nonlinearEquation);
        System.out.println("\nResult [TridiagonalMatrixAlgorithm]:\n" + solveVector);
    }

    public static void demoJacobiAlgorithmExample() {
        Matrix matrix = new Matrix(new double[][]{{3, -1,  1},
                                                  {-1, 2, 0.5},
                                                  {1, 0.5, 3}});
        Vector vector = new Vector(new double[][]{{1},
                                                  {1.75},
                                                  {2.5}});
        NonlinearEquation nonlinearEquation = new NonlinearEquation(matrix, vector,0.01);
        TridiagonalMatrixAlgorithm tridiagonalMatrixAlgorithm = new TridiagonalMatrixAlgorithm();
        Vector solveVector = tridiagonalMatrixAlgorithm.solve(nonlinearEquation);
        System.out.println("\nResult [TridiagonalMatrixAlgorithm]:\n" + solveVector);
    }

}
