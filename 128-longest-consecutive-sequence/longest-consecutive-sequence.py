class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                while num + 1 in num_set:
                    count += 1
                    num += 1
                longest = max(longest, count)
        return longest
        