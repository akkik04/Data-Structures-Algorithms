// Kth MISSING POSITIVE NUMBER LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class KthMissingPositiveNumber {

    // creating a function to find the 'Kth positive integer'.
    public static int findKthPositive(int arr[], int k) {

        // creating variables to track the leftmost and rightmost index.
        int min = 0;
        int max = arr.length - 1;

        // creating a while-loop to perform the binary search.
        while (min <= max){

            // creating a variable to store the midpoint of the search space after every iteration.
            int mid = min + (max - min) / 2;

            // creating an if-statement to check the difference between the element at the midpoint and the natural number at that position.
            if (arr[mid] - (mid + 1) < k){

                // code to move the leftmost index to the 'midpoint + 1', simply cutting out a half of search space that is negligible.
                min = mid + 1;

            }

            else {

                // code to move the rightmost index to the 'midpoint - 1', simply cutting out a half of search space that is negligible.
                max = mid - 1;
            }
        }

        // returning the 'minimum + k', as it stores the value for the missing number.
        return min + k;
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

            // taking input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // taking input for the 'Kth' integer, as we perform the search based on that.
        int k = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = findKthPositive(arr, k);
        System.out.println(answer);
    }
}