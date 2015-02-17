# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, left, right):
        head = ListNode(0)
        prev = head

        while True:
            if not left:
                prev.next = right
                return head.next
            if not right:
                prev.next = left
                return head.next
            if left.val > right.val:
                end = right
                while end.next:
                    if end.next.val > left.val:
                        break
                    end = end.next
                prev.next = right
                prev = end
                right = end.next
            else:
                end = left
                while end.next:
                    if end.next.val > right.val:
                        break
                    end = end.next
                prev.next = left
                prev = end
                left = end.next
        
    def mergesort(self, head):
        if not head or not head.next:
            return head
        
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None
        head = self.mergesort(head)
        right = self.mergesort(right)
        return self.merge(head, right)
        
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        head = self.mergesort(head)
        return head
