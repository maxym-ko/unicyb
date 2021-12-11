package csc.measurer;

public class CharacterMeasurer extends Measurer {
    private static long initEmpty0 = -1;

    public CharacterMeasurer() {
        super("char");
        if (initEmpty0 == -1) init();
        initEmpty = initEmpty0;
    }

    private static void init() {
        int number = 0;
        long limit = Long.MIN_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < Integer.MAX_VALUE / 4234; i++) {
            if (number > limit) {
                number = Integer.MAX_VALUE;
            }
            number = i;
        }
        for (int i = 0; i < Integer.MAX_VALUE / 4234 * 4233; i++) {
            number = i;
        }
        long end = System.nanoTime();
        initEmpty0 = end - start;
    }

    protected long measureAddition0() {
        char delta = (char) 4234;

        char number = 0;
        char limit = (char) (Character.MAX_VALUE - delta);

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number > limit) {
                number = Character.MIN_VALUE;
            }
            number += delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureSubtraction0() {
        char delta = (char) 4234;

        char number = 0;
        char limit = (char) (Character.MIN_VALUE + delta);

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < limit) {
                number = Character.MAX_VALUE;
            }
            number -= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }

    protected long measureMultiplication0() {
        char delta = (char) 2;

        char number = 1;
        char limit = (char) (Character.MAX_VALUE / delta);

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
        char delta = (char) 2;

        char number = Character.MAX_VALUE;

        long start = System.nanoTime();
        for (int i = 0; i < getIter(); i++) {
            if (number < delta) {
                number = Character.MAX_VALUE;
            }
            number /= delta;
        }
        long end = System.nanoTime();

        return end - start;
    }
}
