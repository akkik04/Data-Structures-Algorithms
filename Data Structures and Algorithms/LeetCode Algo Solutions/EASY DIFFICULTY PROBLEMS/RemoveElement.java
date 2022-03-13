// REMOVE ELEMENT LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class RemoveElement {

    public static int removeElements(int[] arr, int val, int n) {

        // creating a variable to act as a counter for the iteration.
        int i = 0;

        // creating a for-loop to iterate while the counter is less than the length of the array.
        while (i < n){

            // checking for deletion, if the value is met.
            if (arr[i] == val){

                arr[i] = arr[n - 1];
                n--;
            }

            // incrementing the counter.
            else {

                i++;
            }
        }

        // returning the length of the modified array.
        return n;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired length.
        int n = kp.nextInt();
        int[] arr = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i = 0; i < n; i++){

            arr[i] = kp.nextInt();
        }

        // creating a variable to store the value to be searched for.
        int val = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = removeElements(arr, val, n);
        System.out.println(answer);
    }
}