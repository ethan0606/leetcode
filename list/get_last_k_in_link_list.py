# 1->2->3->4->5 k=2
# return 4->5

# list 要巧妙利用双指针的思想

from list.link_list import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        curr = head
        i = 0
        while i < k:
            if curr:
                curr = curr.next
            i = i + 1
        k_node = curr
        while k_node and head:
            k_node = k_node.next
            head = head.next
        return head

