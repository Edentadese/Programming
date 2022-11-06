class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        deleted=0
        count=0
        m_x=0
        i=0
        j=0
        while j<n:
            if nums[j]==0:
                deleted+=1
            elif nums[j]==1:
                count+=1
            if deleted==1:
                m_x=max(m_x,j-i)
            while(deleted > 1):
                if(nums[i] == 0) :
                    deleted-=1
                i+=1
             
            
            j+=1
        if count==n:
            return n-1
        else:
            return m_x
        
        
