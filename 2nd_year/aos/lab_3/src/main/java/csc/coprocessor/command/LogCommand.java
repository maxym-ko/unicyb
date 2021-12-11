package csc.coprocessor.command;

public class LogCommand extends FuncCommand {
    public LogCommand() {
        super("FLOGE", "### Обчислюємо натуральний логарифм від значення, " +
                "котре зберігається на вершині стеку та заміняємо вершину стеку на отримане значення");
    }

    @Override
    public double func(double x) {
        return Math.log(x);
    }
}
