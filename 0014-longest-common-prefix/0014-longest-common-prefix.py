class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            if (strs[0][i] != strs[-1][i]):
                return prefix
            else: 
                prefix += strs[0][i]
        return prefix
                
        