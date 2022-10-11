class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int)-> int:
        sum = 0
        count=0
        n=len(arr)

        for i in range(k):
            sum += arr[i]
        if sum/k>=threshold:
            count+=1
        for i in range(n-k):
            sum+= arr[i+k] - arr[i]
            if sum /k >= threshold:
                count += 1

        return count
        
        
