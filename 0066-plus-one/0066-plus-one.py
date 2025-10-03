class Solution(object):
    def plusOne(self, digits):
        #to convert the list into a single string
        num = ""
        for dig in digits:
            num += str(dig)
        #converting string into integer and then adding 1 and again converting into string to iterate on it
        newNumStr = str(int(num) + 1)
        ret =[]
        for i in newNumStr:
            #converting into integer and storing into list
            ret.append(int(i))
     
        return ret
        