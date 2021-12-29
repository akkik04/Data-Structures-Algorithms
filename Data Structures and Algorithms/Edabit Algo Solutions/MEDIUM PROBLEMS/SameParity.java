// SAME PARITY EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class SameParity {

    // creating a function to return a boolean value based on parity.
    public static boolean sameParity(int num) {

        // creating variables to perform the task of summing the digits of the given integer.
        int sum = 0;
        int digit = 0;
        int temp = num;

        // creating a variable to take length of the integer.
        int length = String.valueOf(num).length();

        // creating an if-statement to return 'true' for the base case of a single digit, as parity remains the same.
        if (length == 1){

            // returning 'true'.
            return true;
        } 

        // creating a while-loop to calculate the sum of the digits.
        while (temp != 0){

            // code to sum each digit.
            digit = temp % 10;
            sum += digit;

            // dividing by 10 to discard the digit that was previously summed, it is done for each iteration.
            temp /= 10;
        }

        // creating an if-statement to compare the parity of the sum of digits and the integer.
        if ((num % 2 == 0) && (sum % 2 == 0)){

            return true;
        }

        else if ((num % 2 == 1) && (sum % 2 == 1)){

            return true;
        }

        // returning 'false' if the parity does not match upon comparison.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the number from the user.
        int num = kp.nextInt();

        // creating a variable to store and print the boolean value returned by the function.
        boolean answer = sameParity(num);
        System.out.println(answer);
    }
}