class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n=len(piles)
        piles.sort()
        j=len(piles)-2
        sum=0
        while j>=(n/3):
            sum+=piles[j]
            
            j-=2
        return sum
        
