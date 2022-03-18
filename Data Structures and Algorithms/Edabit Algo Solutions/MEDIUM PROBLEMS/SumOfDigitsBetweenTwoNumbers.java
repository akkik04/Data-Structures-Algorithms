// SUM OF DIGITS BETWEEN TWO NUMBERS EDABIT SOLUTION:

// importing the scanner class.
import java.util.Scanner;

public class SumOfDigitsBetweenTwoNumbers {

    public static int sumBetweenTwoNums(int a, int b) {

        // temp variable.
        int temp = a;

        // sum variable.
        int sum = 0;

        // creating a while-loop to run within the given range.
        while (temp <= b){

            a = temp;

            // algorithm to find the sum of the digits.
            while (a != 0){

                sum += a % 10;
                a /= 10;
            }

            // incremnenting the number to the next one in the range.
            temp++;
        }

        // returning the value of the sum.
        return sum;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating variables to store the first and second numbers.
        int a = kp.nextInt();
        int b = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = sumBetweenTwoNums(a, b);
        System.out.println(answer);
    }
}