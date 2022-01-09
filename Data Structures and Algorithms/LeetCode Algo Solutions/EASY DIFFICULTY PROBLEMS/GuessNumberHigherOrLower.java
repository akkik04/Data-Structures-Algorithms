// GUESS NUMBER HIGHER OR LOWER LEETCODE SOLUTION (JAVA):

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number   ----------> Leetcode Problem Notes.
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

public class GuessNumberHigherOrLower {

    public int guessNumber(int n){

        // declaring the leftmost and rightmost indexes.
        int min = 1;
        int max = n;

        // creating a while-loop to perform the binary search.
        while (min <= max){

            // creating a variable to find the midpoint for each search that occurs.
            int mid = min + (max - min) / 2;

            // creating a variable to store the result returned by the 'guess API' when 'mid' is passed as a paremeter.
            int res = guess(mid);

            // creating an if-statement to check if the midpoint is the correct guess.
            if (res == 0){

                // returning the midpoint value if the condition is met.
                return mid;
            }

            else if (res == -1){

                // if the number is lower than the guess number, we re-write the rightmost index to 'mid - 1' (simply cutting out a half of possibilities if required).
                max = mid - 1;
            }

            else {

                // if the number is higher than the guess number, we re-write the leftmost index to 'mid + 1' (simply cutting out the other half of possibilities if required).
                min = mid + 1;
            }
        }

        // returning -1.
        return -1;
    }
}