import java.text.MessageFormat;


public class Print {
    public static void main(String[] args) {
        // Example usage
        print("Hello {0} #{1}. It is {2}.", "guest", 3, 
            java.time.LocalDateTime.now());
    }

    // Function for formattable printing to the console
    public static void print(String template, Object... args) {
        String msg = new MessageFormat(template).format(args);
        System.out.println(msg);
    }
}