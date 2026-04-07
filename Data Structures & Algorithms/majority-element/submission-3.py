class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res={}

        for num in nums:
            if num in res:
                res[num]+=1
            else:
                res[num]=1
        
        median=len(nums)//2

        for num in res:
            if res[num] > median:
                return num