class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
 
        window=set()
        i=0

        for j in range(len(nums)):
            if nums[j] in window:
                return True

            window.add(nums[j])

            if len(window)>k:
                window.remove(nums[i])
                i+=1

        return False