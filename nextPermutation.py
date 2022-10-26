class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        
        
        inv=len(nums)-2
        while inv>=0 and nums[inv]>=nums[inv+1]:
            inv-=1
        if inv+1 ==0:
            return nums.reverse()

        j=len(nums)-1
        while j>=inv:
            if nums[j]>nums[inv]:
                nums[j],nums[inv]=nums[inv],nums[j]
                break
            
            j-=1
        nums[inv+1:]=reversed(nums[inv+1:])

        
        
   
