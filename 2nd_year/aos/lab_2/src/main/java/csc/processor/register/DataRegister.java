package csc.processor.register;

public class DataRegister extends Register {
    public DataRegister(int size, String name) {
        super(name, 0, size);
    }

    @Override
    public boolean isOverflowed() {
        return getValue() > Math.pow(2, getSize()) - 1;
    }

    @Override
    public String toString() {
        return getName() + " = " + getBinaryFormatted(Integer.toBinaryString(getValue()));
    }
}
