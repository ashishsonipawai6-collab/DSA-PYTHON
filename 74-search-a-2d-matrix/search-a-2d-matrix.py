class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        startRow = 0 
        endRow = m - 1

        while startRow <= endRow:
            midRow = startRow + (endRow - startRow) // 2

            if target >= matrix[midRow][0] and target <= matrix[midRow][n-1]:
                break
            elif target > matrix[midRow][n-1]:
                startRow = midRow + 1
            else:
                endRow = midRow - 1
        # inside the row
 
        start = 0
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if target == matrix[midRow][mid]:
                return True

            elif target > matrix[midRow][mid]:
                start = mid + 1

            else:
                end = mid - 1

        return False
