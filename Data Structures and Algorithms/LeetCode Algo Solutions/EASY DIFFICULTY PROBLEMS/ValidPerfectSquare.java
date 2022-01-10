// VALID PERFECT SQUARE LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class ValidPerfectSquare {

    // creating a function to return a boolean value based on properties of a perfect square.
    public static boolean isPerfectSquare(int n) {

        // creating the left and righthand indexes.
        long min = 0;
        long max = n;

        // creating a while-loop to perform the binary search.
        while (min <= max){

            // creating a variable to store the mid after each iteration.
            long mid = min + (max - min) / 2;

            // creating an if-statement to check if 'mid * mid == n', indicating a direct perfect square.
            if (mid * mid == n){

                // returning 'true' if the condition is met.
                return true;
            }

            // if 'mid * mid > n', we know that one half of the number list is not relevant anymore.
            else if (mid * mid > n){

                // re-writing the rightmost index.
                max = mid - 1;
            }

            else {

                // re-writing the min index.
                min = mid + 1;
            }
        }

        // returning 'false' if the number is not a perfect square.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);
        
        // creating a variable to take input for a number.
        int num = kp.nextInt();

        boolean answer = isPerfectSquare(num);
        System.out.println(answer); 
    }
}