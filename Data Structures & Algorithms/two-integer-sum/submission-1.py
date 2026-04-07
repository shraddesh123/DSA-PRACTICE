class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}

        for index,num in enumerate(nums):
            remaining=target-num

            if remaining in temp:
                return [temp[remaining],index]
                
            temp[num]=index