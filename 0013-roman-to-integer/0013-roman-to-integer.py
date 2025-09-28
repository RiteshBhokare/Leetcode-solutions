class Solution(object):
    def romanToInt(self, s):
        l = list(s)
        total = 0
        prev=""
        for i in range(len(l)):
            curr = l.pop()
            if curr == 'I':
                if prev in ('V','X','L','C','D','M'):
                    total -= 1
                else:
                    total += 1
            elif curr == 'V':
                if prev in ('X','L','C','D','M'):
                    total -= 5
                else:
                    total += 5
            elif curr == 'X':
                if prev in ('L','C','D','M'):
                    total -= 10
                else:
                    total += 10
            elif curr == 'L':
                if prev in ('C','D','M'):
                    total -= 50
                else:
                    total += 50
            elif curr == 'C':
                if prev in ('D','M'):
                    total -= 100
                else:
                    total += 100
            elif curr == 'D':
                if prev == 'M':
                    total -= 500
                else:
                    total += 500
            elif curr == 'M':
                total += 1000
    
            prev=curr
        return total
        
        