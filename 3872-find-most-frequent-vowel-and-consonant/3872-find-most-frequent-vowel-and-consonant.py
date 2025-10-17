class Solution:
    def maxFreqSum(self, s: str) -> int:
        freqVowel = 0
        freqConsonant = 0
        currVowel = 0
        currConsonant = 0
        for i in s:

            if i in ('a','e','i','o','u'):
                currVowel = s.count(i)
                if freqVowel < currVowel :
                    freqVowel = currVowel
            else:
                currConsonant = s.count(i)
                if freqConsonant < currConsonant:
                    freqConsonant = currConsonant
        return freqConsonant + freqVowel
