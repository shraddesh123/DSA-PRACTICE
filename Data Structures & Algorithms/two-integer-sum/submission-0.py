class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_store={}

        for indices, num in enumerate(nums):
            difference= target-num

            if difference in temp_store:
                return [temp_store[difference],indices]
            temp_store[num]=indices