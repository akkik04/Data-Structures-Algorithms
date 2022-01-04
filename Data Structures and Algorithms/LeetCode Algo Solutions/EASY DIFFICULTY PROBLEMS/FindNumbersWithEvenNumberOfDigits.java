// FIND NUMBERS WITH EVEN NUMBER OF DIGITS LEETCODE SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class FindNumbersWithEvenNumberOfDigits{

    // creating a function to count the number of elements with even number of digits.
    public static int countEvenDigitElements(int arr[]) {

        // creating a variable to track the total digits in an element. 
        int digitCount = 0;

        // creating a variable to track the number of elements with even number of digits.
        int counter = 0;

        // creating a for-loop to iterate for the length of the array.
        for (int i=0; i < arr.length; i++){

            // creating a variable to tie the current element.
            int curr_el = arr[i];

            // creating a while-loop to find the total number of digits in the element.
            while (curr_el != 0){

                // incrementing the 'digitCount' after each iteration.
                curr_el /= 10;
                digitCount++;
            }

            // creating an if-statement to check if the element has an even number of digits.
            if (digitCount % 2 == 0){

                // code to increment the 'counter' if the condition is met.
                counter++;
            }

            // code to set the 'digitCount' back to '0' for processing the next element in the array.
            digitCount = 0;
        }

        // returning the counter storing the number of elements with even digits.
        return counter;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the array size.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to iterate for the length of the array, taking input for each index.
        for (int i=0; i < arr.length; i++){

            // code to receive input for each index.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = countEvenDigitElements(arr);
        System.out.println(answer);
    }
}
