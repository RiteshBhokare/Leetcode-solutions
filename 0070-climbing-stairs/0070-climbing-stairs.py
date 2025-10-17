class Solution:
    def climbStairs(self, n: int) -> int:
       
        dp = []
        dp.append(1)
        for i in range(1,n+1):
            if i == 1:
                dp.append(dp[i-1])
            else:
                dp.append(dp[i-1] + dp[i-2])
        return dp[n]
