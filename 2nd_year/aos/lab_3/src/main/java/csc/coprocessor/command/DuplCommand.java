package csc.coprocessor.command;

import csc.coprocessor.stack.CoprocessorStack;

public class DuplCommand extends ValueCommand {
    public DuplCommand() {
        super("FDUPL","### Дублюємо вершину стеку");
    }

    @Override
    public void execute(CoprocessorStack stack) {
        stack.push(stack.peek().getValue());
    }
}