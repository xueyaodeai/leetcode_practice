# 二叉树的最小深度
# 深度优先 DFS
# 递归结束条件：
#   1. 当前节点 root 为空，此处树的高度为 0，也即是最小值
#   2. 当前节点 root 的左子树和右子树都为空，此处树的高度为 1，1 也是最小值
#   3. 当前节点 root 的左子树和右子树其一为空，此处树的高度为 min_depth(left) + min_depth(right) + 1
#   4. 当前节点 root 的左右子树都不为空，此处树的高度为 min(min_depth(left), min_depth(right)) + 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: TreeNode) -> int:
    if root is None:
        return 0

    d_left = min_depth(root.left)
    d_right = min_depth(root.right)
    if root.left is None or root.right is None:
        return d_left + d_right + 1
    return min(d_left, d_right) + 1


# 广度优先 BFS
# 1. 根节点放进数组
# 2. 根节点为 None 则返回 0
# 3. 根节点取出，深度 + 1，判断是否为叶子结点(左右子节点都为 None)，是就返回当前深度
# 4. 非叶子结点就遍历左右子节点，非 None 则放进数组
# 5. 重复遍历数组直至满足条件
def min_depth_bfs(root: TreeNode) -> int:
    queue, depth = [root], 0
    while root and len(queue) > 0:
        n, depth = len(queue), depth + 1
        for _ in range(n):
            node = queue.pop(0)
            if not node.left and not node.right:
                return depth
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
    return 0
