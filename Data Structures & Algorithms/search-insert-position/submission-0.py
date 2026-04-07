class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i=0
        j=n-1
        res=n

        while i <= j:

            mid=i+(j-i)//2

            if nums[mid]>=target:
                res=mid
                j=mid-1
            else:
                i=mid+1
        return res