from tree.TreeNode import *


def build(pre_order, in_order):
    if len(pre_order) != len(in_order):
        return None
    map = dict()
    for i in range(len(in_order)):
        map[in_order[i]] = i
    return build_tree(pre_order, 0, len(pre_order)-1, map, 0, len(in_order)-1)


# 3 9 20 15 7
# pl, pl+1,  pr

# x -pl-1 = pi -1 -if
# x = pi + pl -if

# 9 3 15 20 7
# if  pi


def build_tree(pre_order, pre_left, pre_right, map, in_left, in_right):
    if pre_left > pre_right or in_left > in_right:
        return None

    root_val = pre_order[pre_left]
    root = TreeNode(root_val)
    p_index = map[root_val]

    root.left = build_tree(pre_order, pre_left+1, p_index-in_left+pre_left,
                           map, in_left, p_index-1)
    root.right = build_tree(pre_order, p_index-in_left+pre_left+1, pre_right,
                            map, p_index+1, in_right)
    return root

if __name__ == '__main__':
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]
    root = build(pre_order, in_order)
    pre_order_print(root)
