class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums: number[]): number {
        if (nums.length === 1) { return nums[0]; }

        function robArr(arr: number[]): number {
            let minus2 = 0;
            let minus1 = 0;
            for (const num of arr) {
                let prev = minus2;
                minus2 = minus1;
                minus1 = Math.max(minus1, prev + num);
            }
            return minus1;
        }

        return Math.max(robArr(nums.slice(1)), robArr(nums.slice(0, nums.length - 1)));
    }
}
