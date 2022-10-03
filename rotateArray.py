class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        i,j,l,m,n,o=0,(len(nums) - 1),0, k - 1,k,(len(nums) - 1)
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i+=1
        while l < m:
            nums[l], nums[m] = nums[m], nums[l]
            m -= 1
            l += 1
        while n < o:
            nums[n], nums[o] = nums[o], nums[n]
            o -= 1
            n += 1
