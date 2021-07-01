# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepestLeavesSum(root):
    sums = []

    def dfs(root, lvl):
        if lvl == len(sums):
            sums.append(root.val)
        else:
            sums[lvl] += root.val
        if root.left:
            dfs(root.left, lvl + 1)
        if root.right:
            dfs(root.right, lvl + 1)

    dfs(root, 0)
    return sums[-1]
