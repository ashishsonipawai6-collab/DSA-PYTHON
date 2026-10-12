class Solution(object):
    def findMissingAndRepeatedValues(self, grid):

        s = set()
        n = len(grid)
        a = 0
        actual_sum = 0

        for i in range(n):
            for j in range(n):
                num = grid[i][j]

                actual_sum += num

                if num in s:
                    a = num
                
                s.add(num)
        expsum = (n * n) * (n*n+1) // 2
        b = expsum + a - actual_sum

        return [a, b]  
