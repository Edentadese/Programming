class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        stack=[]
        intervals.sort(key=lambda x:x[0])
        while i<n:
            if len(stack)==0 or stack[-1][1]<intervals[i][0]:
                stack.append(intervals[i])

            else:
                stack[-1][1]=max(stack[-1][1],intervals[i][1])
            i+=1

        return stack
