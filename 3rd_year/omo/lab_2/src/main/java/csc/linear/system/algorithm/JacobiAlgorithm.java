package csc.linear.system.algorithm;

import csc.linear.system.domain.Matrix;
import csc.linear.system.function.Function;
import csc.linear.system.domain.NonlinearEquation;
import csc.linear.system.domain.Vector;

import java.util.*;

public class JacobiAlgorithm extends AbstractAlgorithm<NonlinearEquation, Matrix> {

    @Override
    public boolean checkConditions(NonlinearEquation equation) {
        Matrix matrix = equation.getMatrix();
        Vector vector = equation.getVector();

        return vector.getSize() == matrix.getRow() && matrix.isQuadratic() && matrix.isDiagonallyDominant() && matrix.canBeDiagonalized();
    }

    @Override
    Vector solve0(NonlinearEquation equation) {
        transform(equation);

        Matrix matrix = equation.getMatrix();
        Vector vector = equation.getVector();
        int eqSize = matrix.getRow();

        ArrayList<Function<Double>> functions = new ArrayList<>();
        for (int i = 0; i < eqSize; i++) {
            int diagonalIndex = i;
            Function<Double> function = args -> {
                double diagonal = matrix.get(diagonalIndex, diagonalIndex);
                double res = vector.get(diagonalIndex) / diagonal;
                for (int j = 0; j < eqSize; j++) {
                    if (j != diagonalIndex) {
                        res -= (matrix.get(diagonalIndex, j) / diagonal) * args[j];
                    }
                }
                return res;
            };
            functions.add(function);
        }

        Double[] emptyArray = new Double[matrix.getRow()];
        Arrays.fill(emptyArray, 0.0);

        double[] res = processIteration(calculateIterations(matrix, equation.getAccuracy()),
                                        functions,
                                        emptyArray);

        return new Vector(res);
    }

    private int calculateIterations(Matrix matrix, double accuracy) {
        double q = calcQ(matrix);
        return (int) (Math.log((1 - q) * accuracy) / Math.log(q)) + 1;
    }

    private double calcQ(Matrix matrix) {
        double q = 1;
        for (int i = 0; i < matrix.getRow(); i++) {
            double q0 = (absSumByRow(matrix, i) - matrix.get(i, i)) / matrix.get(i, i);
            if (q0 < q) q = q0;
        }

        return q;
    }

    private int absSumByRow(Matrix matrix, int row) {
        int res = 0;
        for (int i = 0; i < matrix.getRow(); i++) {
            res += Math.abs(matrix.get(row, i));
        }

        return res;
    }

    private double[] processIteration(int iteration, List<Function<Double>> functions, Double[] args) {
        if (iteration <= 0) {
            double[] result = new double[args.length];
            for (int i = 0; i < result.length; i++) {
                result[i] = args[i];
            }
            return result;
        }

        return processIteration(--iteration, functions, functions.stream()
                                                                 .map(function -> function.apply(args))
                                                                 .toArray(Double[]::new));
    }

    private void transform(NonlinearEquation equation) {
        equation.getMatrix().transformToDiagonal();
    }
}
