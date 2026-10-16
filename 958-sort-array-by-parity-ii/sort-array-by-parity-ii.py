class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1
        n = len(nums)

        while even < n and  odd < n:
            if nums[even] % 2 == 0:
                even += 2

            elif nums[odd] % 2 == 1:
                odd += 2

            else:
                temp = nums[even]
                nums[even] = nums[odd]
                nums[odd] = temp

                even += 2
                odd += 2
        return nums
        