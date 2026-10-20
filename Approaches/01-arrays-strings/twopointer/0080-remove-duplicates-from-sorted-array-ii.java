// 80. Remove Duplicates from Sorted Array II  [Medium]
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
// runtime 1 ms | memory 46.6 MB

class Solution {
    public int removeDuplicates(int[] nums) {
        int k=0;
        int expectednums[]=new int[nums.length];
        for (int i=0;i<nums.length;i++){
            if(i==0){
                expectednums[k]=nums[i];
                k++;
            }
            else if(i==nums.length-1){
              expectednums[k]=nums[i];
                k++;
            }
          else  if(nums[i]!=nums[i-1]){
             expectednums[k]=nums[i];
            k++;
           }
           else if(nums[i]!=nums[i+1]){
             expectednums[k]=nums[i];
            k++;
           }
           else if(nums[i]==nums[i+1]&&nums[i]==nums[i-1]){
            continue;
           }
        }
        for(int i=0;i<nums.length;i++){
            nums[i]=expectednums[i];
        }
        return k;
    }
}
