class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = 0
        count = 0
        m = {0: 1}

        for num in nums:
            prefix += num

            if prefix - k in m:
                count += m[prefix - k]

            m[prefix] = m.get(prefix, 0) + 1

        return count     