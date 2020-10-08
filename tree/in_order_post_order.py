from tree.TreeNode import *


def build(in_order, post_order):
    in_len = len(in_order)
    post_len = len(post_order)
    if in_len != post_len:
        return None
    m = {val:idx for idx, val in enumerate(in_order)}
    print(m)

    def build_tree(in_left, in_right):
        if in_left > in_right:
            return None

        root_val = post_order.pop()
        root = TreeNode(root_val)
        pi = m[root_val]
        # 这里要注意构造的顺序，要先构建右树
        root.right = build_tree(pi + 1, in_right)
        root.left = build_tree(in_left, pi - 1)
        return root

    return build_tree(0, in_len-1)


if __name__ == '__main__':
    in_order = [9, 3, 15, 20, 7]
    post_order = [9, 15, 7, 20, 3]
    root = build(in_order, post_order)
    in_order_print(root)
