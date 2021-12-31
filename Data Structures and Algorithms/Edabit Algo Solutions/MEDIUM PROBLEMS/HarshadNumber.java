// HARSHAD NUMBER EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class HarshadNumber {

    // creating a function to return a boolean value based on the 'harshad number' requirements.
    public static boolean harshadNumber(int num) {

        // creating variables to calculate the sum of the digits. 
        int dig = 0;
        int sum = 0;
        int temp = num;

        // creating a while-loop to find the sum of the digits.
        while (temp != 0){

            // code to find the current digit of the number.
            dig = temp % 10;

            // adding the digit to the sum variable.
            sum += dig;

            // code to reduce the integer by the current digit.
            temp /= 10;
        }

        // creating an if-statement to check if the number is a 'Harshad Number'.
        if (num % sum == 0){

            // returning 'true' if the number is a 'Harshad Number'.
            return true;
        }

        // returning 'false' if the number is not a 'Harshad Number'.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input and store a number from the user.
        int num = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        boolean answer = harshadNumber(num);
        System.out.println(answer);  
    }
}