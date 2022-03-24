// CUMULATIVE ARRAY SUM EDABIT SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class CumulativeArraySum {

    public static int[] cumulativeArraySum(int[] arr) {

        // creating a variable to track the sum.
        int sum = 0;

        // creating a 'temp' array.
        int[] temp = new int[arr.length];

        // creating a for-loop to find the cumulative sum.
        for (int i = 0; i < arr.length; i++){

            // adding the current element's value to the sum's gathered from before.
            sum += arr[i];

            // tying the element to the sum.
            temp[i] = sum;
        }

        // returning the 'temp' array that contains the cumulative sum of the elements.
        return temp;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired capacity, with input from the user for the elements.
        int n = kp.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++){

            arr[i] = kp.nextInt();
        }

        // creating an array variable to store and print the value returned by the function.
        int[] answer = cumulativeArraySum(arr);
        for (int ele: answer){

            System.out.print(ele);
            System.out.print(" ");
        }
    }
}