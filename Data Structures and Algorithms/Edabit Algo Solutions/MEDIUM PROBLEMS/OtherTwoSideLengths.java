// FIND THE OTHER TWO SIDE LENGTHS EDABIT SOLUTION (JAVA):

// importing required modules.
import java.util.Scanner;
import java.lang.Math;

public class OtherTwoSideLengths {

    // function to calculate the other sides, and output them in an array.
    public static double[] othersides(int small_side) {

        // creating a variable to calculate the hypotenuse.
        double hypot = small_side * 2;

        // creating a variable to calculate the 'last side'.
        double last_side = (small_side *(Math.sqrt(3)));

        // code to round the 'last side', as specified by the question.
        last_side *= 100;
        last_side = Math.round(last_side);
        last_side /= 100;

        // creating an array of 'double-type' to store the two values of the sides.
        double arr[] = {hypot, last_side};

        // returning the array.
        return arr;
    }
    
    // main.
    public static void main(String[] args) {

        // instantiating the scanner object for user input.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input from the user regarding the magntitude of the 'small side'.
        int small_side = kp.nextInt();

        // creating a variable of an array of 'double-type' to store the array given from the function.
        double[] answer;

        // calling the function, and storing its output in the 'answer' variable.
        answer = othersides(small_side);

        // code to print the array with the magnitudes of the sides.
        for (double element: answer){

            System.out.print(element);
            System.out.print(" ");
        }
    }
}