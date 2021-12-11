package csc.measurer;

public abstract class Measurer {
    protected long initEmpty;
    protected long empty;
    private int iter;
    private static int freq;
    private final String type;

//    static {
//        int number = 0;
//
//        long start = System.nanoTime();
//        for (int i = 0; i < Integer.MAX_VALUE; i++) {
//            if (number > i) {
////                number = Integer.MIN_VALUE;
//            }
////            number = i;
//        }
//        long end = System.nanoTime();
//
//        INIT_EMPTY = end - start;
//    }

    public Measurer(String type) {
        this.type = type;
    }

    abstract long measureAddition0();

    abstract long measureSubtraction0();

    abstract long measureMultiplication0();

    abstract long measureDivision0();

    public double measureAddition() {
        return ((double) (measureAddition0() - empty)) / iter;
    }

    public double measureSubtraction() {
        return ((double) (measureSubtraction0() - empty)) / iter;
    }

    public double measureMultiplication() {
        return ((double) (measureMultiplication0() - empty)) / iter;
    }

    public double measureDivision() {
        return ((double) (measureDivision0() - empty)) / iter;
    }

    public void updateEmpty() {
        empty = (int) (1.0 * iter / Integer.MAX_VALUE * initEmpty);
    }

    public void print(float additionPerSecond, float subtractionPerSecond, float multiplicationPerSecond, float divisionPerSecond) {
        int additionPerformance = calcPerformance(additionPerSecond);
        int subtractionPerformance = calcPerformance(subtractionPerSecond);
        int multiplicationPerformance = calcPerformance(multiplicationPerSecond);
        int divisionPerformance = calcPerformance(divisionPerSecond);

        String format = "%s%8s\t\t%e\t%-50s%d\n";
        String res = "";
        res += String.format(format, "+", getType(), additionPerSecond, getDiagram(additionPerformance), additionPerformance);
        res += String.format(format, "-", getType(), subtractionPerSecond, getDiagram(subtractionPerformance), subtractionPerformance);
        res += String.format(format, "*", getType(), multiplicationPerSecond, getDiagram(multiplicationPerformance), multiplicationPerformance);
        res += String.format(format, "/", getType(), divisionPerSecond, getDiagram(divisionPerformance), divisionPerformance);

        System.out.println(res);
    }

    private int calcPerformance(float operationPerSecond) {
        return (int) (operationPerSecond / (freq * Math.pow(10, 7)));
    }

    private String getDiagram(int percent) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < percent / 2; i++) {
            res.append('X');
        }
        for (int i = percent / 2; i < 50; i++) {
            res.append(' ');
        }
        res.append('\t');
        return res.toString();
    }

    public String getType() {
        return type;
    }

    public int getIter() {
        return iter;
    }

    public long getEmpty() {
        return empty;
    }

    public void setIter(int iter) {
        this.iter = iter;
        updateEmpty();
    }

    public static void setFreq(int freq) {
        Measurer.freq = freq;
    }
}
