class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int minus2 = 0;
        int minus1 = 0;

        for (int i = 2; i <= cost.length; i++) {
            int curr = Math.min(minus2 + cost[i-2], minus1 + cost[i-1]);
            minus2 = minus1;
            minus1 = curr;
        }

        return minus1;
    }
}
