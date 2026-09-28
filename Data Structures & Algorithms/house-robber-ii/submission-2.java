class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) { return nums[0]; }

        return Math.max(
            robArr(Arrays.copyOfRange(nums, 1, nums.length)),
            robArr(Arrays.copyOfRange(nums, 0, nums.length - 1))
        );
    }

    public int robArr(int[] arr) {
        int minus2 = 0;
        int minus1 = 0;
        for (int num : arr) {
            int prev = minus2;
            minus2 = minus1;
            minus1 = Math.max(minus1, prev + num);
        }
        return minus1;
    }
}
