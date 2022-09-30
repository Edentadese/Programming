class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ci, cii, ciii = 0, 0, 0
        for i in nums:
            if i == 0:
                ci += 1
            if i == 1:
                cii += 1
            if i == 2:
                ciii += 1

        for i in range(0, ci):
            nums[i] = 0
        for i in range(ci, ci + cii):
            nums[i] = 1
        for i in range(cii + ci, len(nums)):
            nums[i] = 2
        """
        Do not return anything, modify nums in-place instead.
        """
