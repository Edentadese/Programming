class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,j = [],0

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while j < len(popped) and stack:
                if stack[-1] == popped[j]:
                    stack.pop()
                    j = j + 1
                else:
                    break

        return j == len(popped)
