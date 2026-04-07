class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # slow=0
        # for fast in range(len(nums)):
        #     if nums[fast]!=val:
        #         nums[slow]=nums[fast]
        #         slow+=1
                
        # return slow
            

        tmp=[]

        for num in nums:
            if num != val:
                tmp.append(num)

        n=len(tmp)

        for i in range(n):
            nums[i]=tmp[i]

        return n