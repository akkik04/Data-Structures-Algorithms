// ADD DIGITS LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class AddDigits {
    
    public static int addDigits(int num) {

        // creating a variable to store the sum of the digits.
        int sum = 0;

        // creating a while-loop to iterate while the number is greater than '0'.
        while (num > 0){

            // adding the digit of the current number to the sum.
            sum += num % 10;
            num /= 10;

            // creating an if-statement to check if the iteration is still necessary.
            if (num == 0 && sum > 9){

                // re-writing the old sum, and setting the new sum as the item to iterate through.
                num = sum;
                sum = 0;
            }
        }

        // returning the sum.
        return sum;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the inputted number.
        int n = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = addDigits(n);
        System.out.println(answer);
    }
}