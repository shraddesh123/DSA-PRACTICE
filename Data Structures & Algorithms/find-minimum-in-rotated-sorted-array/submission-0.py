class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum=float('inf')
        n=len(nums)

        low=0
        high=n-1

        while low<= high:
            mid=low+(high-low)//2

            minimum=min(minimum,nums[mid])

            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1

        return minimum