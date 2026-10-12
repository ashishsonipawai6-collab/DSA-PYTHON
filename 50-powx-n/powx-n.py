class Solution(object):
    def myPow(self, x, n):
        power = abs(n)
        ans = 1.0

        while power:
            if power % 2 == 1:
                ans *= x

            x *= x
            power //= 2

        if n < 0:
            ans = 1.0 / ans

        return ans