class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # res = 0
        # i = 1
        # colors = list(colors)
        # while i < len(neededTime):
        #     if colors[i] == colors[i-1]:
        #         curr = min(neededTime[i-1], neededTime[i])
        #         res += curr
        #         if neededTime[i-1] == curr:
        #             colors.pop(i-1)
        #             # colors = colors.replace(colors[i-1], "")
        #             neededTime.pop(i-1)
                    
        #         elif neededTime[i] ==curr:
        #             colors.pop(i)
        #             # colors = colors.replace(colors[i], "")
        #             neededTime.pop(i)
                    
        #         else:
        #             i+=1
        #     else:
        #         i += 1
        # return res

        prevTime = None
        prevColor = None
        res = 0
        for x, y in zip(colors, neededTime):
            if x == prevColor:
                if y > prevTime:
                    res += prevTime
                else:
                    res += y
                    continue
            prevColor = x
            prevTime = y
        return res