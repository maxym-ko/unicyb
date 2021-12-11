package csc.coprocessor.converter;

public class BinaryConverter {
    private final int characteristicCapacity;
    private final int mantissaCapacity;
    private final double maxValue;
    private final double minValue;
    private final String zero;
    private final String positiveInfinity;
    private final String negativeInfinity;

    public BinaryConverter(int characteristicCapacity, int mantissaCapacity) {
        this.characteristicCapacity = characteristicCapacity;
        this.mantissaCapacity = mantissaCapacity;
        maxValue = Math.pow(2, Math.pow(2, characteristicCapacity) - Math.pow(2, characteristicCapacity - 1));
        minValue = -maxValue;
        zero = getZeo();
        positiveInfinity = getPositiveInfinity();
        negativeInfinity = getNegativeInfinity();
    }

    public String convertToIEEE754(double x) {
        if (x == 0) return zero;
        if (x > maxValue) return positiveInfinity;
        if (x < minValue) return negativeInfinity;

        // calc sign bit
        String signBit = "0";
        if (x < 0) {
            signBit = "1";
        }

        // calc characteristic bits
        long k = (long) Math.ceil(Math.log(1. / Math.abs(x)) / Math.log(2));
        long bias = (long) Math.pow(2, characteristicCapacity - 1) - 1;
        long characteristic = bias - k > 0 ? bias - k : 0;

        String characteristicBits =
                String.format("%0" + characteristicCapacity + "d", Long.parseLong(Long.toBinaryString(characteristic)));

        double m = Math.abs(x) * Math.pow(2, k);
        double mantissa = m - 1;
        String mantissaBits = binaryOfFraction(mantissa, mantissaCapacity);

        return Math.abs(k) < bias  * 2 ? signBit + " " + characteristicBits + " " + mantissaBits : getAbsMin();
    }

    private String binaryOfFraction(double x, int accuracy) {
        StringBuilder res = new StringBuilder();

        int integralPart = (int) x;
        double fractionalPart = x - integralPart;
        for (int i = 0; i < accuracy; i++) {
            x = fractionalPart * 2;
            integralPart = (int) (x);
            res.append(integralPart);
            fractionalPart = x - integralPart;
        }

        return res.toString();
    }

    public String getZeo() {
        if (zero != null) return zero;
        StringBuilder res = new StringBuilder("0 ");
        for (int i = 0; i < characteristicCapacity; i++) {
            res.append('0');
        }
        res.append(" ");
        for (int i = 0; i < mantissaCapacity; i++) {
            res.append('0');
        }

        return res.toString();
    }

    public String getPositiveInfinity() {
        return positiveInfinity == null ? "0 " + getInfinityBinary() : positiveInfinity;
    }

    public String getNegativeInfinity() {
        return negativeInfinity == null ? "1 " + getInfinityBinary() : negativeInfinity;
    }

    private String getInfinityBinary() {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < characteristicCapacity; i++) {
            res.append('1');
        }
        res.append(" ");
        for (int i = 0; i < mantissaCapacity; i++) {
            res.append('0');
        }

        return res.toString();
    }

    public String getNan() {
        StringBuilder res = new StringBuilder("1 ");
        for (int i = 0; i < characteristicCapacity; i++) {
            res.append('1');
        }
        res.append(" ");
        for (int i = 0; i < mantissaCapacity - 1; i++) {
            res.append('0');
        }
        res.append('1');

        return res.toString();
    }

    public String getMax() {
        StringBuilder res = new StringBuilder("0 ");
        for (int i = 0; i < characteristicCapacity - 1; i++) {
            res.append('1');
        }
        res.append('0');
        res.append(" ");
        for (int i = 0; i < mantissaCapacity; i++) {
            res.append('1');
        }

        return res.toString();
    }

    public String getMin() {
        return "1" + getMax().substring(1);
    }

    public String getAbsMin() {
        return getZeo().substring(0, getZeo().length() - 1) + "1";
    }

    public int getCharacteristicCapacity() {
        return characteristicCapacity;
    }

    public int getMantissaCapacity() {
        return mantissaCapacity;
    }

    public double getMaxValue() {
        return maxValue;
    }

    public double getMinValue() {
        return minValue;
    }
}
