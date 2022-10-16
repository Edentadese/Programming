class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        nums.sort()
        while i<n-1:            
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i+=2
        return nums
        
