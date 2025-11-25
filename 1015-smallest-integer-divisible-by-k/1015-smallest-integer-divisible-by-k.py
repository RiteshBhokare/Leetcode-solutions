class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%10 not in {1,3,7,9}:
            return -1
        res = 0
        for i in range(1, k+1):
            res = (res * 10 + 1) % k
            if not res:
                return i