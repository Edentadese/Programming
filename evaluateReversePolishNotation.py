class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c not in ['/','*','+','-']:
                stack.append(c)
            if c in "+-*/":
                val1=int(stack.pop())
                val2=int(stack.pop())
                if c=="+":
                    res=val2+val1
                if c=="-":
                    res=val2-val1
                if c=="*":
                    res=val2*val1
                if c=="/":
                    res=int(val2/val1)

                stack.append(res)
        return stack[-1]
