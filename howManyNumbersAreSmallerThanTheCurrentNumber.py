class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        empty=[]
        for element in nums:
            count=0
            for i in range(len(nums)):
                if element>nums[i]:
                    count+=1
            empty.append(count)
        return empty
        
