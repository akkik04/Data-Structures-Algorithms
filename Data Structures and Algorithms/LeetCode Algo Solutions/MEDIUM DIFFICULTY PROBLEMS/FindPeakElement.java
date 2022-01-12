// FIND PEAK ELEMENT LEETCODE SOLUTION:

// importing the scanner class.
import java.util.Scanner;

public class FindPeakElement {

    // creating a function to find the index of the peak element.
    public static int findPeakElement(int arr[]){

        // creating a leftmost index and a rightmost index.
        int min = 0;
        int max = arr.length - 1;

        // creating a while-loop to perform the binary search.
        while (min < max){

            // creating a variable to store the midpoint of the search space for each iteration.
            int mid = (min + max) / 2;

            // creating an if-statement to check for the conditions of a 'peak element'.
            if (arr[mid] > arr[mid + 1]){

                // setting the rightmost index as the mid, if the condition is met.
                max = mid;
            }

            else {

                // setting the leftmost index to 'mid + 1', if the peak element condition is not met with the inspected element.
                min = mid + 1;
            }
        }

        // returning the value for 'min', as it holds the index value in the end.
        return min;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the array size 'n', and create an array.
        int n = kp.nextInt();
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            arr[i] = kp.nextInt();
        }

        // creating a variable to print and store the value returned by the function.
        int answer = findPeakElement(arr);
        System.out.println(answer);
    }
}