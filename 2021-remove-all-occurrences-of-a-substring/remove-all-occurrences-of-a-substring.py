class Solution(object):
    def removeOccurrences(self, s, part):
        while s.find(part) != -1:
            idx = s.find(part)
            s = s[:idx] + s[idx + len(part):]
        return s
        