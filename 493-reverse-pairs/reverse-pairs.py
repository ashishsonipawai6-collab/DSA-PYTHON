class Solution(object):
    def reversePairs(self, nums):

        def merge_sort(arr):
            if len(arr) <= 1:
                return 0

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            count = merge_sort(left)
            count += merge_sort(right)

            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j

            i = 0
            j = 0
            temp = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    j += 1

            temp.extend(left[i:])
            temp.extend(right[j:])

            arr[:] = temp
            return count

        return merge_sort(nums)