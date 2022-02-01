// SIGN OF THE PRODUCT OF AN ARRAY LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class SignOfTheProductOfAnArray {

    // creating a function to find the sign of the product of an array.
    public static int signOfProduct(int arr[]) {

        // creating variables to store the count of positive and negative elements in the array.
        int positiveCount = 0;
        int negativeCount = 0;                                 

        // creating a for-loop to iterate for the elements in the array.
        for (int i=0; i < arr.length; i++){

            // creating an if-statement to check if an element is '0'.
            if (arr[i] == 0){

                // returning the product's sign as '0'.
                return 0;
            }

            else if (arr[i] > 0){

                // code to increment the positive element count if the element is greater than '0'.
                positiveCount++;
            }

            else {

                // code to increment the negative element count if the element is less than '0'.
                negativeCount++;
            }
        }                                           

        // creating an if-statement to check if the negative element count is '0'.
        if (negativeCount % 2 == 0){

            // returning '1', as a postive count of negative elements yields a postive sign for the product.
            return 1;
        }

        // returning '-1' if the sign of the product of the array is negative.
        return -1;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the capacity of the array. 
        int n = kp.nextInt();

        // creating an array of desired capacity.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = signOfProduct(arr);
        System.out.println(answer);
    }
}