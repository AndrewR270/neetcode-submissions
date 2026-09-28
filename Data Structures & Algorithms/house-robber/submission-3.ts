class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        if (nums.length === 1) { return nums[0]; }

        let minus2 = nums[0];
        let minus1 = Math.max(nums[0], nums[1]);

        for (let i = 2; i < nums.length; i++) {
            let curr = Math.max(minus1, minus2 + nums[i]);
            minus2 = minus1;
            minus1 = curr;
        }

        return minus1;
    }
}
