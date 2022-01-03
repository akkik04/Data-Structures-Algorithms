// COUNTING THE NUMBER OF ONES IN THE BINARY REPRESENTATION OF AN INTEGER EDABIT SOLUTION (JAVA).

// importing the scanner object.
import java.util.Scanner;

public class OnesInBinaryRepresentation {

    // creating a function to find the number of '1' in the binary representation of a given integer.
    public static int countOnes(int num) {

        // creating a variable to convert the integer to its respective binary string.
        String bin_string = Integer.toString(num, 2);

        // creating a variable to count the '1' in the binary representation.
        int count = 0;

        // creating a for-loop to iterate for the binary string.
        for (int i=0; i < bin_string.length(); i++){

            // code to determine the current character.
            char c = bin_string.charAt(i);

            // creating an if-statement to check if the current character is a '1'.
            if (c == '1'){

                // code to increment the count, as the condition is met.
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

        // creating a variable to take input for the number.
        int num = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = countOnes(num);
        System.out.println(answer);
    }
}