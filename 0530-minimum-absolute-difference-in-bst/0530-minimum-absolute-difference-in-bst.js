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
var getMinimumDifference = function (root) {
    let curr = root
    let stack = []
    let currMin = Infinity
    let prev = null

    while (curr || stack.length) {
        while (curr) {
            stack.push(curr)
            curr = curr.left
        }

        curr = stack.pop()
        if(prev){
            currMin = Math.min(currMin, (Math.abs(curr.val - prev.val)))
        }
        prev = curr
        curr = curr.right
    }
    return currMin
};