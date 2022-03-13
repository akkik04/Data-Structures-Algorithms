// PUZZLE PIECES EDABIT SOLUTION (JAVA):

public class PuzzlePieces {

    public static boolean puzzlePieces(int[][]n) {

        // checking the base case of the two arrays not having the same length.
        if (n[0].length != n[1].length){

            // returning 'false' if the condition is met.
            return false;
        }

        // storing the initial sum of the two elements from both arrays.
        int initial = n[0][0] + n[1][0];

        // creating a for-loop to check if the same initial sum is not present, indicating that we must return 'false'.
        for (int i = 0; i < n[0].length; i++){

            // creating an if-statement to check for a violation of the requirements. 
            if (n[0][i] + n[1][i] != initial){

                return false;
            }
        }

        // returning 'true' if no obstacles were found.
        return true;
    }
}
