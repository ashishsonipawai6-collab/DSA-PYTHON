class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = len(height)
        maxWater = 0
        i = 0
        j = h-1

        while i < j:
            width = j - i
            min_height = min(height[i], height[j])
            currWater = width * min_height
            maxWater = max(maxWater, currWater)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxWater 
        