// AUTOMORPHIC NUMBERS EDABIT SOLUTION (JAVA):

// importing the required modules.
import java.util.Scanner;

public class SevenBoom {

    // creating a function to pass a boolean value based on the desired number being present.
    public static boolean findSeven(int arr[]) {

        // creating a for-loop to iterate for the length of the array.
        for (int j=0; j < arr.length; j++){

            // code to check if the number '7' is present within any index of the array.
            if (String.valueOf(arr[j]).contains("7")){

                // returning 'true' if the number '7' is present within the array.
                return true;
            }
        }

        // returning 'false' if the number '7' is not present within the array.
        return false;
    }

    // main method.
    public static void main(String[] args) {
        
        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // code to prompt the user for the number of elements in the array.
        System.out.print("Enter the number of elements in the array please: ");
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // receiving input for the elements in the array from the user.
        for (int i=0; i < arr.length; i++){

            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the boolean value returned by the function.
        boolean answer = findSeven(arr);
        System.out.println(answer);
        
    }
}