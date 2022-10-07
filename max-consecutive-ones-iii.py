class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size=0
        i=0
        j=0
        noOfZeroes=0
        while j<len(nums):
            if nums[j]==0 :
                noOfZeroes+=1
            while noOfZeroes>k:
                if nums[i]==0:
                    noOfZeroes-=1
                i+=1
            size=max(size,j-i+1)
            j+=1
        return size
        
