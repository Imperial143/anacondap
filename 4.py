MaxNumber.java
package calci;
public class MaxNumber {
    public int findMax(int a, int b, int c) {
        int max = a;
        if(b > max)
            max = b;
        if(c > max)
            max = c;
        return max;
    }
}

MaxNumberTest.java
package calci;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
public class MaxNumberTest {
    MaxNumber m = new MaxNumber();
    @Test
    void testMaxNumber() {
        assertEquals(9, m.findMax(5,9,3));
    }
}
