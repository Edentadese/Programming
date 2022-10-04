class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        pre=0
        total = sum(nums)
    
        for i in range(len(nums)):
            
            if pre==(total-nums[i]-pre):
                return i
            pre=pre+nums[i]
            
        return -1
        
