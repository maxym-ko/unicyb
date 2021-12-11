package csc.coprocessor.command;

import csc.coprocessor.register.DataRegister;
import csc.coprocessor.stack.CoprocessorStack;

public abstract class BiFuncCommand extends ValueCommand {
    public BiFuncCommand(String name, String comment) {
        super(name, comment);
    }

    @Override
    public void execute(CoprocessorStack stack) {
        DataRegister top = stack.pop();
        stack.peek().setValue(func(top.getValue(), stack.peek().getValue()));
    }

    public abstract double func(double x, double y);
}
