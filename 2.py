GreetingService.java
package calci;
public class GreetingService {
    public String greet(String name) {
        return "Hello " + name + "!";
    }
}

GreetingServiceTest.java
package calci;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
public class GreetingServiceTest {
    GreetingService service = new GreetingService();
    @Test
    void testGreeting() {
        assertEquals("Hello Pranav!", service.greet("Pranav"));
    }

}
