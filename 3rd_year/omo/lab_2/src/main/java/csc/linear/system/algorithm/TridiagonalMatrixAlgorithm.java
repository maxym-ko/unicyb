package csc.linear.system.algorithm;

import csc.linear.system.domain.Matrix;
import csc.linear.system.domain.Vector;
import csc.linear.system.domain.NonlinearEquation;

import java.util.*;

public class TridiagonalMatrixAlgorithm extends AbstractAlgorithm<NonlinearEquation, Matrix> {

    @Override
    public boolean checkConditions(NonlinearEquation equation) {
        Matrix matrix = equation.getMatrix();
        csc.linear.system.domain.Vector vector = equation.getVector();

        return vector.getSize() == matrix.getRow() && matrix.isQuadratic() && matrix.isTridiagonal();
    }

    @Override
    csc.linear.system.domain.Vector solve0(NonlinearEquation equation) {
        transform(equation);

        Matrix matrix = equation.getMatrix();
        csc.linear.system.domain.Vector vector = equation.getVector();
        int eqSize = matrix.getRow();

        List<Double> alphas = new ArrayList<>();
        List<Double> betas = new ArrayList<>();

        double alpha0 = matrix.get(0, 1) / matrix.get(0, 0);
        double beta0 = vector.get(0) / matrix.get(0, 0);

        alphas.add(alpha0);
        betas.add(beta0);

        for (int i = 1; i < eqSize - 1; i++) {
            double alpha = matrix.get(i, i + 1) / (matrix.get(i, i) - alpha0 * matrix.get(i, i - 1));
            alphas.add(alpha);

            double beta = (vector.get(i) + matrix.get(i, i - 1) * beta0) / (matrix.get(i, i) - alpha0 * matrix.get(i, i - 1));
            betas.add(beta);

            alpha0 = alpha;
            beta0 = beta;
        }

        List<Double> yN = new ArrayList<>();
        double y0 = (vector.get(eqSize - 1) + matrix.get(eqSize - 1, eqSize - 2) * betas.get(betas.size() - 1)) /
                    (matrix.get(eqSize - 1, eqSize - 1) - alphas.get(alphas.size() - 1) * matrix.get(eqSize - 1, eqSize - 2));
        yN.add(y0);
        for (int i = 1; i < eqSize; i++) {
            double y = alphas.get(alphas.size() - i)  * y0 + betas.get(betas.size() - i);
            yN.add(y);

            y0 = y;
        }

        Collections.reverse(yN);

        csc.linear.system.domain.Vector res = new csc.linear.system.domain.Vector(eqSize);
        for (int i = 0; i < eqSize; i++) {
            res.set(i, yN.get(i));
        }

        return res;
    }

    private void transform(NonlinearEquation equation) {
        Matrix matrix = equation.getMatrix();
        Vector vector = equation.getVector();

        int row = matrix.getRow();
        for (int i = 0; i < row; i++) {
            vector.set(i, -1 * vector.get(i));
            matrix.set(i, i, -1 * matrix.get(i, i));
        }
    }
}
