# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create Dummy Node
        dummy = ListNode()
        # Have Tail and Dummy Node Initializing
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                # Incrementing List1
                list1 = list1.next
            else:
                tail.next = list2
                # Incrementing List2
                list2 = list2.next
            # Incrementing Tail.
            tail = tail.next

        # If either list is short than the other
        # ensuring the edge case is covered.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next