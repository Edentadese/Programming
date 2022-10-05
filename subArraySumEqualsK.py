class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict={0:1}
       
        count=0
        s=0
        for num in nums:
            s+=num
            if s-k in dict:
                count+=dict[s-k]
            if s in dict:
                dict[s]+=1
            else:
                dict[s]=1
        return count
        
