class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        charset = set()
        maxlength = 0

        while right < len(s):
            if s[right] not in charset:
                charset.add(s[right])
                maxlength= max(maxlength, right - left + 1)
                right += 1
            else:
                charset.remove(s[left])
                left += 1

        return maxlength

        