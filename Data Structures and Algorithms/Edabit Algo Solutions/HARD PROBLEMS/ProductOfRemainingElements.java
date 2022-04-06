// PRODUCT OF REMAINING ELEMENTS EDABIT SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class ProductOfRemainingElements {

    public static boolean productOfRemainingElements(int[] arr) {

        // creating a for-loop to iterate through the elements in the array.
        for (int i = 0; i < arr.length; i++){

            // storing the current element.
            int cur_el = arr[i];

            // creating a variable to store the product.
            int product = 1;

            // creating a nested for-loop for a second iteration through the array.
            for (int j = 0; j < arr.length; j++){

                // avoiding the current index.
                if (i != j){

                    // contributing to the product variable, as long as it is not the current index.
                    product *= arr[j];
                }
            }

            // creating an if-statement to validate the product.
            if (product == cur_el){

                // returning 'true' if the condition is met.
                return true;
            }
        }

        // returning 'false'.
        return false;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of numbers from user-input.
        int n = kp.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){

            arr[i] = kp.nextInt();
        }

        // creating a variable to store the value returned by the function.
        boolean answer = productOfRemainingElements(arr);
        System.out.println(answer);
    }
}