# Linked list 是一个节点接下一个节点，每个节点保存下一个指向的地址


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


# l1 = Node(0)
# l1.next = Node(1)
# l1.next.next = Node(2)
# print_list(l1)


# print_list(generate_list([1, 2 , 3]))