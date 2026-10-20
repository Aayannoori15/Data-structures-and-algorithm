// 9. Palindrome Number  [Easy]
// https://leetcode.com/problems/palindrome-number/
// runtime 4 ms | memory 44.6 MB

class Solution {
    public boolean isPalindrome(int x) {
        int b=x;
        int temp=0;
        while(b>0){
              temp=temp*10;
            temp=temp+(b%10);
          
            b=b/10;
           
        }
        if(temp==x){
            return true;
        }
        else {
            return false;
        }
    }
}
