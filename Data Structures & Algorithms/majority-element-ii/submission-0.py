class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]

        n=len(nums)
        one_third=n//3

        hashmap={}

        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

        for num in hashmap:
            if hashmap[num]> one_third:
                ans.append(num)
        return ans