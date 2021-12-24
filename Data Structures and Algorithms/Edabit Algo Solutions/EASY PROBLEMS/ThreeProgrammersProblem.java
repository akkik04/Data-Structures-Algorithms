// THREE PROGRAMMERS PROBLEM EDABIT SOLUTION (JAVA):

// importing scanner object.
import java.util.Scanner;

public class ThreeProgrammersProblem {

    // creating an integer function with the three salaries as parameters.
    public static int programmers(int one, int two, int three) {

        // creating variables, initializing the lowest salary as the first integer, and the highest salary as the last integer.
        int min = one;
        int max = three;

        // creating an array with the three salaries as elements.
        int arr[] = {one, two, three};

        // creating a for-loop to iterate for the three salaries.
        for(int i=0; i < 3; i++) {

            // creating a nested if-statement to check for any salaries in the array being greater than the initialized 'max'. 
            if (arr[i] > max){

                // setting the new max.
                max = arr[i];
            }
            
            // checking for salaries in the array that are lower than the initialized 'min'.
            else if (arr[i] < min){

                // setting the new min.
                min = arr[i];
            }

        }

        // returning the difference between the 'max' and 'min' salaries.
        return(max - min);
    }
    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object for user input.
        Scanner kp = new Scanner(System.in);

        // creating three variables to act as three integer salaries.
        int one = kp.nextInt();
        int two = kp.nextInt();
        int three = kp.nextInt();

        // creating a variable to print out the answer given through the function.
        int answer;

        // calling the function.
        answer = programmers(one, two, three);
        System.out.println(answer);
    }
}