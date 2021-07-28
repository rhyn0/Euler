import java.util.Scanner;

public class Euler {

    public static int problemMax = 3;

    public static void showProblems() {
        System.out.println("""
                \t1 - Sum of multiples of 3 and 5, default 1000
                \t2 - Sum of even Fibonacci, default 4 million
                \t3 - Largest Prime factor of N, default 600851475143
                \t4 - Largest Palindrome Product of 3 digit numbers
                \t5 - Smallest multiple of all numbers 1 to n, default 20.
                """);
    }

    public static int euler1() {
        return euler1(1000);
    }

    public static int euler1(int n) {
        int total = 0;
        for (var i = 3; i < n; i += 3) {
            total += i;
        }
        for (var i = 5; i < n; i += 5) {
            if (i % 3 != 0)
                total += i;
        }
        return total;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String input = null;
        int problem = 0;
        int retries = 0;
        do {
            if (retries > 0) {
                System.out.println("That is not an available problem at this time. Enter 'h' for more info.");
            }
            retries++;
            System.out.print("Which Euler Problem would you like the answer to (h for more info) ");
            input = in.nextLine();
            if (input.equals("h")) {
                showProblems();
                continue;
            }
            try {
                problem = Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("That was not an integer representing a problem. Please input an integer.");
            }
        } while (!(1 <= problem && problem <= problemMax) && retries < 3);
        if (retries == 3) {
            System.out.println("Input failure too many times. Exiting...");
            return;
        }
        switch (problem) {
            case 1:
                System.out.println("Answer to Eueler 1 is: " + euler1());
                break;

            default:
                System.out.println("Somehow you entered an invalid Problem number.");
                break;
        }
    }
}
