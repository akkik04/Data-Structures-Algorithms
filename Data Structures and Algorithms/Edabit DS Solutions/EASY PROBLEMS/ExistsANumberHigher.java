// EXISTS A NUMBER HIGHER EDABIT SOLUTION:

// importing the scanner object.
import java.util.Scanner;

public class ExistsANumberHigher {

    // creating a function to check for a number higher than 'num' in the array.
    public static boolean NumberHigher(int arr[], int num) {

        // creating a for-loop to iterate for the length of the array.
        for (int j=0; j < arr.length; j++){

            // creating an if-statement to check for any element being higher than 'num'.
            if (arr[j] > num){

                // returning 'true' if the condition is met.
                return true;
            }
        }

        // returning 'false' if there is no higher number than 'num'.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // prompting the user for the number of elements in the array.
        System.out.print("Enter the number of elements in the array please: ");
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to iterate for the length of the array to take input for each index.
        for (int i=0; i < arr.length; i++){

            // taking input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // prompting the user for the main number to perform the comparison to other numbers in the array.
        System.out.println("Enter the main number please: ");
        int num = kp.nextInt();

        // creating a variable to store and print the 'boolean value' returned by the function.
        boolean answer = NumberHigher(arr, num);
        System.out.println(answer);
    }
}