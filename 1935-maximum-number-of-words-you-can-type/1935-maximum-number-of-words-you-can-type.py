class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)
        l = text.split(" ")
        cnt =0
        for word in (l):
            for ele in word:
                if ele in brokenLetters:
                    cnt += 1
                    break
        return len(l) - cnt 