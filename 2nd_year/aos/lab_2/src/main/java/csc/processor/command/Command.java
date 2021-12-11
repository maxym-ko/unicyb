package csc.processor.command;

import csc.processor.register.Register;

import java.util.Map;

public interface Command {
    void execute(String operand, Map<String, Register> registerMap);
}
