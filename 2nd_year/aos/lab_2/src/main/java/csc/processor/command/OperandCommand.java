package csc.processor.command;

import csc.processor.register.Register;

import java.util.Map;

public abstract class OperandCommand implements Command {
    private final String name;
    OperandCommand(String name) {
        this.name = name;
    }

    @Override
    public void execute(String operand, Map<String, Register> registerMap) {
        Register accumulator = registerMap.get("A");
        execute0(registerMap, accumulator, operand);

        Register programSate = registerMap.get("PS");
        programSate.setValue(accumulator.getSign());
    }

    protected abstract void execute0(Map<String, Register> registerMap, Register accumulator, String operand);

    public String getName() {
        return name;
    }
}
