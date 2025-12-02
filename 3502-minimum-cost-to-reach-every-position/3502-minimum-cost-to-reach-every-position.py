class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        minCost = cost[0]
        for i in range(1,len(cost)):
            cost[i] = min(cost[i], minCost)
            minCost = cost[i]
        return cost