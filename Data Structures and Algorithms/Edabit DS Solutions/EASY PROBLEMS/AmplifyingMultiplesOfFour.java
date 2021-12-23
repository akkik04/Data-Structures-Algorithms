// AMPLIFYING MULTIPLES OF FOUR EDABIT SOLUTION:

// importing the scanner object.
import java.util.Scanner;

public class AmplifyingMultiplesOfFour {

    public static void main(String[] args) {

        // code to instantiate the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating variables to take input for the array size and create an integer array.
        int n = kp.nextInt();
        int arr[] = new int[n];

        // creating a for-loop to iterate through the numbers until 'n', while checking for the required conditions to amplify.
        for (int i=0; i < n; i++){

            // saving each number as an element in the array.
            arr[i] = i + 1;

            // checking the condition to amplify for each element in the array.
            if (arr[i] % 4 == 0){

                arr[i] = arr[i] * 10;
            }
        }

        // creating a for-loop to iterate through the array to print the modified array.
        for (int element: arr){

            // code to print each element in the array.
            System.out.print(element);
            System.out.print(" ");
        }
    }
}
