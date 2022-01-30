// SEARCH IN ROTATED SORTED ARRAY LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class SearchInRotatedSortedArray {

    // creating a function with the array and the target as parameters.
    public static int rotatedSearch(int arr[], int target) {

        // creating variables to store the left-most and right-most indexes.
        int min = 0;
        int max = arr.length - 1;

        // creating a variable to store the final output with regards to the binary search.
        int x = -1;

        // creating a while-loop to perform the binary search algorithm, with modifications.
        while (min <= max){

            // creating a variable to store the midpoint of each search space.
            int mid = min + (max - min) / 2;

            // creating an if-statement to check for the target being found at an index in the array.
            if (arr[mid] == target){

                // setting the final output variable 'x' to the value of the midpoint, as the target is there.
                x = mid;
            }

            // as the array is rotated, we must modify the traditional binary search algorithm.
            // creating an if-statement to check if the midpoint of the array is greater than the element at the left-most index.
            if (arr[mid] >= arr[min]){

                // creating an if-statement to check if the target is in the space between the left-most index and midpoint.
                if (target >= arr[min] && target <= arr[mid]){

                    // if the condition is met, we know our new search space should be between the left-most index and midpoint.
                    // we discard the useless half of the array, as the target does not reside there.
                    max = mid - 1;
                }

                else {

                    // if the condition is not met, we discard the space between the left-most index and the midpoint.
                    // we set a new left-most index.
                    min = mid + 1;
                }
            }


            else {

                // creating an if-statement to check if the target resided between the midpoint and the right-most index.
                if (target >= arr[mid] && target <= arr[max]){

                    // if the condition is met, we know our new search space should be between the midpoint and the right-most index.
                    // we discard the useless half of the array, as the target does not reside there.
                    min = mid + 1;
                }

                else {

                    // if the condition is not met, we discard the space between the midpoint and the right-most index.
                    // we set a new right-most index.
                    max = mid - 1;
                }

            }


        }

        // returning the final output variable 'x'.
        return x;
        
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the length of the array.
        int n = kp.nextInt();

        // creating an array of desired length;
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store the target value. 
        int target = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = rotatedSearch(arr, target);
        System.out.println(answer);
    }
}