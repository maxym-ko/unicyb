package csc.measurer;

public class DoubleMeasurer extends Measurer {
    private static long initEmpty0 = -1;

    public DoubleMeasurer() {
        super("double");
        if (initEmpty0 == -1) init();
        initEmpty = initEmpty0;
    }

    private static void init() {
        int number = 0;
        long limit = Long.MIN_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < Integer.MAX_VALUE / 6801; i++) {
            if (number > limit) {
                number = Integer.MAX_VALUE;
            }
            number = i;
        }
        for (int i = 0; i < Integer.MAX_VALUE / 6801 * 6800; i++) {
            number = i;
        }
        long end = System.nanoTime();
        initEmpty0 = end - start;
    }

    protected long measureAddition0() {
        double delta = Double.MAX_VALUE / 6801;

        double number = 0;
        double limit = Double.MAX_VALUE - delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number > limit) {
                number = Double.MIN_VALUE;
            }
            number += delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureSubtraction0() {
        double delta = Double.MAX_VALUE / 6801;

        double number = 0;
        double limit = Double.MIN_VALUE + delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < limit) {
                number = Double.MAX_VALUE;
            }
            number -= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureMultiplication0() {
        double delta = 1.11;

        double number = 1;
        double limit = Double.MAX_VALUE / delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number> limit) {
                number = 1;
            }
            number *= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureDivision0() {
        double delta = 1.11;

        double number = Double.MAX_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < delta) {
                number = Double.MAX_VALUE;
            }
            number /= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }
}
