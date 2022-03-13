// FIND THE MEAN OF ALL DIGITS EDABIT SOLUTION (JAVA):

import java.util.Scanner;

public class FindTheMeanOfAllDigits {

    public static int findMean(int n) {

        // creating variables to track the count of digits and their sum.
        int count = 0;
        int sum = 0;

        // creating a while-loop to iterate over all the digits in the integer.
        while (n > 0){

            // filtering one digit at a time.
            int dig = n % 10;

            // adding the digit to the sum, and incrementing the digit count.
            sum += dig;
            count++;

            // decreasing the original integer by a digit, as it is already analyzed.
            n /= 10;
        }

        // returning the mean.
        return (sum / count);
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the integer input.
        int n = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = findMean(n);
        System.out.println(answer);
    }
}