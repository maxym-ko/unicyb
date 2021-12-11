package csc.coprocessor.command;

import csc.coprocessor.register.DataRegister;
import csc.coprocessor.stack.CoprocessorStack;

public class ExchCommand extends ValueCommand {
    public ExchCommand() {
        super("FXCH ST(1)", "### Міняємо місцями два верхні значення зі стеку");
    }

    @Override
    public void execute(CoprocessorStack stack) {
        DataRegister top = stack.pop();
        DataRegister top2 = stack.pop();
        stack.push(top.getValue());
        stack.push(top2.getValue());
    }
}
