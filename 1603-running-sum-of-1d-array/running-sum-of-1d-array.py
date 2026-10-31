class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        ans = []
        for num in nums:
            total += num
            ans.append(total)
        
        return ans