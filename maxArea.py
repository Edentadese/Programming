class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        i=0
        j=n-1
        while i<j:
            if height[i]<height[j]:
                curr_res=(j-i)*height[i]
                i+=1
            else:
                curr_res=(j-i)*height[j]
                j-=1
            ans=max(ans,curr_res)

        return ans

        
