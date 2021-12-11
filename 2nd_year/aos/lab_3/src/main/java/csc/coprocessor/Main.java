package csc.coprocessor;

import csc.coprocessor.command.*;
import csc.coprocessor.converter.BinaryConverter;
import csc.coprocessor.register.ProgramStateRegister;
import csc.coprocessor.stack.CoprocessorStack;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Ця лабораторна робота симулює роботу математичного сопроцесора та " +
                "демонструє обрахунок наступного виразу: ln(y)*cos(x) + 3*tg(x)\n");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Введіть x, y для того, щоб почати обрахунок: ");
        double x = scanner.nextDouble();
        double y = scanner.nextDouble();
        System.out.println();

        CoprocessorStack stack = new CoprocessorStack(4, 3, 9);
        ProgramStateRegister stateRegister = new ProgramStateRegister();
        Command[] commands = {
                new LoadCommand(x),
                new DuplCommand(),
                new TanCommand(),
                new LoadCommand(3),
                new MulCommand(),
                new ExchCommand(),
                new CosCommand(),
                new LoadCommand(y),
                new LogCommand(),
                new MulCommand(),
                new AddCommand()
        };

        for (Command command : commands) {
            scanner.nextLine();
            System.out.println(command);
            command.execute(stack);
            System.out.print(stack);
            checkState(stack, stateRegister);
            System.out.println(stateRegister);
        }

        System.out.println("Результат обчислення: " + stack.getTopValue());
    }

    private static void checkState(CoprocessorStack stack, ProgramStateRegister stateRegister) {
        stateRegister.setOverflowed(stack.isTopValueOverflowed());
        stateRegister.setLastCommandPositive(stack.peek().getValue() > 0);
    }
}
