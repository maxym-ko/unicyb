package csc.processor.register;

public class ProgramSateRegister extends SpecialPurposeRegister {
    private int isOverflow;

    public ProgramSateRegister(int size, String name) {
        super(size, name);
    }

    public int getIsOverflow() {
        return isOverflow;
    }

    public void setIsOverflow(int isOverflow) {
        this.isOverflow = isOverflow;
    }

    @Override
    public String toString() {
        return getName() + " = " + getValue() + " | " + getIsOverflow();
    }
}
