// 27. Remove Element  [Easy]
// https://leetcode.com/problems/remove-element/
// runtime 0 ms | memory 42.5 MB

class Solution {
    public int removeElement(int[] nums, int val) {
        int j=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=val){
              nums[j]=nums[i];
              j++;
            }
        }
        return j;

    }
}
