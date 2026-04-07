class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = float("inf")
        sums = 0
        for j in range(n):
            sums += nums[j]

            while sums >= target:
                res = min(res, j - i + 1)
                sums -= nums[i]
                i += 1

        return 0 if res == float("inf") else res
