package csc.coprocessor.command;

import csc.coprocessor.stack.CoprocessorStack;

public abstract class Command {
    private final String name;
    private final String comment;

    public Command(String name, String comment) {
        this.name = name;
        this.comment = comment;
    }

    public abstract void execute(CoprocessorStack stack);

    @Override
    public String toString() {
        return "command = " + name + "\t\t" + comment;
    }
}
