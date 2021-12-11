package csc.coprocessor.command;

public class AddCommand extends BiFuncCommand {
    public AddCommand() {
        super("FADDP ST(0) ST(1)", "### Додаємо два верхні значення зі стеку та викидуємо їх; " +
                "результат залишається на вершині");
    }

    @Override
    public double func(double x, double y) {
        return x + y;
    }
}
