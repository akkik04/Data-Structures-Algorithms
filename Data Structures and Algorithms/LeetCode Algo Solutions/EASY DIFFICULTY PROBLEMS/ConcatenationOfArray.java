// CONCATENATION OF ARRAY LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class ConcatenationOfArray {

    public static int[] concatenateArray(int arr[], int n) {

        // creating an array, double the capacity of the initial inputted size.
        int new_arr[] = new int[n * 2];

        // creating a for-loop to iterate for the length of the initial array.
        for (int i = 0; i < n; i++){

            // adding the elements at their appropriate places.
            new_arr[i] = arr[i];
            new_arr[i + n] = arr[i];
        }

        // returning the new array.
        return new_arr;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired capacity.
        int n = kp.nextInt();
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i = 0; i < n; i++){

            arr[i] = kp.nextInt();
        }

        // creating a variable to store the new array returned by the function.
        int answer[] = concatenateArray(arr, n);

        // creating a for-loop to print the elements in the returned new array.
        for (int ele: answer){

            System.out.print(ele);
            System.out.print(" ");
        }
    }
}