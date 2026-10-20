// 1492. The kth Factor of n  [Medium]
// https://leetcode.com/problems/the-kth-factor-of-n/
// runtime 1 ms | memory 41.1 MB

class Solution {
    public int kthFactor(int n, int k) {
      int a[]=new int[n];
      int i,j=0;
      for(i=1;i<=n;i++){
        if(n%i==0){
         a[j++]=i;
        }
      }
     if(a[k-1]>=1){
      return a[k-1];
     }
     else if(a.length<k){
        return -1;
     }
     else{
        return -1;
     }
}
}
