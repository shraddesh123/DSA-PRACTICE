class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        def rotate_array(i,j):

            while i < j :
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            return nums
        n=len(nums)



        rotate_array(0,n-1)
        rotate_array(0,k-1)
        rotate_array(k,n-1)
        