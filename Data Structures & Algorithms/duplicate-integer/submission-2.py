class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if nums[i]  in hashmap:
                hashmap[nums[i]]+=1
            else:
                hashmap[nums[i]]=1

        for i in hashmap:
            if hashmap[i]>1:
                return True
        return False