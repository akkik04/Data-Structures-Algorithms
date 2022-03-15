// ELIMINATE ODD NUMBERS IN AN ARRAY EDABIT SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class EliminateOddNumbers {

    public static int[] filterOutEvens(int[] nums) {

        // counting the number of even elements within the array.
        int count = 0;
        for (int i = 0; i < nums.length; i++){

            if (nums[i] % 2 == 0){

                count++;
            }
        }

        // creating an array that holds the count of even elements.
        int[] arr = new int[count];

        // creating a counter variable.
        int x = 0;

        // creating a for-loop to filter out the even numbers and add them to the new array.
        for (int j = 0; j < nums.length; j++){

            if (nums[j] % 2 == 0){

                arr[x] = nums[j];
                x++;
            }
        }

        // returning the array that contains only the even elements.
        return arr;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);
        
        // creating an array of desired length.
        int n = kp.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++){

            nums[i] = kp.nextInt();
        }

        // creating a variable to store and print the array returned by the function.
        int[] answer = filterOutEvens(nums);
        for (int ele: answer){

            System.out.print(ele);
            System.out.print(" ");
        }
    }
}