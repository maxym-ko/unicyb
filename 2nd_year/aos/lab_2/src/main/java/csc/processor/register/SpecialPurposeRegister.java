package csc.processor.register;

public class SpecialPurposeRegister extends Register {
    public SpecialPurposeRegister(int size, String name) {
        super(name, 0, size);
    }

    public SpecialPurposeRegister(int size, String name, int value) {
        super(name, value, size);
    }

    @Override
    public String toString() {
        return getName() + " = " + getValue();
    }

    @Override
    public boolean isOverflowed() {
        return false;
    }
}
