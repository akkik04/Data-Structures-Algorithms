// TWO SUM II LEETCODE SOLUTION (JAVA):

// importing the scanner and array class.
import java.util.Scanner;
import java.util.Arrays;

public class TwoSumII {

    // creating a function with parameters as the array and target.
    public static int[] twoSumII(int arr[], int target) {

        // creating variables to act as left and right pointers.
        int min = 0;
        int max = arr.length - 1;

        // creating a while-loop to find two values that sum to the desired target.
        while (min < max){

            // creating an if-statement to check for the 'min + max' being greater than the target.
            if (arr[min] + arr[max] > target){

                // decreasing the right pointer, as the sum is greater than the target.
                max--;
            }

            // if the 'min + max' is less than the target.
            else if (arr[min] + arr[max] < target){

                // code to increase the left pointer, as the sum is lower than the target, indicating that a higher value is necessary.
                min++;
            }

            else {

                // if the sum of the pointers is equal to the target, we return their '1-indexed' values.
                return new int[]{min + 1, max + 1};
            }
        }

        // returning null;
        return null;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the capacity of the array.
        int n = kp.nextInt();

        // creating an array of desired capacity.
        int arr[] = new int[n];

        // creating a for-loop to iterate for the length of the array, taking input for each index.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to take input for the target value.
        int target = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer[] = twoSumII(arr, target);

        // code to print the array in appropriate format.
        System.out.println(Arrays.toString(answer));
    }
}
