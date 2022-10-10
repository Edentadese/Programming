class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if 0 not in nums:
            return n - 1
        left=0
        right=0
        max_count=0
        for i in range(n-1):
            if nums[i]!=0:
                left+=1
            else:
                for j in range(i+1,n):
                    if nums[j]!=0:
                        right+=1
                    else:
                        break
                max_count=max(left+right,max_count)
                left=0
                right=0
        return max_count
        
        
