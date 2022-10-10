class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if (len(cardPoints) < k):
            print("Invalid")
            return -1

        res=0
        for j in range(n-k,n):
            res+=cardPoints[j]

        curr_sum = res
        j=n-k
        for i in range(k):
            res+=(cardPoints[i]-cardPoints[j])
            curr_sum=max(curr_sum,res)
            i+=1
            j+=1
        return curr_sum
