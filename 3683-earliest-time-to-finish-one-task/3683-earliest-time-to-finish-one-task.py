class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = inf
        for ele in tasks:
            res = min(res, ele[0] + ele[1])
        return res