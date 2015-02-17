# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        player1 = player2 = head
        while True:
            if not player1.next:
                return False
            player1 = player1.next
            if not player2.next:
                return False
            player2 = player2.next
            if not player2.next:
                return False
            player2 = player2.next
            
            if player1 == player2:
                return True
