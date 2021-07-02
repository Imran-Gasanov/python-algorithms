class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.summ = 0

    def sumEvenGrandparent(self, root) -> int:
        """
        >>> root = TreeNode()
        >>> root.val = TreeNode(6)
        >>> root.val.left = TreeNode(7)
        >>> root.val.right = TreeNode(8)
        >>> root.val.left.left = TreeNode(2)
        >>> root.val.left.right = TreeNode(7)
        >>> root.val.right.left = TreeNode(1)
        >>> root.val.right.right = TreeNode(3)
        >>> root.val.left.left.left = TreeNode(9)
        >>> root.val.left.left.right = TreeNode(None)
        >>> root.val.left.right.left = TreeNode(1)
        >>> root.val.left.right.right = TreeNode(4)
        >>> root.val.right.left.left = TreeNode(None)
        >>> root.val.right.left.right = TreeNode(None)
        >>> root.val.right.right.left = TreeNode(None)
        >>> root.val.right.right.right = TreeNode(5)
        >>> a = Solution()
        >>> Solution.sumEvenGrandparent(a, root)
        18
        """
        if root == None:
            return 0
        self.dfs(root, None, None)
        return self.summ

    def dfs(self, root, parent, grandparent):
        if root == None:
            return
        if grandparent != None and grandparent.val % 2 == 0:
            self.summ += root.val
            print(self.summ)
        self.dfs(root.left, root, parent)
        self.dfs(root.right, root, parent)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
