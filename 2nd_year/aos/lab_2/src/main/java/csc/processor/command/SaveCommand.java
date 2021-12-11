package csc.processor.command;

import csc.processor.register.Register;

import java.util.Map;

public class SaveCommand extends OperandCommand {
    public SaveCommand(String name) {
        super(name);
    }

    @Override
    protected void execute0(Map<String, Register> registerMap, Register accumulator, String operand) {
        Register dataRegister = registerMap.get(operand);
        if (dataRegister == null) throw new IllegalArgumentException("Command " + getName() + " should contain integer operand");
        dataRegister.setValue(accumulator.getValue());
    }
}
