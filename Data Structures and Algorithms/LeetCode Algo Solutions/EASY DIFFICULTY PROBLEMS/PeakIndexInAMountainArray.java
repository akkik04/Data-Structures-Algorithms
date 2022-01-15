// PEAK INDEX IN A MOUNTAIN ARRAY LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class PeakIndexInAMountainArray {

    // creating a function to find the peak index in a mountain array. 
    public static int peakIndex(int arr[]){

        // creating a variable to store the leftmost index.
        int min = 0;

        // creating a variable to store the rightmost index.
        int max = arr.length - 1;

        // creating a while-loop to perform the binary search algorithm.
        while (min < max){

            // creating a variable to store the midpoint for every search space.
            int mid = min + (max - min) / 2;

            // creating an if-statement to check if the 'peak index' conditions are satisfied.
            if (arr[mid] > arr[mid + 1]){

                // setting the rightmost index to the midpoint if the condition is met.
                max = mid;
            }

            else {

                // setting the leftmost index to the 'midpoint + 1'.
                min = mid + 1;
            }

        }

        // returning the value of the 'min', as it will store the peak index at the end of the search.
        return min;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the size of an array.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // taking input for each index 
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = peakIndex(arr);
        System.out.println(answer);
    }
}