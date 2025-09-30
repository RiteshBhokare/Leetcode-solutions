class Solution(object):
    def longestCommonPrefix(self, strs):
        '''sorting list in lexicographical order'''
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            '''bcoz of sorting, prefix of first ele and last ele will 
            be same for whole list'''
            if (strs[0][i] != strs[-1][i]):
                return prefix
            else: 
                prefix += strs[0][i]
        return prefix
                
        