package csc;

import csc.measurer.*;

public class Main {
    private static final int NANOSECONDS_IN_SECOND = 1_000_000_000;

    public static void main(String[] args) {
        Measurer.setFreq(4);

        Measurer[] measurers = {new IntegerMeasurer(),
                new LongMeasurer(),
                new FloatMeasurer(),
                new DoubleMeasurer(),
                new CharacterMeasurer()};


        for (Measurer measurer : measurers) {
            measurer.setIter(Integer.MAX_VALUE);
            float additionPerSecond = (float) (NANOSECONDS_IN_SECOND / measurer.measureAddition());
            float subtractionPerSecond = (float) (NANOSECONDS_IN_SECOND / measurer.measureSubtraction());
            measurer.setIter(74748364);
            float multiplicationPerSecond = (float) (NANOSECONDS_IN_SECOND / measurer.measureMultiplication());
            measurer.setIter(74748364);
            float divisionPerSecond = (float) (NANOSECONDS_IN_SECOND / measurer.measureDivision());

            measurer.print(additionPerSecond, subtractionPerSecond, multiplicationPerSecond, divisionPerSecond);
        }
    }
}