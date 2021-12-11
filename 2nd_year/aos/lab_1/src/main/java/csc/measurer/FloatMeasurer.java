package csc.measurer;

public class FloatMeasurer extends Measurer {
    private static long initEmpty0 = -1;

    public FloatMeasurer() {
        super("float");
        if (initEmpty0 == -1) init();
        initEmpty = initEmpty0;
    }

    private static void init() {
        int number = 0;
        long limit = Long.MIN_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < Integer.MAX_VALUE / 850; i++) {
            if (number > limit) {
                number = Integer.MAX_VALUE;
            }
            number = i;
        }
        for (int i = 0; i < Integer.MAX_VALUE / 850 * 849; i++) {
            number = i;
        }
        long end = System.nanoTime();
        initEmpty0 = end - start;
    }

    protected long measureAddition0() {
        float delta = Float.MAX_VALUE / 850;

        float number = 0;
        float limit = Float.MAX_VALUE - delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number > limit) {
                number = Float.MIN_VALUE;
            }
            number += delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureSubtraction0() {
        float delta = Float.MAX_VALUE / 850;

        float number = 0;
        float limit = Float.MIN_VALUE + delta;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < limit) {
                number = Float.MAX_VALUE;
            }
            number -= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureMultiplication0() {
        float delta = 1.11f;
        if (delta < 0) return -1L;

        float number = 1;
        float limit = Float.MAX_VALUE / delta;

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
        float delta = 1.11f;

        float number = Float.MAX_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < delta) {
                number = Float.MAX_VALUE;
            }
            number /= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }
}
