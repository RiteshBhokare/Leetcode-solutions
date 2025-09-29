class Solution(object):
    def isValid(self, s):
        l=[]
        for i in s:
            if i in ('(', '[', '{'):
                l.append(i)
            else:
                if not l:
                    return False
                top = l.pop()
                if i == ')' and top != '(':
                    return False
                if i == '}' and top != '{':
                    return False
                if i == ']' and top != '[':
                    return False
        return len(l) == 0