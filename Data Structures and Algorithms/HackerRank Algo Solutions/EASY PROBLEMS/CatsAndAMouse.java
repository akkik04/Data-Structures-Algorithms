// CATS AND A MOUSE HACKERRANK SOLUTION (JAVA):

// importing the required modules.
import java.util.Scanner;
import java.lang.Math;

public class CatsAndAMouse {

    // creating a function to determine the winner. 
    public static String CatAndMouse(int x, int y, int z){

        // creating an if-statement to check for the different winners. 
        if (Math.abs(z - y) < Math.abs(z - x)){

            // returning 'Cat B' if its distance to the mouse is closer.
            return "Cat B";
        }

        else if (Math.abs(z - y) > Math.abs(z - x)){

            // returning 'Cat A' if its distance to the mouse is closer.
            return "Cat A";
        }

        // returning 'Mouse C' if it overcomes the two cats.
        return "Mouse C";
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating variables to take the three positions (Cat A, Cat B, Mouse C).
        int x = kp.nextInt();
        int y = kp.nextInt();
        int z = kp.nextInt();

        // creating a variable to store and print the output returned by the function. 
        String answer = CatAndMouse(x, y, z);
        System.out.println(answer);
    }
}