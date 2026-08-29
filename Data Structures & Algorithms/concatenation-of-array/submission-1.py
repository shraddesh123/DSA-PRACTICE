class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[0]*(2*l)
        j=l
        for i in range(l):
            ans[i]=nums[i]
            ans[j]=nums[i]
            j+=1
        return ans