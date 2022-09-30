class Solution:
    def sortSentence(self, s: str) -> str:
        sh = s.split(" ")
        final = ""
        for i in range (len(sh)):
            min_index=i
            for j in range(i,len(sh)):
                if sh[j][-1]<=sh[min_index][-1]:
                    min_index=j
            sh[min_index], sh[i] = sh[i], sh[min_index]
            final+=sh[i][:-1]+" "
        return final[:-1]
        
