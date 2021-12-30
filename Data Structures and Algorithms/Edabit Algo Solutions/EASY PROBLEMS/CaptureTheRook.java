// CAPTURE THE ROOK EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class CaptureTheRook {

    // creating a function to return a boolean value based on certain conditions.
    public static boolean captureRooks(String[] rooks) {

        // creating an if-statement to check if two rooks are on the same row or column.
        if ((rooks[0].charAt(0) == rooks[1].charAt(0) || rooks[0].charAt(1) == rooks[1].charAt(1))){

            // returning 'true' if the rooks are on the same row or column.
            return true;
        }

        // returning 'false' if the rooks are not on the same row or column, preventing a capture.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating variables to take the square coordinates of the two rooks.
        String s1 = kp.next();
        String s2 = kp.next();

        // creating an array with the two inputted square coordinates.
        String rooks[] = {s1, s2};

        // creating a variable to store and print the boolean value returned by the function.
        boolean answer = captureRooks(rooks);
        System.out.println(answer);
    }
}