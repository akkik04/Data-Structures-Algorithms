// WAR OF NUMBERS EDABIT SOLUTION:

// importing the scanner class.
import java.util.Scanner;

public class WarOfNumbers {

    // creating a function to find the difference between the sum of the even and odd numbers.
    public static int warOfNumbers(int arr[]) {

        // creating variables to store the sum of the even numbers and odd numbers.
        int evenSum = 0;
        int oddSum = 0;

        // creating a for-loop to iterate for the length of the array, analyzing the parity of each element.
        for (int i=0; i < arr.length; i++){

            // creating an if-statement to check the parity of each element.
            if (arr[i] % 2 == 0){

                // adding the even element to the even sum.
                evenSum += arr[i];
            }

            else {

                // adding the odd element to the odd sum.
                oddSum += arr[i];
            }
        }

        // returning the difference between the even and odd sum.
        return Math.abs(oddSum - evenSum);
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the array's size.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // code to take input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = warOfNumbers(arr);
        System.out.println(answer);
    }
}