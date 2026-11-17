class Solution(object):
    def isAnagram(self, s, t):
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        count = [0] * 26
        for i in range(n1):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if count[i] != 0:
                return False
        return True      