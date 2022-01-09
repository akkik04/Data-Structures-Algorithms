// SQRT(X) LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class SqrtX {

    // creating a function to calculate the square root.
    public static int mySqrt(int num) {

        // creating variables to store the leftmost index, rightmost index, and the result.
        long min = 0;
        long max = num;
        long res = 0;

        // creating a while-loop to perform the binary search.
        while (min <= max){

            // creating a variable to find the midpoint after each iteration.
            long mid = (min + max) / 2;

            // creating an if-statement to check if the square of the midpoint is '<=' the number.
            if (mid * mid <= num){

                // setting the result to the midpoint.
                res = mid;

                // re-writing the leftmost index as the 'mid + 1' (simply cutting out a half of possibilities).
                min = mid + 1;
            }

            else {

                // re-writing the rightmost index as the 'mid - 1' (simply cutting out another half of possibilities).
                max = mid - 1;
            }
        }

        // returning the result as an integer.
        return (int)res;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the number. 
        int num = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = mySqrt(num);
        System.out.println(answer); 
    }
}