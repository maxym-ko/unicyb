package csc.processor.command;

import csc.processor.register.Register;

public class MoveCommand extends ValueCommand {
    public MoveCommand(String name, int size) {
        super(name, size);
    }

    @Override
    protected void execute0(Register accumulator, int value) {
        accumulator.setValue(value);
    }
}
