'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Example:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: ListNode) -> ListNode:             
        if not head or not head.next:
            return head                # 若list為空 或是只有一個 就直接回傳
        
        previous, fast, slow = None, head, head # 初始化三個指標, prev:指向前一個; fast:一次走兩步; slow:一次走一步
        
        while fast and fast.next: # 當走快的還沒到盡頭就開始或繼續 , 直到最後代表slow就會是在中間的位置
            previous = slow
            slow = slow.next
            fast = fast.next.next
            
        previous.next = None # 這樣就可以跟slow做切斷
        
        n1 = self.sortList(head) # 繼續切分
        n2 = self.sortList(slow) # 繼續切分    
        return self.merge(n1, n2)
            
        
    def merge(self, n1: ListNode, n2: ListNode) -> ListNode:
        n = ListNode(0) # n來記錄位置
        ite = n         # ite來看現在走到哪
        while n1 and n2:
            
            if n1.val < n2.val:
                ite.next = n1
                n1 = n1.next
            else:
                ite.next =n2
                n2 = n2.next     
            ite = ite.next
            
        if n1:
            ite.next = n1
        if n2:
            ite.next = n2        
        
        return n.next # 不是ite    
            
if __name__ == '__main__':
    
    list = [2,7,4,1,8,1]
    s = Solution()
    print(s.sortArray(list))     
                    