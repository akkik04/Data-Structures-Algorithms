// CALCULATE THE MEAN EDABIT SOLUTION (JAVA):

// importing the required modules.
import java.util.Scanner;
import java.lang.Math;

public class CalculateTheMean {

    // creating a function to calculate the mean of the given elements.
    public static double CalcMean(int arr[]) {

        // creating a variable to store the sum of each element in the array.
        double sum = 0;

        // creating a for-loop to iterate through the array and find the sum of all elements.
        for (int j=0; j < arr.length; j++){

            // code to add each element to the sum variable.
            sum += arr[j];
        }

        // rounding the sum.
        sum = Math.round(sum * 100.0) / 100.0;

        // returning the 'mean value'.
        return sum / arr.length;
        
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to take input for the array's length.
        System.out.print("Enter the length of the array please: ");
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to iterate for the length of the array, gathering inputted elements from the user.
        for (int i=0; i < arr.length; i++){

            // code to receive input for each index of the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the 'mean value' returned by the function.
        double answer = CalcMean(arr);
        System.out.println(answer);
        
    }
}