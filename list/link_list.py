# Linked list 是一个节点接下一个节点，每个节点保存下一个指向的地址


class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head):
    while head:
        if not head.next:
            print(head.val)
        else:
            print(head.val, end='->')
        head = head.next


def generate_list(arr):
    dummy = Node(-1)
    curr = dummy
    for i in arr:
        tmp = Node(i)
        curr.next = tmp
        curr = curr.next
    return dummy.next


l1 = Node(0)
l1.next = Node(1)
l1.next.next = Node(2)
# print_list(l1)
# print_list(generate_list([1, 2 , 3]))


def delete_node(node):
    if not node.next:
        node = None
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
    return

print_list(l1)
delete_node(l1.next)
print_list(l1)

