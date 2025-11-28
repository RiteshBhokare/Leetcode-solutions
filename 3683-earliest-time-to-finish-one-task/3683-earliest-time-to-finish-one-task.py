class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(ele[0] + ele[1] for ele in tasks)
        