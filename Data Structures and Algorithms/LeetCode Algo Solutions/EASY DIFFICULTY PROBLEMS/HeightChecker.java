// HEIGHT CHECKER LEETCODE SOLUTION (JAVA):

// importing the 'util' package for its uses.
import java.util.*;

public class HeightChecker {

    // creating a function to check for the appropriate increment in height.
    public static int checkingHeight(int arr[]) {

        // creating a temporary array to compare the 'required' indices to the 'given' indices.
        int temp_array[] = new int[arr.length];

        // creating a variable to count the number of incorrectly placed indices.
        int count = 0;

        // creating a for-loop to add the given elements to the temporary array.
        for (int i=0; i < arr.length; i++){

            // adding the same elements.
            temp_array[i] = arr[i];
        }
        
        // sorting the temporary array.
        Arrays.sort(temp_array);

        // creating a for-loop to see difference in indices between the sorted and given array.
        for (int j=0; j < arr.length; j++){

            // creating an if-statement to check for incorrectly placed indices.
            if (arr[j] != temp_array[j]){

                // code to increment the count if the condition is met.
                count++;
            }
        }

        // returning the count.
        return count;
    }

    // main method.
    public static void main(String[] args) {
        
        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the length of the array.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the desired array.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = checkingHeight(arr);
        System.out.println(answer);
    }
}