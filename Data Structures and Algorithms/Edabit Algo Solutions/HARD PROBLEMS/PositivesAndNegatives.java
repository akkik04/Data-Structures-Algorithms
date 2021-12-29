// POSITIVE AND NEGATIVES EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class PositivesAndNegatives {

    // creating a function to return 
    public static boolean positiveAndNegative(int arr[]){

        if ((arr.length == 1) && (arr[0] == 0)){

            return false;
        }

        for (int i=0; i < arr.length - 1; i++){

            if (arr[i] * arr[i + 1] >= 0){

                return false;
            }
        }
        
        return true;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // receiving input for the length of the array.
        int n = kp.nextInt();

        // creating a new array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index in the array.
        for (int i=0; i < arr.length; i++){

            arr[i] = kp.nextInt();
        }

        boolean answer = positiveAndNegative(arr);
        System.out.println(answer);
    }
}
