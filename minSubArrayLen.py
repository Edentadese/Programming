class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        ans = 0
        j=0
        sum=0
        i=0
        while i<n:
            sum+=nums[i]
            while sum-nums[j]>=target and j<=i:
                sum-=nums[j]
                j+=1
            if sum>=target:
                if (ans == 0 or ans > (i - j + 1)):
                    ans = (i - j + 1)
            i+=1
        return ans
        
        
