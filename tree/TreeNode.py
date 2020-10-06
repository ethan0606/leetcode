class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_print(root):
    if not root:
        return
    print(root.val, end=',')
    pre_order_print(root.left)
    pre_order_print(root.right)
    return

def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print(root.val, end=',')
    in_order_print(root.right)
    return


def post_order_print(root):
    if not root:
        return
    post_order_print(root.left)
    post_order_print(root.right)
    print(root.val, end=',')
    return

def traverse(root):
    # preorder
    traverse(root.left)
    # inorder
    traverse(root.right)
    # postorder


def partition(nums, lo, hi):
    return 0

def sort(nums, lo ,hi):
    # 通过交换元素构建分界点 p
    p = partition(nums, lo, hi)
    sort(nums, lo, p-1)
    sort(nums, p+1, hi)


if __name__ == '__main__':
    r = TreeNode(0)
    r.left = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)
    r.right.right = TreeNode(4)
    pre_order_print(r)
    print()
    in_order_print(r)
    print()
    post_order_print(r)