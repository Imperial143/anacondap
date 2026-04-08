BankAccount.java
package calci;
public class BankAccount {
    private double balance;
    public BankAccount(double balance) {
        this.balance = balance;
    }
    public double getBalance() {
        return balance;
    }
    public void deposit(double amount) {
        balance = balance + amount;
    }
    public void withdraw(double amount) {
        balance = balance - amount;
    }
}

BankAccountTest.java
package calci;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
public class BankAccountTest {
    @Test
    void testDeposit() {
        BankAccount acc = new BankAccount(1000);
        acc.deposit(500);

        assertEquals(1500, acc.getBalance());
    }
    @Test
    void testWithdraw() {
        BankAccount acc = new BankAccount(1000);
        acc.withdraw(300);
        assertEquals(700, acc.getBalance());
    }

}
