// LARGEST EVEN NUMBER IN AN ARRAY:

import java.util.Scanner;

public class LargestEvenNumberInArray {
    public static void main(String[] args) {

        Scanner kp = new Scanner(System.in);

        int largestEven = 0;
        System.out.print("Enter the length of the desired array please: ");
        int arrlength = kp.nextInt();
        int arr[] = new int[arrlength];

        System.out.print("Enter the array elements please: ");
        for (int i=0; i < arr.length; i++){

            arr[i] = kp.nextInt();
        }

        for (int j=0; j < arr.length; j++){

            if ((arr[j] % 2 == 0) && (arr[j] > largestEven)){

                largestEven = arr[j];
            }
        }

        System.out.println("The largest even number in the given array is: "+ largestEven); 
    }
}