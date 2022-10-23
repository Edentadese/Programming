class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        dict={0:1}
        count=0
        s=0
        for element in nums:
            s+=element
            if s-k in dict:
                count+=dict[s-k]
            if s in dict:
                dict[s]+=1
            else:
                dict[s]=1
        return count
                        
                
            
