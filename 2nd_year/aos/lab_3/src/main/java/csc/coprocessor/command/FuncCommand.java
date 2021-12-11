package csc.coprocessor.command;

import csc.coprocessor.register.DataRegister;
import csc.coprocessor.stack.CoprocessorStack;

public abstract class FuncCommand extends ValueCommand {
    public FuncCommand(String name, String comment) {
        super(name, comment);
    }

    @Override
    public void execute(CoprocessorStack stack) {
        stack.peek().setValue(func(stack.peek().getValue()));
    }

    public abstract double func(double x);
}
