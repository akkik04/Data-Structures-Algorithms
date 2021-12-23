// FINDING THE MISSING NUMBER IN AN ARRAY FROM ELEMENTS ONE TO TEN:

// importing the scanner object for taking user input.
import java.util.Scanner;

public class FindTheMissingNumberOneToTen {

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        
        Scanner kp = new Scanner(System.in);

        // creating an array with 10 total elements (9 indexes with 0-based indexing).
        int arr[] = new int[9];
        
        // creating a variable to store the sum of the numbers from 1-10.
        int total = 55;

        // creating a for-loop to take the numbers as input to create the array.
        System.out.print("Enter the elements from 1-10, with a number missing please: ");
        for (int i=0; i < arr.length; i++){

            // taking the numbers as input.
            arr[i] = kp.nextInt();

            // arithmetic operation to find the missing number.
            total -= arr[i];
        }

        // code to print out the missing number to the user.
        System.out.println("The missing number from the array is: " + total);
    }
}
