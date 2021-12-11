package csc.processor.command;

import csc.processor.register.Register;

public class OrCommand extends ValueCommand {
    public OrCommand(String name, int size) {
        super(name, size);
    }

    @Override
    protected void execute0(Register accumulator, int value) {
        accumulator.setValue(accumulator.getValue() | value);
    }
}
