// SUBTRACT THE PRODUCT AND SUM OF DIGITS OF AN INTEGER LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class SubtractProductAndSumOfDigits {

    // creating a function to find the difference between the product and sum.
    public static int productAndSum(int n){

        // creating variables to store the product and the sum.
        int product = 1;
        int sum = 0;

        // creating a 'temp' version of 'n' to find the sum and product of its digits.
        int temp = n;

        // creating a variable to store the current digit.
        int dig = 0;
        
        // creating a while-loop to iterate to the end of all the digits.
        while (temp > 0){

            // storing the current digit.
            dig = temp % 10;

            // code to apply the appropriate action on the digit.
            product *= dig;
            sum += dig;

            // code to get rid of the digit that was examined already.
            temp /= 10;

        }

        // returning the difference between the product and the sum.
        return product - sum;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input and store a number from the user.
        int n = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = productAndSum(n);
        System.out.println(answer);
    }
}
