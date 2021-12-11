package csc.coprocessor.stack;

import csc.coprocessor.register.DataRegister;

import java.util.Deque;
import java.util.LinkedList;

public class CoprocessorStack {
    private final Deque<DataRegister> registers = new LinkedList<>();
    private final int characteristicCapacity;
    private final int mantissaCapacity;

    public CoprocessorStack(int amount, int characteristicCapacity, int mantissaCapacity) {
        this.characteristicCapacity = characteristicCapacity;
        this.mantissaCapacity = mantissaCapacity;

        for (int i = 0; i < amount; i++) {
            registers.add(new DataRegister(0, characteristicCapacity, mantissaCapacity));
        }
    }

    public void push(double x) {
        registers.addFirst(new DataRegister(x, characteristicCapacity, mantissaCapacity));
        registers.removeLast();
    }

    public DataRegister peek() {
        return registers.getFirst();
    }

    public DataRegister pop() {
        registers.addLast(new DataRegister(0, characteristicCapacity, mantissaCapacity));
        return registers.pollFirst();
    }

    public double getTopValue() {
        return  registers.getFirst().getValue();
    }

    public boolean isTopValueOverflowed() {
        return registers.getFirst().isOverflowed();
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder("name   s ch  man\n");
        int i = 0;
        for (DataRegister register : registers) {
            res.append("P");
            res.append(++i);
            res.append("  =  ");
            res.append(register);
            res.append('\n');
        }
        return res.toString();
    }
}
