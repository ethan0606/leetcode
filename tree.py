class TreeNode:
    def __init__( self, val ):
        self.val = val
        self.left = None
        self.right = None

def pre_order(root):
    res = []

    def helper(node):
        if not node:
            return None
        res.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return res


def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


def min_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    q = [root]
    depth = 0
    while q:
        size = len(q)
        depth = depth + 1
        for i in range(size):
            root = q.pop(0)
            if not root.left and not root.right:
                return depth
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
    return depth


def revert_tree(root):
    def helper(root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        helper(root.left)
        helper(root.right)
        return root
    return helper(root)

def revert_tree_v2(root):
    if not root:
        return root
    q = [root]
    while q:
        size = len(q)
        for i in range(size):
            curr = q.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return root

def level_order(root):
    res = []
    if not root:
        return res
    q = [root]
    while q:
        size = len(q)
        tmp = []
        for i in range(size):
            curr = q.pop(0)
            tmp.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        res.append(tmp[::])
    return res








if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.right = TreeNode(5)

    #    0
    #  1  2
    # 3 4

    print(pre_order(root))
    print(max_depth(root))
    # print(pre_order(revert_tree(root)))
    print(pre_order(revert_tree_v2(root)))
    print(level_order(root))

