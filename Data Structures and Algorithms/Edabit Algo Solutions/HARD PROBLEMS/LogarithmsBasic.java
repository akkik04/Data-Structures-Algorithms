// LOGARITHMS BASIC EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class LogarithmsBasic {

    // creating a function to calculate the 'power' of the logarithm.
    public static void Logarithms(int base, int num) {

        // creating a for-loop to find the 'power'.
        for (int i=1; i < num; i++){

            // creating a nested if-statement to check for a valid 'power'. 
            if (Math.pow(base, i) == num){

                // code to print the 'power' if it is found.
                System.out.println(i);
            }
        }

        // code to print 'Invalid' if no 'valid power' is found.
        System.out.println("Invalid");
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating variables to take input for the 'base' and 'number' of the logarithm.
        int base = kp.nextInt();
        int num = kp.nextInt();

        // calling the function.
        Logarithms(base, num);
    }
}