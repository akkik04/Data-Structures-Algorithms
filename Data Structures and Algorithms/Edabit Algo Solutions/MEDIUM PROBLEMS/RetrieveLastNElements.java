// RETRIEVE THE LAST N ELEMENTS EDABIT SOLUTION (JAVA):

import java.util.Scanner;

public class RetrieveLastNElements {

    // creating a function to retrieve the last 'N' elements.
    public static int[] lastNElements(int[] nums, int n) {

        // returning 'null' if 'N' is greater than the length of the given array.
        if (n > nums.length){

            return null;
        }

        // creating a temporary array of 'N' length.
        int[] temp_arr = new int[n];

        // creating a counter variable.
        int x = 0;

        // creating a for-loop to retrieve the last 'N' elements.
        for (int i = nums.length - n; i < nums.length; i++){

            temp_arr[x] = nums[i];
            x++;
        }

        // returning the temporary array that contains the last 'N' elements.
        return temp_arr;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired length.
        int length = kp.nextInt();
        int[] arr = new int[length];
        
        // creating a for-loop to take input for each index of the array.
        for (int i = 0; i < length; i++){

            arr[i] = kp.nextInt();
        }

        // creating a variable to store the value 'N', telling us how many elements to retrieve.
        int n = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int[] answer = lastNElements(arr, n);
        for (int ele: answer){

            System.out.print(ele);
            System.out.print(" ");
        }
    }
}