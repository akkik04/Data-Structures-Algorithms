// FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class FirstAndLastPositionOfElementInSortedArray {

    public static int[] searchRange(int[] arr, int target) {

        // creating an array with a capacity of two for storage of index numbers.
        int[] res = new int[2];

        // initializing both indices of the array to '-1'.
        res[0] = -1;
        res[1] = -1;

        // creating variables to track the left-most, right-most, and midpoint during the search.
        int min = 0;
        int max = arr.length - 1;
        int mid = min + (max - min) / 2;

        // first binary search 
        while (min <= max){

            mid = min + (max - min) / 2;

            // creating an if-statement to check for the midpoint housing the target.
            if (arr[mid] == target){

                // setting the first index of the array to the midpoint.
                res[0] = mid;

                // re-writing the right-most index.
                max = mid - 1;
            }

            // creating an if-statement to check for the value at the midpoint being greater than the target.
            else if (arr[mid] > target){

                // re-writing the right-most index.
                max = mid - 1;
            }

            // creating an if-statement to check for the value at the midpoint being less than the target.
            else if (arr[mid] < target){

                // re-writing the left-most index.
                min = mid + 1;
            }

        }

        // re-initialzing the left-most index, right-most index, and midpoint.
        min = 0;
        max = arr.length - 1;
        mid = min + (max - min) / 2;

        // second binary search.
        while (min <= max){

            mid = min + (max - min) / 2;

            // creating an if-statement to check for the midpoint housing the target.
            if (arr[mid] == target){

                // setting the second index of the array to the midpoint.
                res[1] = mid;

                // re-writing the right-most index.
                min = mid + 1;
            }

            // creating an if-statement to check for the value at the midpoint being greater than the target.
            else if (arr[mid] > target){

                // re-writing the right-most index.
                max = mid - 1;
            }

            // creating an if-statement to check for the value at the midpoint being less than the target. 
            else if (arr[mid] < target){

                // re-writing the left-most index.
                min = mid + 1;
            }
        }

        // returning the array that holds the two indices.
        return res;
    }
  

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired capacity, and taking input for each index of the array.
        int n = kp.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++){

            arr[i] = kp.nextInt();
        }

        // prompting the user for a target value to search for.
        int target = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int[] answer = searchRange(arr, target);
        for (int ele: answer){

            System.out.print(ele);
            System.out.print(" ");
        }
    }
}