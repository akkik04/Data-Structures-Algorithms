// SPECIAL ARRAYS:

// importing the scanner object in java.
import java.util.Scanner;

public class SpecialArrays {

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object to enable user input.
        Scanner kp = new Scanner(System.in);

        // creating a variable named 'count' to keep track of the valid indexes and respective values.
        int count = 0;

        // creating a variable to take the length of the array (0-indexed).
        int n = kp.nextInt();

        // creating an array with the amount of desired elements from the user.
        int arr[] = new int[n];
        
        // creating a for-loop to recieve array input and check for the required conditions to achieve a special array.
        for (int i=0; i < n; i++){

            // code to take input for the elements in the array.
            arr[i] = kp.nextInt();

            // creating an if-statement to check for the required conditions to be a special array.
            if ((i % 2 == 0) && (arr[i] % 2 == 0)){

                count++;
            }
            else if ((i % 2 != 0) && (arr[i] % 2 != 0)){

                count++;
            }
        }

        // code to print out if the array is special or not based on the count value relating to the array length.
        System.out.print(count == arr.length);
    }
}