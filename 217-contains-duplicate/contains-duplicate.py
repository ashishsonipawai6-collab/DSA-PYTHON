class Solution(object):
    def containsDuplicate(self, nums):
       
        n = len(nums)
        s = set(nums)

        if len(s) < n:
            return True
        else:
            return False

        