from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        majority=n//2
        count=Counter(nums)
        for num in count:
            if count[num]> majority:
                return num
