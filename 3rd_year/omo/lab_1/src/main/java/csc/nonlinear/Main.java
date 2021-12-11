package csc.nonlinear;

import com.bethecoder.ascii_table.ASCIITable;

import java.util.ArrayList;
import java.util.List;
import java.util.function.BiFunction;

import static java.util.Arrays.asList;

public class Main {

    public static void main(String[] args) {
        System.out.println("Newton method");
        demo(Main::fNewton);

        System.out.println("Relaxation method");
        demo(Main::fRelaxation);
    }

    private static void demo(BiFunction<Integer, Double, Double> function) {
        String [] tableHeaders = { "Iteration", "x_n", "f(x_n)"};
        List<List<String>> data = new ArrayList<>();

        double x0 = 5.5;
        double accuracy = 0.0001;

        int prioriEstimate = getPrioriEstimate(x0, accuracy, 28, 40.75);

        int iteration = -1;
        double value;
        do {
            ++iteration;
            double x = function.apply(iteration, x0);
            value = f(x);
            data.add(asList(String.valueOf(iteration), String.valueOf(x), String.valueOf(value)));
        } while (Math.abs(value) > accuracy);

        String[][] tableData = new String[data.size()][];
        for (int i = 0; i < tableData.length; i++) {
            tableData[i] = data.get(i).toArray(new String[0]);
        }

        ASCIITable.getInstance().printTable(tableHeaders, tableData);

        System.out.println("A priori estimate: " + prioriEstimate);
        System.out.println("A posteriori estimate: " + iteration);
    }

    public static int getPrioriEstimate(double x0, double accuracy, double mLower, double mUpper) {
        double q = (mUpper - mLower) / (mLower + mUpper);
        return (int) (Math.log(Math.abs(x0)/accuracy) / Math.log(1/q)) + 1;
    }

    public static double fRelaxation(int n, double x0) {
        if (n == 0) return x0;

        double value = fRelaxation(n - 1, x0);
        return value - 2. / 51 * f(value);
    }

    public static double fNewton(int n, double x0) {
        if (n == 0) return x0;

        double value = fNewton(n - 1, x0);
        return value - f(value) / 40.75;
    }

    public static double f(double x) {
        return Math.pow(x, 3) - 3 * Math.pow(x, 2) - 17 * x + 22;
    }
}