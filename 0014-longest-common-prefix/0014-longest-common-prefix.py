class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        str1 = ""
        for i in range(len(strs[0])):
            le = strs[0]
            ri = strs[-1]
            if (le[i] == ri[i]):
                str1 += le[i]
            else:
                break
        return str1