from tree.TreeNode import *


class Codec:
    def serialize(self, root):
        def helper(root):
            if not root:
                return "none,"
            return str(root.val) + "," + helper(root.left) + helper(root.right)
        return helper(root)

    def deserialize(self, data):
        data_array = data.split(",")
        def helper(arr):
            if arr[0] == "none":
                arr.remove(arr[0])
                return None
            root = TreeNode(int(arr[0]))
            arr.remove(arr[0])
            root.left = helper(arr)
            root.right = helper(arr)
            return root
        return helper(data_array)


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)

    c = Codec()
    in_order_print(root)
    print()
    res = c.serialize(root)
    res1 = c.deserialize(res)
    print(res)
    in_order_print(res1)