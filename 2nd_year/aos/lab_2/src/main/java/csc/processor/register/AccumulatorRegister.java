package csc.processor.register;

public class AccumulatorRegister extends DataRegister implements RollBackable {
    private int commitValue;

    public AccumulatorRegister(int size, String name) {
        super(size, name);
    }

    @Override
    public void commit() {
        commitValue = getValue();
    }

    @Override
    public void rollback() {
        setValue(commitValue);
    }

    @Override
    public String toString() {
        return super.toString();
    }
}
