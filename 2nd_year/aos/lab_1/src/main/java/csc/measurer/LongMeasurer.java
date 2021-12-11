package csc.measurer;

public class LongMeasurer extends Measurer {
    private static long initEmpty0 = -1;

    public LongMeasurer() {
        super("long");
        if (initEmpty0 == -1) init();
        initEmpty = initEmpty0;
    }

    private static void init() {
        int number = 0;
        long limit = Long.MIN_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < Integer.MAX_VALUE / 62; i++) {
            if (number > limit) {
                number = Integer.MAX_VALUE;
            }
            number = i;
        }
        for (int i = 0; i < Integer.MAX_VALUE / 62 * 61; i++) {
            number = i;
        }
        long end = System.nanoTime();
        initEmpty0 = end - start;
    }

    protected long measureAddition0() {
        long delta = Long.MAX_VALUE / 62;

        long number = 0;
        long limit = Long.MAX_VALUE - delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number > limit) {
                number = Long.MIN_VALUE;
            }
            number += delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureSubtraction0() {
        long delta = Long.MAX_VALUE / 62;

        long number = 0;
        long limit = Long.MIN_VALUE + delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < limit) {
                number = Long.MAX_VALUE;
            }
            number -= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureMultiplication0() {
        long delta = 2;


        long number = 1;
        long limit = Long.MAX_VALUE / delta;

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
        long delta = 2;

        long number = Long.MAX_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < delta) {
                number = Long.MAX_VALUE;
            }
            number /= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }
}
