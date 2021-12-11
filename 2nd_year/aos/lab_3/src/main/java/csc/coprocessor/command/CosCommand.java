package csc.coprocessor.command;

public class CosCommand extends FuncCommand {
    public CosCommand() {
        super("FCOS", "### Обчислюємо косинус від значення, котре зберігається на вершині стеку " +
                "та заміняємо вершину стеку на отримане значення");
    }

    @Override
    public double func(double x) {
        return Math.cos(x);
    }
}
