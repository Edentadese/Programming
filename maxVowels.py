class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        set="aeiou"
        count=i=j=m_x=0
        while j<n:
            if s[j] in set:
                count+=1
            if j-i>k-1:
                if s[i] in set:
                    count-=1
                i+=1
            m_x=max(m_x,count)
            j+=1
        return m_x
        
