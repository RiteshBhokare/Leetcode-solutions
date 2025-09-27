class Solution(object):
    def lengthOfLastWord(self, s):
        s=s[::-1]
        last_word=[]
        freq=0
        for i in s:
            if i != " ":
                last_word.append(i)
                freq+=1
            elif(freq != 0):
                break
        return len(last_word)
        