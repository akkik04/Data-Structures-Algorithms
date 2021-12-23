// ARRAY OF MULTIPLES:

// importing the scanner object.
import java.util.Scanner;

public class ArrayOfMultiples {

    public static void main(String[] args) {
        
        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the desired number's multiples. 
        System.out.print("Enter a number to find its multiples please: ");
        int number = kp.nextInt();

        // creating a variable to store the length at which the number's multiples must be repeated till.
        System.out.print("Enter the length of the multiples please: ");
        int length = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[length];

        // creating a variable to keep track of the count variable, setting it to '1'.
        int count = 1;

        // creating a for-loop to add the multiples till the desired length to the array. 
        for (int i=0; i < length; i++){

            // adding each multiple to each index, using the counter strategy.
            arr[i] = number * count;

            // incrementing the counter after each iteration for use to find the next multiple of the number.
            count++;
        }

        // creating a for-loop to print out the multiples in an array.
        for (int element: arr){

            System.out.print(element);
            System.out.print(" ");
        }
    }
}