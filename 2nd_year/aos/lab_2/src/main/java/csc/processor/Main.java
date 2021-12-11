package csc.processor;

import csc.processor.command.*;
import csc.processor.register.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
    private static final Map<String, Register> registerMap = new TreeMap<>();
    private static final Map<String, Command> commandMap = new TreeMap<>();
    private static final int SIZE = 18;

    public static void main(String[] args) throws Exception {
        if (args.length != 1) throw new IllegalArgumentException("There should be one argument (file name)");

        init();
        CommandReader commandReader = new CommandReader(args[0]);
        Scanner scanner = new Scanner(System.in);

        String command;
        String code;
        String operand;
        while ((command = commandReader.nextCommand()) != null) {
            scanner.nextLine();

            registerMap.get("TC").setValue(1);

            code = commandReader.getCode();
            operand = commandReader.getOperand();

            if (!updateInstructionRegisterAndOverflow(code, operand)) continue;
            printState(command);
            scanner.nextLine();

            Command commandExecutor = commandMap.get(code);
            if (commandExecutor == null) throw new IllegalArgumentException("There is no such a command code");
            commandExecutor.execute(operand, registerMap);
            registerMap.get("TC").addValue(1);
            printState(command);

            registerMap.get("PC").addValue(1);
        }

    }

    private static boolean updateInstructionRegisterAndOverflow(String command, String operand) {
        ((ProgramSateRegister) registerMap.get("PS")).setIsOverflow(0);

        InstructionRegister instructionRegister = (InstructionRegister) registerMap.get("IR");
        instructionRegister.setCommand(command);
        instructionRegister.commit();
        instructionRegister.setOperand(operand);
        if (instructionRegister.isOverflowed()) {
            instructionRegister.rollback();
            System.out.println("The command '" + command + " " + operand + "' was skipped due to the overflow");
            return false;
        }
        return true;
    }

    private static void init() {
        registerMap.put("IR", new InstructionRegister(SIZE, "IR")); // instructionRegister
        registerMap.put("R1", new DataRegister(SIZE, "R1")); // register1
        registerMap.put("R2", new DataRegister(SIZE, "R2")); // register2
        registerMap.put("R3", new DataRegister(SIZE, "R3")); // register3
        registerMap.put("R4", new DataRegister(SIZE, "R4")); // register4
        registerMap.put("PC", new SpecialPurposeRegister(SIZE, "PC", 1)); // programCounter
        registerMap.put("TC", new SpecialPurposeRegister(SIZE, "TC")); // timeCounter
        registerMap.put("PS", new ProgramSateRegister(SIZE, "PS")); // programSate
        registerMap.put("A", new AccumulatorRegister(SIZE, "A ")); // accumulator

        commandMap.put("mov", new MoveCommand("mov", SIZE));
        commandMap.put("save", new SaveCommand("save"));
        commandMap.put("inv", new InversionCommand("inv", SIZE));
        commandMap.put("add", new AddCommand("add", SIZE));
        commandMap.put("sub", new SubtractCommand("sub", SIZE));
        commandMap.put("mod", new ModCommand("mod", SIZE));
        commandMap.put("and", new AndCommand("and", SIZE));
        commandMap.put("or", new OrCommand("or", SIZE));
    }

    private static void printState(String command) {
        System.out.println("Command = " + command);
        System.out.print(registerMap.get("R1") + "\t\t\t");
        System.out.println(registerMap.get("IR"));
        System.out.print(registerMap.get("R2") + "\t\t\t");
        System.out.println(registerMap.get("PC"));
        System.out.print(registerMap.get("R3") + "\t\t\t");
        System.out.println(registerMap.get("TC"));
        System.out.print(registerMap.get("R4") + "\t\t\t");
        System.out.println(registerMap.get("PS"));
        System.out.println(registerMap.get("A"));
    }

    private static class CommandReader {
        private final Scanner scanner;
        private String[] commandArray;

        CommandReader(String fileName) throws FileNotFoundException {
            scanner = new Scanner(new File(fileName));
        }

        String nextCommand() {
            if (!scanner.hasNext()) return null;
            String command = scanner.nextLine();
            commandArray = command.split("\\s");
            validate(commandArray);

            return command;
        }

        void validate(String[] array) {
            if (array.length != 2)
                throw new IllegalArgumentException("The command should match format 'command_code operand'");
            if (array[0].matches(".*\\d.*"))
                throw new IllegalArgumentException("The command code can't contain digits");
        }

        String getCode() {
            return commandArray[0];
        }

        String getOperand() {
            return commandArray[1];
        }
    }
}
