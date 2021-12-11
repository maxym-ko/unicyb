package csc.measurer;

public class IntegerMeasurer extends Measurer {
    private static long initEmpty0 = -1;

    public IntegerMeasurer() {
        super("int");
        if (initEmpty0 == -1) init();
        initEmpty = initEmpty0;
    }

    private static void init() {
        int number = 0;
        long limit = Long.MIN_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < Integer.MAX_VALUE / 30; i++) {
            if (number > limit) {
                number = Integer.MAX_VALUE;
            }
            number = i;
        }
        for (int i = 0; i < Integer.MAX_VALUE / 30 * 29; i++) {
            number = i;
        }
        long end = System.nanoTime();
        initEmpty0 = end - start;
    }

    protected long measureAddition0() {
        int delta = Integer.MAX_VALUE / 30;

        int number = 0;
        int limit = Integer.MAX_VALUE - delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number > limit) {
                number = Integer.MIN_VALUE;
            }
            number += delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureSubtraction0() {
        int delta = Integer.MAX_VALUE / 30;

        int number = 0;
        int limit = Integer.MIN_VALUE + delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < limit) {
                number = Integer.MAX_VALUE;
            }
            number -= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureMultiplication0() {
        int delta = 2;

        int number = 1;
        int limit = Integer.MAX_VALUE / delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number > limit) {
                number = 1;
            }
            number *= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureDivision0() {
        int delta = 2;

        int number = Integer.MAX_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < delta) {
                number = Integer.MAX_VALUE;
            }
            number /= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }
}
