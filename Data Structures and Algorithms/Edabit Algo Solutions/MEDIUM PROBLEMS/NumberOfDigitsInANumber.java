// FIND THE NUMBER OF DIGITS IN A NUMBER EDABIT SOLUTION (JAVA);

// importing the scanner object.
import java.util.Scanner;

public class NumberOfDigitsInANumber {
    
    // creating a function to count the number of digits in the given integer.
    public static int numDigits(int num) {

        // creating a variable to track the count of digits, initializing it to '1'.
        int count = 1;

        // creating a while-loop to count the number of digits.
        while (num / 10 != 0){

            // incrementing the count variable for each iteration.
            count++;

            // performing an arithmetic operation on the number to decrease the number by a digit after each iteration.
            num /= 10;
        }

        // returning the count of digits in the given integer.
        return count;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the number.
        int num = kp.nextInt();

        // creating a variable to store and print the count returned by the function.
        int answer = numDigits(num);
        System.out.println(answer);
    }
}