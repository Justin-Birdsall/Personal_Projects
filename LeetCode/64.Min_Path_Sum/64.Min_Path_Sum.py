class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Make our grid one size bigger like in class
        # Initialize it with infinity since we are trying to find the smallest path
        # Think of it like 0 basically, I think in theory we could fill with 0's
        # but filling it with inf helps my understanding 
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # Settting the top-left cell to be the starting point since we filled it with inf
        # our inital starting path is 0 not inf
        dp[0][1] = 0
        #Loop through our 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #for the index that we are acessing look at the left and up and take
                #the lesser of the two since we are looking for the minimum path
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        #after we loop through we can just look at the bottom right corner to get the value of the
        #the sum of the min path
        return dp[m][n]
