// BINARY SEARCH LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class BinarySearch {

    // creating a function to perform the binary search algorithm.
    public static int binSearch(int arr[], int target) {

        // creating a variable to initialize the leftmost index.
        int mindex = 0;

        // create a variable to initialize the rightmost index.
        int maxdex = arr.length - 1;

        // creating a while-loop to iterate while the leftmost index is less than or equal to the rightmost index.
        while (mindex <= maxdex){

            // finding out midpoint in the array.
            int mid = (mindex + maxdex) / 2;

            // creating an if-statement to check if the midpoint in the array contains the target.
            if (arr[mid] == target){

                // returning the midpoint (index) if the condition is met.
                return mid;
            }
            
            // checking if the target is before the midpoint.
            else if (arr[mid] > target){

                // decreasing the rightmost index to the 'midpoint - 1'. (simply cutting out a half of the array if needed).
                maxdex = mid - 1;
            }

            // checking if the target is after the midpoint.
            else if (arr[mid] < target){

                // increasing the leftmost index to the 'midpoint + 1'. (simply cutting out the other half of the array if needed).
                mindex = mid + 1;
            }
        }

        // returning '-1' if the target is not within the array.
        return -1;  
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the length of the array.
        int n = kp.nextInt();
        
        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to take input for the desired target element. 
        int target = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = binSearch(arr, target);
        System.out.println(answer);
    }
}