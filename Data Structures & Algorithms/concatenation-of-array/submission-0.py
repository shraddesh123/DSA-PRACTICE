class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)

        ans=[0]*(2*n)

        j=n

        for i in range(n):
            ans[i]=nums[i]
            ans[j]=nums[i]
            j+=1
        return ans