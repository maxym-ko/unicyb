package csc.coprocessor.register;

public class ProgramStateRegister {
    private boolean overflowed;
    private boolean isLastCommandPositive;

    public void setOverflowed(boolean overflowed) {
        this.overflowed = overflowed;
    }

    public void setLastCommandPositive(boolean positive) {
        this.isLastCommandPositive = positive;
    }

    @Override
    public String toString() {
        return "PS  =  " + (isLastCommandPositive ? "0" : "1") + " | " + (overflowed ? "1" : "0");
    }
}
