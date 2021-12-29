// POSITIVE AND NEGATIVES EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class PositivesAndNegatives {

    // creating a function to return the appropriate boolean value.
    public static boolean positiveAndNegative(int arr[]){
        
        // creating an if-statement to check for the case of a direct 'false'.
        if ((arr.length == 1) && (arr[0] == 0)){
            
            // returning 'false' if the condition is met.
            return false;
        }
        
        // creating a for-loop to iterate for the length of the array.
        for (int i=0; i < arr.length - 1; i++){
            
            // creating a nested if-statement to check if the product of adjacent elements is positive.
            if (arr[i] * arr[i + 1] >= 0){
                
                // returning 'false', as the sum should be negative for alternating signed elements.
                return false;
            }
        }
        
        // returning 'true' if no objections are met.
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
        
        // creating a variable to store and output the boolean value returned by the function.
        boolean answer = positiveAndNegative(arr);
        System.out.println(answer);
    }
}
