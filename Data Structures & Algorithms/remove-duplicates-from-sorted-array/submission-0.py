class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=[]

        for num in nums:
            if num not in temp:
                temp.append(num)

        k=len(temp)

        for i in range(k):
            nums[i]=temp[i]
        return k 