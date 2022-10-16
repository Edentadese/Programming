class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string=""
        for i in range(len(nums)):
            j=i+1
            while j<len(nums):
                if str(nums[i])+str(nums[j])<str(nums[j])+str(nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
                j+=1
        for j in nums:
            string=string+str(j)
        if string[0]=="0":
            return "0"
        return string
        
