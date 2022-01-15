// LARGEST GAP EDABIT SOLUTION (JAVA):

// importing the required classes.
import java.util.Scanner;
import java.util.Arrays;

public class LargestGap {
    
    // creating a function to find the largest gap within the array.
    public static int largestGap(int arr[]) {

        // sorting the array using the imported class.
        Arrays.sort(arr);

        // creating a variable to store the largest gap.
        int largestGap = 0;

        // creating a for-loop to iterate for the length of the array.
        for (int i=0; i < arr.length - 1; i++){

            // creating an if-statement to check if the current gap is greater than the stored 'largestGap'. 
            if (arr[i + 1] - arr[i] > largestGap){

                // code to set the largest gap as the current gap, if the condition is met.
                largestGap = arr[i + 1] - arr[i];
            }
        }

        // returning the largest gap's value.
        return largestGap;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the size of the array.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for(int i=0; i < arr.length; i++){

            // taking input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = largestGap(arr);
        System.out.println(answer);
    }
}