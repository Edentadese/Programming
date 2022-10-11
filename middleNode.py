# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode=head
        length=0
        while currentNode is not None:
            length+=1
            currentNode=currentNode.next
        middle=length//2
        currentPosition=0
        currentNode=head
        while True:
            if currentPosition==middle:
                return currentNode  
            currentPosition+=1
            currentNode=currentNode.next
        return None
        
        
