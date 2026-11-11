class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1

    #first non negative index
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        neg = left

    # first positive index
        left = 0
        right = n-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
        pos = n - left

        
        return max(neg, pos)