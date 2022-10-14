class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n=len(tokens)
        score=0
        i=0
        j=n-1
        ans=0
        while i<=j:
            if power>=tokens[i]:
                score+=1
                power=power-tokens[i]
                i+=1
                ans = max(ans, score)
                
            else:
                if score>0:
                    score-=1
                    power+=tokens[j]
                    j-=1
                else:
                    break
        return ans
        
