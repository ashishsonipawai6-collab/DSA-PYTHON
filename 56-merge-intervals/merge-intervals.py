class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort()

        l = len(intervals)
        ans = [intervals[0]]
        

        for i in range(1, l):
            last_intervals = ans[-1]

            if last_intervals[1] >= intervals[i][0]:
                last_intervals[1] = max(last_intervals[1], intervals[i][1])

            else:
                ans.append(intervals[i])

        return ans
