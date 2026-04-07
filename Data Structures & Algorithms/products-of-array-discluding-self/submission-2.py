class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        var=1

        prefix[0]=suffix[n-1]=1
        
        for i in range(1,n):
            prefix[i]=nums[i-1]*prefix[i-1]

        for j in range(n-2,-1,-1):
            var*=nums[j+1]
            prefix[j]=prefix[j]*var

        return prefix