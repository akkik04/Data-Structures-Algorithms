// FIND SMALLEST LETTER GREATER THAN TARGET LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class FindSmallestLetterGreaterThanTarget {

    // creating a function to find the smallest letter that is greater than the target character.
    public static char nextGreatestLetter(char arr[], int target) {
        
        // creating a variable to store the smallest letter, setting it to the first element in the array.
        char s = arr[0];
        
        // creating variables to store the leftmost and rightmost indexes.
        int min = 0;
        int max = arr.length - 1;

        // creating a while-loop to perform the binary search.
        while (min <= max){

            // creating a variable to find the midpoint for every search space.
            int mid = min + (max - min) / 2;

            // creating an if-statement to check if the character at the midpoint is '<=' to the target.
            if (arr[mid] <= target){

                // re-writing the leftmost index, as the left-half of the search space is not necessary to search.
                min = mid + 1;
            }

            else {
                
                // if the character at the midpoint is '>' the target, we store that value in our 's' variable.
                s = arr[mid];

                // re-writing the rightmost index.
                max = mid - 1;
            }
        }

        // returning the variable that stores the smallest letter that is greater than the target.
        return s;
    }
    
    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of characters, with input from the user.
        char arr[] = kp.next().toCharArray();

        // code to take input for the target character.
        char target = kp.next().charAt(0);

        // creating a variable to store and print the character returned by the function.
        char answer = nextGreatestLetter(arr, target);
        System.out.println(answer);
    }
}