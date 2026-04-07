class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum=1
        n=len(nums)
        if n ==0:
            return 0
        nums=sorted(nums)
        current=1
        for i in range(1,n):
            
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]-nums[i-1]==1:
                current+=1
            else:
                current=1
            maximum=max(current,maximum)


        return maximum