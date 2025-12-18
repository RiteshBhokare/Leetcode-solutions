class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        # for i in num:
            # print(i)
        num.sort()
        return int(num[0]+num[3])+int(num[1]+num[2])