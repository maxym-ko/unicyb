package csc.linear.system.algorithm;

import csc.linear.system.domain.Vector;

public abstract class AbstractAlgorithm<T, R> implements Algorithm<T, R> {
    public abstract boolean checkConditions(T t);

    @Override
    public Vector solve(T t) {
        if (!checkConditions(t)) {
            throw new IllegalStateException("The input you passed doesn't specify algorithm conditions");
        }
        return solve0(t);
    }

    abstract Vector solve0(T t);
}
