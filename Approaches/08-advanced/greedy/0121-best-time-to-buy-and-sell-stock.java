// 121. Best Time to Buy and Sell Stock  [Easy]
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// runtime 2 ms | memory 61.7 MB

class Solution {
    public int maxProfit(int[] prices) {
        int buy=prices[0];
        int profit=0;
        for (int i=1;i<prices.length;i++){
            if(buy>prices[i]){
                buy=prices[i];
            }
            else if(prices[i]-buy>profit){
               profit= prices[i]-buy;
            }
        }
        return profit;
    }
}
