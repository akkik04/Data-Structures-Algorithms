// NUMBER OF STUDENTS DOING HOMEWORK AT A GIVEN TIME LEETCODE SOLUTION (JAVA):

// importing the scanner class.
import java.util.Scanner;

public class NumberOfStudentsDoingWork {

    // creating a function to find the count of students working during the query.
    public static int busyStudent(int startTime[], int endTime[], int queryTime) {

        // creating a variable to count the number of students doing work during the query.
        int count = 0;

        // creating a for-loop to iterate through the same index in both arrays.
        for (int i=0; i < startTime.length; i++){

            // creating an if-statement to check if the 'queryTime' falls between the interval that is created by both arrays' indexes.
            if (queryTime >= startTime[i] && queryTime <= endTime[i]){

                // code to increment the count variable if the condition is met.
                count++;
            }
        }

        // returning the value of count.
        return count;
    }

    // main method.
    public static void main(String[] args) {

        // instantiating the scanner object.
        Scanner kp = new Scanner(System.in);

        // code to take input for the length of the arrays (startTime.length == endTime.length).
        int n = kp.nextInt();

        // creating arrays for the start and end times.
        int startTime[] = new int[n];
        int endTime[] = new int[n];

        // creating for-loops to take input for each index of the array.
        for (int i=0; i < startTime.length; i++){

            startTime[i] = kp.nextInt();
        }

        for (int j=0; j < endTime.length; j++){

            endTime[j] = kp.nextInt();
        }

        // creating a variable to take input for 'queryTime'.
        int queryTime = kp.nextInt();

        // creating a variable to store and print the value returned by the function.
        int answer = busyStudent(startTime, endTime, queryTime);
        System.out.println(answer);
    }
}