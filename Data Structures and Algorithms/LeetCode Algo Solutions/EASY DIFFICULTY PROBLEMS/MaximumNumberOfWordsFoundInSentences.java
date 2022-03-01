// MAXIMUM NUMBER OF WORDS FOUND IN SENTENCES LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class MaximumNumberOfWordsFoundInSentences {

    // creating a function to solve the problem.
    public static int maxWordsInSentence(String[] sentences) {

        // creating a variable to store the maximum count of words in a sentence.
        int maxCount = 0;

        // creating a for-loop to iterate for the sentences within the array.
        for (String s: sentences){

            // creating an array to split the sentence at the current index into its respective words. 
            String[] word_arr = s.split(" ");

            // creating an if-statement to find the maximum number of words, upon several iterations.
            if (word_arr.length > maxCount){

                maxCount = word_arr.length;
            }
        }

        // returning the maximum count of words.
        return maxCount;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired capacity.
        int n = kp.nextInt();
        String[] sentences = new String[n];

        // taking input for each index of the array.
        for (int i = 0; i < n; i++){

            sentences[i] = kp.nextLine();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = maxWordsInSentence(sentences);
        System.out.println(answer);
    }
}