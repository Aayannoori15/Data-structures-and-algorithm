// 2678. Number of Senior Citizens  [Easy]
// https://leetcode.com/problems/number-of-senior-citizens/
// runtime 2 ms | memory 43.3 MB

class Solution {
    public int countSeniors(String[] details) {
       int a,b,c,count=0;
      for(int i=0;i<details.length;i++)  {
        a=Integer.parseInt(details[i].charAt(11)+"");
        b=Integer.parseInt(details[i].charAt(12)+"");
        c=(a*10)+b;
        if(c>60){
            count+=1;
        }
        else{
            continue;
        }
      }
      return count;
    }
}
