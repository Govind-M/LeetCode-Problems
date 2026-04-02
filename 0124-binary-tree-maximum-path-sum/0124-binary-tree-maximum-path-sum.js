/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {
    let maxSumPath = -Infinity
    let traversal = (curr) => {
        if (!curr) return 0
        let leftMax = Math.max(0, traversal(curr.left))
        let rightMax = Math.max(0, traversal(curr.right))

        let currMax = curr.val + leftMax + rightMax

        maxSumPath = Math.max(currMax, maxSumPath)

        return curr.val + Math.max(leftMax, rightMax)

    }
    traversal(root)
    return maxSumPath
};