// POWER OF TWO EDABIT SOLUTION (JAVA):

// importing the required modules.
import java.util.Scanner;
import java.lang.Math;

public class PowerOfTwo {

    // creating a boolean function to return if the number is a power of two. 
    public static boolean powTwo(int num) {

        // creating an if-statement to return 'False' if the number is less than zero.
        if (num <=0){

            // returning 'False'.
            return false;
        }

        // creating a for-loop to iterate until the number.
        for (int i=0; i < num; i++){

            // creating an if-statement to check for the number being a power of two.
            if (Math.pow(2, i) == num){

                // returning 'True'.
                return true;
            }
        }

        // returning 'False'.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object for user input.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take an integer as input from the user.
        int num = kp.nextInt();
        
        // creating a boolean variable to store the boolean value returned from the function.
        boolean answer = powTwo(num);

        // printing the output to the user.
        System.out.print(answer);
    }
}