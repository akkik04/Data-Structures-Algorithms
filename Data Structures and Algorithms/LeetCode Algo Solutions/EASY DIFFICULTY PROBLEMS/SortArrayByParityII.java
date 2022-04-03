// SORT ARRAY BY PARITY II LEETCODE SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class SortArrayByParityII {

    public static int[] sortArrayByParityII(int[] nums) {

        // creating counters for storing the index values of even and odd elements.
        int i = 0;
        int j = 1;

        // creating a new array to modify the current elements.
        int[] arr = new int[nums.length];

        // creating a for-loop to filter through the even and odd elements.
        for (int k = 0; k < nums.length; k++){

            // creating a nested if-statement to check for even case.
            if (nums[k] % 2 == 0){

                // tying the even element to the even index in the new array.
                arr[i] = nums[k];

                // incrementing to the next even index for the next occurence of an even element.
                i += 2;
            }

            else {

                // tying the odd element to the odd index in the new array.
                arr[j] = nums[k];

                // incrementing to the next odd index for the next occurence of an odd element.
                j += 2;
            }
        }

        // returning the array.
        return arr;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // taking input for an array.
        int n = kp.nextInt();
        int[] nums = new int[n];

        for (int i = 0; i < n; i++){

            nums[i] += kp.nextInt();
        }

        // creating a variable to store and print the array returned by the function.
        int[] answer = sortArrayByParityII(nums);
        for (int ele: answer){

            System.out.print(ele);
            System.out.print(" ");
        }
    }
}