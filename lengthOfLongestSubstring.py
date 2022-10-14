class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_len = 0
        for i in s:

            if i not in sub:
                sub+=i
            else:
                sub = sub[sub.index(i) + 1:] + i
          
            max_len= max(max_len, len(sub))
        return max_len
        
