package csc.processor.register;

public class InstructionRegister extends Register implements RollBackable {
    private String command;
    private String operand;
    private String commitValue;

    public InstructionRegister(int size, String name) {
        super(name, 0, size);
    }

    @Override
    public void commit() {
        commitValue = operand == null ? "0" : operand;
    }

    @Override
    public void rollback() {
        setOperand(commitValue);
    }

    public String getCommand() {
        return command;
    }

    public void setCommand(String command) {
        this.command = command;
    }

    public String getOperand() {
        return operand;
    }

    public void setOperand(String operand) {
        this.operand = operand;
    }

    @Override
    public String toString() {
        try {
            operand = getBinaryFormatted(Integer.toBinaryString(Integer.parseInt(operand)));
        } catch (NumberFormatException e) {
            operand = getOperand();
        }
        return getName() + " = " + getCommand() + " | " + operand;
    }

    @Override
    public boolean isOverflowed() {
        int value;
        try {
            value = Integer.parseInt(operand);
        } catch (Exception e) {
            value = -1;
        }
        return value > Math.pow(2, getSize()) - 1;
    }
}
