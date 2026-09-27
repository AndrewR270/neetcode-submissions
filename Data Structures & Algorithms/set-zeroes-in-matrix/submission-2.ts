class Solution {
    /**
     * @param {number[][]} matrix
     * @return {void}
     */
    setZeroes(matrix: number[][]): void {
        const rows = matrix.length;
        const cols = matrix[0].length;
        const zeroRows = new Set<number>();
        const zeroCols = new Set<number>();

        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (matrix[r][c] == 0) {
                    zeroRows.add(r);
                    zeroCols.add(c);
                }
            }
        }

        for (const r of zeroRows) {
            for (let c = 0; c < cols; c++) {
                matrix[r][c] = 0;
            }
        }

        for (let r = 0; r < rows; r++) {
            for (const c of zeroCols) {
                matrix[r][c] = 0;
            }
        }
    }
}
