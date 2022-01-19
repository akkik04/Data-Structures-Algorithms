// SEARCH INSERT POSITION LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class SearchInsertPosition {

    public static int searchInt(int arr[], int target) {

        // creating two variables to store the leftmost index, and the rightmost index.
        int min = 0;
        int max = arr.length - 1;

        // creating a while-loop to perform the binary search.
        while (min <= max){

            // creating a variable to store the midpoint for every search space.
            int mid = min + (max - min) / 2;

            // creating an if-statement to check if the midpoint contains the target value.
            if (arr[mid] == target){

                // returning the midpoint if the condition is met.
                return mid;
            }

            // verifying if the midpoint is greater than the target.
            else if (arr[mid] > target){

                // if the condition is met, we simply cut out a half of the space, reducing the search space.
                max = mid - 1;
            }

            // verifying if the midpoint is less than the target.
            else if (arr[mid] < target){

                // if the condition is met, we simply cut out another half of the space, reducing the search space.
                min = mid + 1;
            }
        }

        // returning min, as it will store the insert position.
        return min;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // taking input for the length of the array.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a variable to store the target to look for.
        int target = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = searchInt(arr, target);
        System.out.println(answer);
    }
}