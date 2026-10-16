class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = 0
        odd =  len(nums) - 1

        while even < odd :
            if(nums[even] % 2 == 0):
                even += 1
            elif  (nums[odd] % 2 == 1):
                odd -= 1
            else:
                temp = nums[even]
                nums[even] = nums[odd]
                nums[odd] = temp
                even += 1
                odd -= 1
        return nums