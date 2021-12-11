package csc.coprocessor.command;

import csc.coprocessor.stack.CoprocessorStack;

public class LoadCommand extends OperandCommand {
    public LoadCommand(double operand) {
        super("FLD " + operand, operand,"### Встановлюємо " + operand + " на вершину стеку");
    }

    @Override
    public void execute(CoprocessorStack stack) {
        stack.push(operand);
    }
}