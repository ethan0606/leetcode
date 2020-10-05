from list.link_list import Node
from list.link_list import generate_list
from list.link_list import print_list

# 1->2 ->3
# None <-1 2->3
# prev = 1 curr = 2


def revert_list(head):
    if not head:
        return
    curr = head
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

g = generate_list([1, 2, 3])

print_list(g)
print_list(revert_list(g))

