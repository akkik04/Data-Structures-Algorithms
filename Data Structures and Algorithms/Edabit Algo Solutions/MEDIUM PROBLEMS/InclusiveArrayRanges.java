// INCLUSIVE ARRAY RANGES EDABIT SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class InclusiveArrayRanges {

    // creating a function to create the array of numbers from the desired start integer to the desired end integer.
    public static int[] inclusiveArray(int startNum, int endNum) {

        // creating a variable to track the total number of elements in the array.
        int numofVals = endNum - startNum + 1;

        // creating an array of appropriate length.
        int arr[] = new int[numofVals];

        // creating an if-statement to check for the start number being greater than the end number.
        if (startNum >= endNum){

            // returning the 'start number' if the condition is met.
            return new int[]{startNum};
        }

        // creating a for-loop to iterate for the length of the desired array of integers.
        for (int i=0; i < arr.length; i++){

            // initializing the first element as the 'start number' and progressing by '1' each time until the 'end number'.
            arr[i] = startNum;
            startNum++;
        }

        // returning the array with the numbers present within the desired range.
        return arr;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object for user input.
        Scanner kp = new Scanner(System.in);

        // creating two variables to store the input from the user regarding the 'start' and 'end' values of the array.
        int startNum = kp.nextInt();
        int endNum = kp.nextInt();

        // creating a variable as an array of 'int-type' to store the output from the function.
        int[] answer; 

        // calling the function to store its returned value in the 'answer' variable.
        answer = inclusiveArray(startNum, endNum);
        
        // creating a for-loop to print the array that is present in the 'answer' variable.
        for (int element: answer){

            System.out.print(element);
            System.out.print(" ");
        }
    }
}