class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        product=1
        for i in range(len(nums)):
            left.append(product)
            product=product*nums[i]
        product=1
        for i in range(len(nums)-1,-1,-1):
            right.append(product)
            product=product*nums[i]
        right.reverse()
        res_list = []
        for i in range(0, len(right)):
            res_list.append(right[i] * left[i])
        return res_list
        
        
    
        
            
      
        
        
        
