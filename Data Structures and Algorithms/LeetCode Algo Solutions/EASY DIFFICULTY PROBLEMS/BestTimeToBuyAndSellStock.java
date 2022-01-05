// BEST TIME TO BUY AND SELL STOCK LEETCODE SOLUTION (JAVA):

// importing the scanner object.
import java.util.Scanner;

public class BestTimeToBuyAndSellStock{

    // creating a function to find how to maximize the profit.
    public static int maxProfit(int arr[]) {

        // creating a variable to store the highest stock price.
        // initializing it to the last element in the array.
        int highestPrice = arr[arr.length - 1];

        // creating a variable to store the maximum profit.
        int maxProfit = 0;

        // creating a for-loop to iterate backwards from the last element finding any greater stock prices.
        for (int i = arr.length - 1; i >= 0; i--){

            // creating an if-statement to check for the highest stock price.
            if (highestPrice < arr[i]){

                // code to set the highest price to the element that was found
                highestPrice = arr[i];
            }

            else {

                // code to find the latest max profit after each iteration.
                maxProfit = Math.max(maxProfit, highestPrice - arr[i]);
            }
        }

        // returning the value of the maximum profit.
        return maxProfit;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // creating a variable to prompt the user for the desired array length.
        int n = kp.nextInt();

        // creating an array of desired length.
        int arr[] = new int[n];

        // creating a for-loop to take input for each index of the array.
        for (int i=0; i < arr.length; i++){

            // code to take input for each element in the array.
            arr[i] = kp.nextInt();
        }

        // creating a variable to store and print the value returned by the function.
        int answer = maxProfit(arr);
        System.out.println(answer);
    }
}