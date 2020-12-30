class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):
        current = head
        previous = None
        
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            

        return previous
        

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)

S = Solution()
answer = S.reverseList(node)
while answer:
    print(answer.val)
    
