// POSITIVE AND NEGATIVE COUNT:

// importing the scanner object.
import java.util.Scanner;

public class PositiveAndNegativeCount {

    public static void main(String[] args) {
        
        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to keep track of the length of the array.
        System.out.print("Enter the length of the array please: ");
        int n = kp.nextInt();

        // creating an array of 'n' elements (desired number of elements).
        int arr[] = new int[n];

        // creating variables to keep track of the number of positive integers, and the sum of the negative integers.
        int posCount = 0;
        int negSum = 0;

        // creating a for-loop to iterate till the number of desired elements in the array.
        for (int i=0; i < n; i++){

            // code to recieve the element from the user to add into each index of the array.
            arr[i] += kp.nextInt();

            // creating an if-statement to check for the required conditions.
            if (arr[i] > 0){

                // code to increment the 'posCount' if the element entered is a positive integer.
                posCount++;
            }

            else if (arr[i] < 0){

                // code to add the element's value to the sum of all the negative values detected in the array.
                negSum += arr[i];
            }
        }

        // creating a new array, first element is the count of all positive elements, the second element is the sum of all negative elements.
        int newArr[] = {posCount, negSum};

        // creating a for-loop to print out the collected information about the array.
        for (int element: newArr){

            System.out.print(element);
            System.out.print(" ");
        }
    }
}