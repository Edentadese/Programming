class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int)-> int:
        n=len(arr)
        i=j=sum=count=0
        while j<n:
            
            sum+=arr[j]
            if j-i==k-1:
                average=sum/k
                
                if average>=threshold:
                    count+=1
                sum-=arr[i]
                i+=1
            
            j+=1
        return count

        
        
