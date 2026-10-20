// 88. Merge Sorted Array  [Easy]
// https://leetcode.com/problems/merge-sorted-array/
// runtime 2 ms | memory 42.2 MB

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
     int myArr[] = new int[m+n];
     for(int i=0;i<m;i++){
            myArr[i]=nums1[i];
        }
     for(int i=0;i<n;i++){
            myArr[m]=nums2[i];
            m++;
        }
        for(int i=0;i<myArr.length;i++){
          nums1[i]=myArr[i];
        }
        for(int i=0;i<nums1.length-1;i++){
            for(int j=0;j<nums1.length-1-i;j++){
                if(nums1[j]>nums1[j+1]){
                    int temp=nums1[j];
                    nums1[j]=nums1[j+1];
                    nums1[j+1]=temp;
                }
            }
        }

    }
}
