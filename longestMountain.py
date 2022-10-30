class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res=0
        n=len(arr)
        for i in range(1, n - 1):
            if arr[i + 1] < arr[i] > arr[i - 1]:
                l = r = i
                count=1
                while l and arr[l] > arr[l - 1]: 
                    count+=1
                    l -= 1
                while r  < n-1  and arr[r] > arr[r + 1]: 
                    count+=1
                    r += 1
                res=max(res,count )
        return res
