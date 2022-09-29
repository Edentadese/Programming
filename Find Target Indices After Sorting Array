class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            min=i
            for j in range (i+1,len(nums)):
                if nums[j]<nums[min]:
                    min=j
            if i!=min:
                nums[min],nums[i]=nums[i],nums[min]
        empty = []
        for i in range(len(nums)):
            if nums[i] == target:
                empty.append(i)
        return empty
        
