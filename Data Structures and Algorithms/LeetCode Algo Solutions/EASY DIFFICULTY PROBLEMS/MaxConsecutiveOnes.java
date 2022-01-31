// MAX CONSECUTIVE ONES LEETCODE SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class MaxConsecutiveOnes {

    // creating a function to find the maximum number of ones, given an array as a parameter.
    public static int findMaxConsecutiveOnes(int arr[]) {

        // creating a variable to store the count of consecutive ones.
        int count = 0;

        // creating a variable to store the maximum count of consecutive ones.
        int maxCount = 0;

        // creating a for-loop to iterate for the length of the array.
        for (int i=0; i < arr.length; i++){

            // creating an if-statement to check if the current element is a '1'.
            if (arr[i] == 1){

                // code to increment the count variable, as '1' is found.
                count++;

                // creating an if-statement to **ONLY** increment the 'maxCount' if the initial count is greater than the stored maximum.
                if (count > maxCount){

                    // code to set the value of 'maxCount' to 'count', as a new maximum is found.
                    maxCount = count;
                }
            }

            // checking if '0' is detected at an index instead of '1'.
            else {

                // code to re-set the count variable to one, as the consecutive pattern is interrupted.
                count = 0;
            }
        }

        // returning the value of the maximum number of consecutive ones in an array.
        return maxCount;  
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the array's capacity.
        int n = kp.nextInt();

        // creating an array of desired capacity.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // taking input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = findMaxConsecutiveOnes(arr);
        System.out.println(answer);
    }
}