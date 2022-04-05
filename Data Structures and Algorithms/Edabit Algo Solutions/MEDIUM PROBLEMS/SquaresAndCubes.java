// SQUARES AND CUBES EDABIT SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class SquaresAndCubes {

    public static boolean squaresAndCubes(int[] arr) {

        // returning 'true' if the condition is met, else 'false'.
        return Math.sqrt(arr[0]) == Math.cbrt(arr[1]);
        
    }       

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array to hold the two inputted numbers.
        int[] arr = new int[2];
        for (int i = 0; i < arr.length; i++){

            arr[i] = kp.nextInt();
        }

        // creating a boolean variable to print the value returned by the function.
        boolean answer = squaresAndCubes(arr);
        System.out.println(answer);
    }
}