// 55. Jump Game  [Medium]
// https://leetcode.com/problems/jump-game/
// runtime 2 ms | memory 45.7 MB

class Solution {
    public boolean canJump(int[] nums) {
        boolean a=false;
        int max=0;
        for(int i=0;i<nums.length&&i<=max;i++){
            max=Math.max(max,nums[i]+i);
            if(max>=nums.length-1){
                a=true;
                break;
            }
        }
        return a;
    }
}
