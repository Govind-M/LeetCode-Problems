/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    let queue = [p, q]

    while (queue.length) {
        let t1 = queue.shift()
        let t2 = queue.shift()

        if (!t1 && !t2) continue
        if (!t1 || !t2) return false

        if (t1.val !== t2.val) return false
        else {
            queue.push(t1.left, t2.left)
            queue.push(t1.right, t2.right)
        }
    }

    return true
};