// HIGHEST DIGIT EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class HighestDigit {

    // creating a function to find the highest digit in the given integer.
    public static int highDigit(int n) {

        // creating variables to track the highest digit, and the last digit of the integer.
        int highestDigit = 0, lastDig = 0;

        // creating a while-loop to iterate until the last digit of the given integer.
        while (n != 0){

            // storing the last digit of the integer in the variable for each iteration.
            lastDig = n % 10;

            // creating an if-statement to compare the current digit with the previous one.
            if (lastDig > highestDigit){

                // code to store the current digit as the highest digit if the condition is met.
                highestDigit = lastDig;
            }

            // arithmetically decreasing the integer by a digit for each iteration.
            n = n / 10;
        }

        // returning the highest digit.
        return highestDigit;
        
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object for user input.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take an integer as input from the user.
        int n = kp.nextInt();
        
        // creating a variable to store and print the highest digit returned by the function.
        int answer = highDigit(n);
        System.out.println(answer);
        
    }
}