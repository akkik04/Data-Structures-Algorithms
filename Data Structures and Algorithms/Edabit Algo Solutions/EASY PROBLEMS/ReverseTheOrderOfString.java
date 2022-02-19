// REVERSE THE ORDER OF A STRING EDABIT SOLUTION:

// importing the scanner object.
import java.util.Scanner;

public class ReverseTheOrderOfString {

    // creating a function to reverse the given string.
    public static String reverseString(String str) {

        // creating a variable to store the reversed version of the string.
        String revS = "";

        // creating a character array of the characters in the inputted string.
        char characters[] = str.toCharArray();

        // creating a for-loop to iterate through the character array from backwards.
        for (int i = characters.length - 1; i >= 0; i--){

            // adding each character from backwards into the reversed string variable.
            revS += characters[i];
        }

        // returning the reversed string.
        return revS;
    }

    // main method.
    public static void main(String[] args) {
        
        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to store the inputted string.
        String str = kp.nextLine();

        // creating a variable to store and print the string returned by the function.
        String answer = reverseString(str);
        System.out.println(answer);
    }
}