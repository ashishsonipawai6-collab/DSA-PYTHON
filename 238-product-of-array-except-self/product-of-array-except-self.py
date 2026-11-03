class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(1, n):
            prefix *=  nums[i-1]
            ans[i] *= prefix

        suffix = 1
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix

        return ans