class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        res=float('inf')
        sum=0
        for j in range(n):
            sum+=nums[j]
            while sum-nums[i]>=target and i<j:
                sum=sum-nums[i]
                i+=1
            if sum>=target:
                res=min(res,j-i+1)
        if res==float('inf'):
            return 0
        else:
            return res
   
        
