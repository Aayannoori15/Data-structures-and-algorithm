// 58. Length of Last Word  [Easy]
// https://leetcode.com/problems/length-of-last-word/
// runtime 0 ms | memory 41.6 MB

class Solution {
    public int lengthOfLastWord(String s) {
        int a=s.length()-1;
        int count =0;
        for(int i=a;i>=0;i--){
            if(s.charAt(i)!=' '){
                count+=1;
            }
            else if(s.charAt(i)==' '&& count==0){
                continue;
            }
            if(count!=0 && s.charAt(i)==' ' ){
                break;
            }
        }
        return count;
        
    }
}
