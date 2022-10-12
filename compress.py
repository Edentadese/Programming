class Solution:
    def compress(self, chars: List[str]) -> int:
        empty=[]
        count=1
        i=0
        for j in range(1,len(chars)):
            if chars[j]==chars[i] :
                count+=1
                i+=1
            else:
                empty.append(chars[i])
                if count>1:
                    for k in str(count):
                        empty.append(str(k))
                i += 1
                count = 1
        empty.append(chars[i])
        if count>1:
            for k in str(count):
                empty.append(str(k))

        return len(empty)
        
        
