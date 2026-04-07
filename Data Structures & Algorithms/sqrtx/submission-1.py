class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        while l <= r:
            mid = l + (r - l) // 2

            if mid**2 > x:
                r = mid - 1
            elif mid**2 <= x:
                res = mid
                l = mid + 1

        return res