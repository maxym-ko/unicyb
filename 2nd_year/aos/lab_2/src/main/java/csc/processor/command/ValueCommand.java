package csc.processor.command;

import csc.processor.register.AccumulatorRegister;
import csc.processor.register.ProgramSateRegister;
import csc.processor.register.Register;

import java.util.Map;

public abstract class ValueCommand implements Command {
    private final String name;
    private final int size;

    ValueCommand(String name, int size) {
        this.name = name;
        this.size = size;
    }

    @Override
    public void execute(String operand, Map<String, Register> registerMap) {
        AccumulatorRegister accumulator = (AccumulatorRegister) registerMap.get("A");
        int value;
        try {
            value = Integer.parseInt(operand);
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Command '" + name + "' should contain integer operand");
        }

        accumulator.commit();
        execute0(accumulator, value);

        if (accumulator.isOverflowed()) {
            ((ProgramSateRegister) registerMap.get("PS")).setIsOverflow(1);
            accumulator.rollback();
        }

        Register programSate = registerMap.get("PS");
        programSate.setValue(accumulator.getSign());
    }

    protected abstract void execute0(Register accumulator, int value);

    public String getName() {
        return name;
    }
}
