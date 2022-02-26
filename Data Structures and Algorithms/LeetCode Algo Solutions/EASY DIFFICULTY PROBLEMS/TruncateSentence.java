// TRUNCATE SENTENCE LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class TruncateSentence {

    public static String truncateSentence(String s, int k) {

        // creating a variable to store the word count within the string.
        int word_c = 0;

        // creating a for-loop to iterate for the length of the string.
        for (int i = 0; i < s.length(); i++){

            // creating a variable to store the current character.
            char c = s.charAt(i);

            // creating an if-statement for word-detection.
            if (c == ' '){

                // incrementing the word counter.
                word_c++;
            }

            // creating an if-statement to check when to break out of iteration.
            if (word_c == k){

                // returning the substring until the desired length.
                return s.substring(0, i);
            }
        }

        // returning the modified string.
        return s;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // code to take input for the required parameters.
        String str = kp.nextLine();
        int max = kp.nextInt();

        // creating a variable to store and print the String returned by the function.
        String answer = truncateSentence(str, max);
        System.out.println(answer);
    }
}