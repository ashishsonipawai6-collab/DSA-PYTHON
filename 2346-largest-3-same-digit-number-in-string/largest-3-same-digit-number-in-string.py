class Solution(object):
    def largestGoodInteger(self, num):
        n = len(num)
        ans = ""
        for i in range(n-3, -1, -1):
            if num[i] == num[i+1] == num[i+2]:
                temp = num[i:i+3]
                if temp > ans:
                    ans = temp
        return ans
        
