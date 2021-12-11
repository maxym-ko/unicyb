package csc.coprocessor.register;

import csc.coprocessor.converter.BinaryConverter;

public class DataRegister {
    private double value;
    private final BinaryConverter binaryConverter;
    private boolean isOverflowed;

    public DataRegister(double value, int characteristicCapacity, int mantissaCapacity) {
        binaryConverter = new BinaryConverter(characteristicCapacity, mantissaCapacity);
        setValue(value);
    }

    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        double tmp = value % binaryConverter.getMaxValue();
        if (value < binaryConverter.getMaxValue()) {
            isOverflowed = false;
            this.value = value;
        } else if ((int) (value / binaryConverter.getMaxValue()) % 2 == 0) {
            isOverflowed = true;
            this.value = tmp;
        } else {
            isOverflowed = true;
            this.value = -tmp;
        }
    }

    public boolean isOverflowed() {
        boolean res = isOverflowed;
        isOverflowed = false;
        return res;
    }

    @Override
    public String toString() {
        return binaryConverter.convertToIEEE754(value);
    }
}