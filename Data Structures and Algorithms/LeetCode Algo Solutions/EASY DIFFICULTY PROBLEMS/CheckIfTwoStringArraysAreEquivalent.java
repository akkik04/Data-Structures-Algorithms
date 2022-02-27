class Solution {
  
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        
        // creating string variables to store the two words.
        String word_x = "";
        String word_y = "";
        
        // detecting the first word.
        for (String s: word1){
            
            word_x += s;
        }
        
        // detecting the second word.
        for (String str: word2){
            
            word_y += str;
        }
        
        // returning if the two string arrays produce equivalent strings.
        return word_x.equals(word_y);
    }
}
