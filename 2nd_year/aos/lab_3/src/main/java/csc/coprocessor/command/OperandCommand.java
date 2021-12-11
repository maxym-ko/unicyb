package csc.coprocessor.command;

public abstract class OperandCommand extends Command {
    protected double operand;

    public OperandCommand(String name, double operand, String comment) {
        super(name, comment);
        this.operand = operand;
    }
}
