package csc.processor.register;

public interface RollBackable {
    void commit();
    void rollback();
}
