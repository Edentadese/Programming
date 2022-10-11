class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set="aeiou"
        n=len(s)
        max_val=0
        for i in range(k):
            if s[i] in set:
                max_val+=1
        i=0
        curr_max=max_val
        for j in range(k-1,n-1):
            if s[i] in set:
                max_val-=1
            i+=1
            j+=1
            if s[j] in set:
                max_val+=1
            curr_max=max(curr_max,max_val)
        return curr_max
