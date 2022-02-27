// KIDS WITH THE GREATEST NUMBER OF CANDIES LEETCODE SOLUTION (JAVA):

// importing the required classes.
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class KidsWithTheGreatestNumberOfCandies {

    // creating a function that returns a boolean list.
    public static List<Boolean> kidsWithCandies(int candies[], int extraCandies) {

        // initializing a list of boolean type.
        ArrayList<Boolean> my_list = new ArrayList<>();

        // algorithm to find the maximum number in the given array.
        int max = candies[0];
        for (int i = 0; i < candies.length; i++){

            if (candies[i] > max){

                max = candies[i];
            }
        }

        // creating a for-loop to add the boolean value upon meeting certain requirements.
        for (int el: candies){

            // adding the corresponding boolean value.
            my_list.add(el + extraCandies >= max);
        }

        // returning the boolean list.
        return my_list;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating an array of desired capacity.
        int n = kp.nextInt();
        int candies[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i = 0; i < n; i++){

            candies[i] = kp.nextInt();
        }

        // creating a variable to store the number of extra candies.
        int extraCandies = kp.nextInt();

        // creating a boolean list to store the output returned by the function.
        List<Boolean> answer = kidsWithCandies(candies, extraCandies);

        // creating a for-loop to print out the list.
        for (boolean i: answer){

            System.out.print(i);
            System.out.print(" ");
        }
    }
}