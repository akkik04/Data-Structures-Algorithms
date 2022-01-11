// SUM OF SQUARE NUMBERS LEETCODE SOLUTION:

// importing the scanner class.
import java.util.Scanner;

public class SumOfSquareNumbers {

    // creating a function to judge 'c' based on the square sum functionality.
    public static boolean judgeSquareSum(int c){

        // creating a variable to create two pointers
        // 'min' set to '0'.
        // 'max' set to square root of 'c', as range is only between (1, √c).
        long min = 0;
        long max = (int)Math.sqrt(c);

        // creating a while loop to iterate through the possible search space.
        while (min <= max){

            // creating a variable to calculate the square sum.
            long res = (min * min) + (max * max);

            // creating an if-statement to check if the square sum is equal to 'c'.
            if (res == c){

                // returning 'true' if the condition is met.
                return true;
            }
        
            else if (res > c){

                // if the computed square sum is greater than the 'c', we decrease the max pointer, as we know it is too high.
                max--;
            }

            else{

                // if the computed square sum is less than the 'c', we increase the min pointer, as we know it is too low.
                min++;
            }
        }

        // returning 'false' if the condition is met.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for an integer.
        int c = kp.nextInt();
        
        // creating a variable to store and print the value returned by the function.
        boolean answer = judgeSquareSum(c);
        System.out.println(answer);
    }
}