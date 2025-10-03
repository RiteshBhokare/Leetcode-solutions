class Solution(object):
    def plusOne(self, digits):
        num = ""
        for dig in digits:
            num += str(dig)
        numStr = str(int(num) + 1)
        ret =[]
        for i in numStr:
            ret.append(int(i))
     
        return ret
        