class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l = []
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                total += accounts[i][j]
            l.append(total)
        return max(l)