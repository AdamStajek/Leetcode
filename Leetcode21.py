# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        cur1 = list1
        cur2 = list2
        if cur1.val > cur2.val:
            head3 = cur2
            cur2 = cur2.next
        else:
            head3 = cur1
            cur1 = cur1.next
        cur3 = head3
        while True:
            if cur1 == None:
                cur3.next = cur2
                return head3
            elif cur2 == None:
                cur3.next = cur1
                return

            if cur1.val > cur2.val:
                cur3.next = cur2
                cur2 = cur2.next
            else:
                cur3.next = cur1
                cur1 = cur1.next
            cur3 = cur3.next



