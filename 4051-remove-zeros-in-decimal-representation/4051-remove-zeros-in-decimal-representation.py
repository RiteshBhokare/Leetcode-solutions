class Solution:
    def removeZeros(self, n: int) -> int:
        n = str(n)
        newStr = ""
        for i in n:
            if i != "0":
                newStr += i

        return int(newStr)