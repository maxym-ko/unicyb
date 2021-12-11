package csc.nonlinear.system;

import Jama.Matrix;
import javacalculus.core.CALC;
import javacalculus.core.CalcParser;
import javacalculus.evaluator.CalcSUB;
import javacalculus.struct.CalcDouble;
import javacalculus.struct.CalcInteger;
import javacalculus.struct.CalcObject;
import javacalculus.struct.CalcSymbol;

public class NewtonMethod {

    public static Matrix solve(String function1, String function2, double x0, double y0, double accuracy) throws Exception {

        double z1 = Double.MAX_VALUE; // z_1
        double z2 = Double.MAX_VALUE; // z_2

        while (Math.min(Math.abs(z1), Math.abs(z2)) > accuracy) {
            double f1DiffX = partialDerivative(function1, "x", x0, y0); // A_1_1
            double f1DiffY = partialDerivative(function1, "y", x0, y0); // A_1_2
            double f2DiffX = partialDerivative(function2, "x", x0, y0); // A_2_1
            double f2DiffY = partialDerivative(function2, "y", x0, y0); // A_2_2

            double f1 = calculateAtPoint(function1, x0, y0); // F_1
            double f2 = calculateAtPoint(function2, x0, y0); // F_2

            double[][] lhsArray = {{f1DiffX, f1DiffY},
                                   {f2DiffX, f2DiffY}};
            double[] rhsArray = {f1, f2};
            Matrix lhs = new Matrix(lhsArray);
            Matrix rhs = new Matrix(rhsArray, 2);
            Matrix answer = lhs.solve(rhs);

            z1 = answer.get(0, 0);
            z2 = answer.get(1, 0);

            x0 -= z1;
            y0 -= z2;
        }

        return Matrix.constructWithCopy(new double[][]{{x0}, {y0}});
    }

    private static double partialDerivative(String function, String variable, double x0, double y0) throws Exception {
        return calculateAtPoint("DIFF(" + function + ", " + variable + ")", x0, y0);
    }

    private static double calculateAtPoint(String command, double x0, double y0) throws Exception {
        CalcParser parser = new CalcParser();
        CalcObject parsed = parser.parse(command);
        CalcObject result = parsed.evaluate();

        result = subst(result, "x", x0);
        result = subst(result, "y", y0);
        result = CALC.SYM_EVAL(result);

        return (result instanceof CalcInteger) ? ((CalcInteger) result).intValue()
                                               : ((CalcDouble) result).doubleValue();
    }

    private static CalcObject subst(CalcObject input, String variable, double number) {
        CalcSymbol symbol = new CalcSymbol(variable);
        CalcDouble value = new CalcDouble(number);
        return CalcSUB.numericSubstitute(input, symbol, value);
    }
}
