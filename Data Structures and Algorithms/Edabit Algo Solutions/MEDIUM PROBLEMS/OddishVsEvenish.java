// ODDISH VS. EVENISH EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class OddishVsEvenish {

    // creating a function to return a string based on the parity of the sum of the digits.
    public static String oddVsEven(int num) {

        // creating a variable to keep track of the current digit and the sum.
        int dig = 0;
        int sum = 0;

        // creating a while-loop to find the sum of the digits in the given number.
        while (num != 0){

            // algorithm to sum the digits in the integer.
            dig = num % 10;
            sum += dig;
            num /= 10;
        }

        // creating an if-statement to check for the parity of the sum.
        if (sum % 2 == 0){

            // returning 'Evenish' if the sum is an even number.
            return "Evenish";
        }

        // returning 'Oddish' if the sum is an odd number.
        return "Oddish";
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for a number.
        int num = kp.nextInt();

        // creating a variable to store and print the 'string' returned by the function.
        String answer = oddVsEven(num);
        System.out.println(answer);
    }
}