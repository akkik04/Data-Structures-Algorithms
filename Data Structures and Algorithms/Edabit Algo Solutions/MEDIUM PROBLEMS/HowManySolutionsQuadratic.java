// HOW MANY SOLUTIONS TO A QUADRATIC, GIVEN 'A', 'B', AND 'C':

// importing the scanner object.
import java.util.Scanner;

public class HowManySolutionsQuadratic{

    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating variables for the 'a', 'b', and 'c' values of the quadratic equation.
        int a = kp.nextInt();
        int b = kp.nextInt();
        int c = kp.nextInt();
        
        System.out.println(" ");

        // creating a variable to store the value of the discriminant.
        int discriminant = (b * b) - (4 * a * c);

        // creating an if-statement to check the number of solutions based on the fundamentals of the discriminant.
        if (discriminant > 0) { 

            // code to print '2' solutions if the discriminant is greater than '0'.
            System.out.println("2");
        }
        else if (discriminant == 0) {

            // code to print '1' solution if the discriminant is equal to '0'.
            System.out.println("1");
        }
        else {

            // code to print '0' solutions if the discriminant is less than '0'.
            System.out.println("0");
        }
    }
}