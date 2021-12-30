// FIND NUMBERS WITH EVEN NUMBER OF DIGITS LEETCODE SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class FindNumbersWithEvenNumberOfDigits {

    // creating a function to find the count of even digits in a given array.
    public static int evenDigits(int arr[]) {

        // creating a variable to track the count of even digit elements.
        int count = 0;

        // creating a for-loop to iterate for the length of the array.
        for (int j=0; j < arr.length; j++){

            // creating an if-statement to check for elements that have even number of digits.
            if (String.valueOf(arr[j]).length() % 2 == 0){

                // code to increment the count if the condition is satisfied.
                count++;
            }
        }
        
        // returning the value of the count.
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

        // creating a for-loop to iterate for the length of the array to take input for each index.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = evenDigits(arr);
        System.out.println(answer);
    }
}