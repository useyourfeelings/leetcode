# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        
        fake_head = ListNode(1)
        fake_head.next = head
        prev_node = fake_head
        now_node = head
        
        while True:
            if not now_node or not now_node.next:
                break
                
            if now_node.next.val != now_node.val:
                prev_node = now_node
                now_node = now_node.next
                continue
            
            #got dup
            temp_node = now_node
            while True:
                if not temp_node.next:
                    prev_node.next = now_node = None
                    break
                
                if temp_node.next.val != temp_node.val:
                    prev_node.next = now_node = temp_node.next
                    break
                
                temp_node = temp_node.next
                
        return fake_head.next
