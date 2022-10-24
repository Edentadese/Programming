class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        prefix=[]

        ans=[]
        s=0
        for i in range(n):
            s=arr[i]^s
            prefix.append(s)
        for j in range(len(queries)):
            if queries[j][0]!=0:
                temp=prefix[queries[j][1]]^prefix[queries[j][0]-1]
                ans.append(temp)
            else:
                ans.append(prefix[queries[j][1]])
        return ans
        
