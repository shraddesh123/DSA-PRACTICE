class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()

        for i,val in enumerate(nums):
            if i>0 and nums[i-1]==val:
                continue

            l=i+1
            r=n-1

            while l < r:
                threeSome=val+nums[l]+nums[r]
                if threeSome<0:
                    l+=1
                elif threeSome>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l < r:
                        l+=1
        return res




