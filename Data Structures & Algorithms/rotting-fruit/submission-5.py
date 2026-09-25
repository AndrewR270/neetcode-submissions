class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh = 0
        rotten = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                square = grid[r][c]
                if square == 1: fresh += 1
                if square == 2: rotten.append((r, c))
        
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols) 
                        and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))
                        fresh -= 1
            res += 1
        

        return res if fresh == 0 else -1
