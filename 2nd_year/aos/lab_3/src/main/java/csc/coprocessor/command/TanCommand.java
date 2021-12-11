package csc.coprocessor.command;

public class TanCommand extends FuncCommand {
    public TanCommand() {
        super("FTAN", "### Обчислюємо тангенс від значення, котре зберігається на вершині стеку " +
                "та заміняємо вершину стеку на отримане значення");
    }

    @Override
    public double func(double x) {
        return Math.tan(x);
    }
}
