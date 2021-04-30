'''
//////////////////////////////////////////////////////////////////////////////////////////////////////////

83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 

Return the linked list sorted as well.

//////////////////////////////////////////////////////////////////////////////////////////////////////////

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Linked List
class Solution_1:
    def deleteDuplicates(self, head):
        ite = head
        while ite:
            temp = ite.next  # 先將下一個丟給temp
            while temp and temp.val == ite.val:  # 若值相同, 就跳過他
                temp = temp.next
            ite.next = temp
            ite = ite.next

        return head     
                    

if __name__ == '__main__':
    
    s1 = Solution_1()
    print(s1.deleteDuplicates([1,1,2,3,3]))  
    
    # s2 = Solution_2()
    # print(s2.deleteDuplicates([2, 5, 5, 11], 10))             