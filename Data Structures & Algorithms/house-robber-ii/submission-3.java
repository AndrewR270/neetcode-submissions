class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) { return nums[0]; }

        return Math.max(
            robArr(nums, 1, nums.length),
            robArr(nums, 0, nums.length - 1)
        );
    }

    public int robArr(int[] nums, int start, int end) {
        int minus2 = 0;
        int minus1 = 0;
        for (int i = start; i < end; i++) {
            int prev = minus2;
            minus2 = minus1;
            minus1 = Math.max(minus1, prev + nums[i]);
        }
        return minus1;
    }
}
