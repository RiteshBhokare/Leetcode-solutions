class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        su = 0
        n = str(n)
        for ele in n:
            curr = int(ele)
            su += curr
            mul *=curr
        return mul - su