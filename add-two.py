# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(self, l1, l2):
    
    dummy = ListNode()
    current = dummy
    
    carryover = 0
    
    while l1 or l2 or carryover:
        
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        
        value = l1Val + l2Val + carryover
        carryover = value // 10
        value = value % 10
        
        current.next = ListNode(value)
        
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
        
    return dummy.next