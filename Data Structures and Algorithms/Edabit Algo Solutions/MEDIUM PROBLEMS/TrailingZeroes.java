// TRAILING ZEROES EDABIT SOLUTION:

// importing the scanner class.
import java.util.Scanner;

public class TrailingZeroes {

    public static int factorialTrailingZeroes(int n) {

        // creating a variable to store a value of '5'.
        // this variable serves a key purpose, as a trailing zero is added to 'n' for every multiple of 5.
        int x = 5;

        // creating a variable to keep track of the count of trailing zeroes.
        int count = 0;

        // creating a while-loop to iterate when 'n >= x'.
        while (n >= x){

            // incrementing the count.
            count += (n / x);   
            
            // re-writing 'x'.
            x *= 5;
        }

        // returning the count of the trailing zeroes.
        return count;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // taking input for the number.
        int num = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = factorialTrailingZeroes(num);
        System.out.println(answer);
    }
}