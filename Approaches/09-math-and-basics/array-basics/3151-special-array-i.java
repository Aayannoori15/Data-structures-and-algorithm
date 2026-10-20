// 3151. Special Array I  [Easy]
// https://leetcode.com/problems/special-array-i/
// runtime 1 ms | memory 43.3 MB

class Solution {
    public boolean isArraySpecial(int[] nums) {
        boolean b=false;
        if(nums.length==1){
            return true;
        }
        else
          for(int i=0;i<nums.length-1;i++){
            int j=i+1;
                if(nums[i]%2==0 && nums[j]%2!=0){
                    b=true;
                }
                else if(nums[i]%2!=0 && nums[j]%2==0){
                    b=true;
                   }   
                else{
                    b=false;
                    break;
                }
             }
             return b;
          }
    }
