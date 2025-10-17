class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longestOne = 0
        longestZero = 0
        currLongOne = 0
        currLongZero = 0
        for i in s:
            if i == '1':
                currLongOne += 1
                currLongZero = 0
                if currLongOne > longestOne :
                    longestOne = currLongOne
            else:
                currLongOne = 0
                currLongZero +=1
                if currLongZero > longestZero:
                    longestZero = currLongZero
        return longestOne > longestZero