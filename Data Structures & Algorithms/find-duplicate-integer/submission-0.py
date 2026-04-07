class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        array=[]
        for i in range(len(nums)):
            if nums[i] not in array:
                array.append(nums[i])
            else:
                return nums[i]
        