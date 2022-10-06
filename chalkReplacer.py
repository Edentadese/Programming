class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum=0
        for i in range(len(chalk)):
            sum+=chalk[i]
        n=k%sum
        for i in range(len(chalk)):
            if n-chalk[i]>=0:
                n-=chalk[i]
            else:
                return i
            i+=1
        return i
