package csc.linear.system.algorithm;

import csc.linear.system.domain.Vector;

public interface Algorithm<T, R> {
    Vector solve(T t);
}
