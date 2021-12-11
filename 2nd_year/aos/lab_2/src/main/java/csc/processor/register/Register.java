package csc.processor.register;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public abstract class Register {
    private final String name;
    private int value;
    private final int size;

    Register(String name, int value, int size) {
        this.name = name;
        this.value = value;
        this.size = size;
    }

    public abstract boolean isOverflowed();

    protected String getBinaryFormatted(String binary) {
        if (binary.length() > getSize()) binary = binary.substring(binary.length() - getSize());

        binary = String.format("%" + getSize() + "s", binary, 2).replace(" ", "0");
        List<String> result = new ArrayList<>();
        int index = binary.length();
        while (index > -1) {
            int min = Math.min(index - 4, binary.length());
            result.add(binary.substring(Math.max(min, 0), index));
            index -= 4;
        }
        Collections.reverse(result);

        return String.join(" ", result);
    }

//    protected String getBinaryFormatted(String binary) {
//        if (binary.length() > getSize()) binary = binary.substring(binary.length() - getSize());
//
//        binary = String.format("%" + getSize() + "s", binary, 2).replace(" ", "0");
//        List<String> result = new ArrayList<>();
//        int index = 0;
//        while (index < binary.length()) {
//            result.add(binary.substring(index, Math.min(index + 4, binary.length())));
//            index += 4;
//        }
//
//        return String.join(" ", result);

//    }

    public int getSign() {
        return value > 0 ? 0 : 1;
    }

    public void addValue(int addition) {
        value += addition;
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public int getSize() {
        return size;
    }
}
