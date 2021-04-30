'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. 

The list should be made by splicing together the nodes of the first two lists.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = [0]
Output: [0]

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Linked List
class Solution_1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)          # 先建立一個虛擬節點, 紀錄要回傳的
        previous = dummy                # 建立previous節點, 用來遍歷並記錄下一個節點
        while l1 and l2:                # 當兩個list都還有節點時開始做
            if l1.val <= l2.val:        # 若 list 1 第一個點小於 list 2 第一個節點
                previous.next = l1      # 較小的該節點丟進previous
                l1 = l1.next            # 該list節點往下走一個
            else:
                previous.next = l2      # 較小的該節點丟進previous
                l2 = l2.next            # 該list節點往下走一個
                
            previous = previous.next    # previous 要往下走 
        
        previous.next = l1 or l2        # 若l1 或 l2 其中一個為空, 就把剩下的節點全塞到後面
        
        return dummy.next            

if __name__ == '__main__':
    
    s1 = Solution_1()
    print(s1.mergeTwoLists([1,2,4], [1,3,4]))  
    