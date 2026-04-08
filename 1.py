package calci;
public class Calculator {
    public int add(int a, int b){
        return a + b;
    }
    public int subtract(int a, int b){
        return a - b;
    }
    public int multiply(int a, int b){
        return a * b;
    }
    public int divide(int a, int b){
        return a / b;
    }
}

package calci;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
public class CalculatorTest {
    Calculator calc = new Calculator();
    @Test
    void testAdd(){
        assertEquals(10, calc.add(6,4));
    }
    @Test
    void testSubtract(){
        assertEquals(2, calc.subtract(6,4));
    }
    @Test
    void testMultiply(){
        assertEquals(24, calc.multiply(6,4));
    }
    @Test
    void testDivide(){
        assertEquals(2, calc.divide(8,4));
    }
}
