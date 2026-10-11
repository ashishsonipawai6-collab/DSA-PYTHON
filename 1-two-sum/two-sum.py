class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i
             
        