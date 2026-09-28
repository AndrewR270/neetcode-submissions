class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n: number): number {
        if (n <= 2) { return n; }

        let a = 1;
        let b = 2;

        for (let i = 3; i <= n; i++) {
            const temp = a;
            a = b;
            b += temp;
        }

        return b;
    }
}
