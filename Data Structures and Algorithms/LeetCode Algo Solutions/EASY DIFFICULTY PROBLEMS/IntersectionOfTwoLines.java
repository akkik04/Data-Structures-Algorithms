// INTERSECTION OF TWO LINES JAVA PROGRAM:

// importing the scanner class.
import java.util.Scanner;

public class IntersectionOfTwoLines {

    // creating a function to return the point of intersection.
    public static String pointOfIntersection(int m1, int b1, int m2, int b2) {

        // creating an if-statement to check for parallel lines.
        if (m1 == m2 && b1 != b2){

            return "There is no POI, the two lines are parallel.";
        }

        // checking for the same line, leading to infinite points of intersection.
        else if (m1 == m2 && b1 == b2){

            return "There are infinite POI, the two lines are the same.";
        }

        // calculating the x-coordinate of the POI.
        int xCoor = (b2 - b1) / (m1 - m2);

        // calculating the y-coordinate of the POI.
        int yCoor = ((m1 * ((b2 - b1) / (m1 - m2))) + b1);

        // returning the POI.
        return "The POI is: " + "(" + xCoor + "," + yCoor + ")";
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // taking the required input about the characteristics (slope and y-intercept) of both lines.
        int m1 = kp.nextInt();
        int b1 = kp.nextInt();
        int m2 = kp.nextInt();
        int b2 = kp.nextInt();

        // printing the statement returned by the function.
        String answer = pointOfIntersection(m1, b1, m2, b2);
        System.out.println(answer);
    }
}