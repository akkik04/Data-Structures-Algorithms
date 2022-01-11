// FIRST BAD VERSION LEETCODE SOLUTION (JAVA):

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
  
    // creating a function to solve the problem.
    public int firstBadVersion(int n) {
        
        // creating two variables for the leftmost and rightmost indexes.
        int min = 0;
        int max = n;
        
        // creating a while-loop to perform the binary search.
        while (min < max){
            
            // creating a variable to store the midpoint for every search space.
            int mid = min + (max - min) / 2;
            
            // creating an if-statement to check if the condition with the API is met 
            if (isBadVersion(mid) == true){
                
                // re-writing the right-most index as the midpoint, as we know that everything after is 'bad'.
                max = mid; 
            }
            
            else {
                
                // re-writing the left-most index as the 'midpoint + 1', as we know that we must find the first 'bad' version.
                min = mid + 1;
            }
        }
        
        // returning the 'min', as it stores the first bad version.
        return min;
    }
}
