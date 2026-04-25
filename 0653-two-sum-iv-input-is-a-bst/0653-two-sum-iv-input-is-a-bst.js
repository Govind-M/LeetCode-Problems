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
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function (root, k) {
    if (!root) return false

    let leftStack = []
    let rightStack = []

    var pushLeft = (curr) => {
        while (curr) {
            leftStack.push(curr)
            curr = curr.left
        }
    }

    var pushRight = (curr) => {
        while (curr) {
            rightStack.push(curr)
            curr = curr.right
        }
    }

    var getNext = () => {
        let curr = leftStack.pop()
        pushLeft(curr.right)
        return curr.val
    }

    var getPrev = () => {
        let curr = rightStack.pop()
        pushRight(curr.left)
        return curr.val
    }

    pushLeft(root)
    pushRight(root)

    var hasNext = () => {
        return leftStack.length > 0
    }

    var hasPrev = () => {
        return rightStack.length > 0
    }

    left = getNext()
    right = getPrev()

    while (left < right) {
        let sum = left + right

        if (sum === k) return true
        else if (sum < k) {
            if (hasNext()) {
                left = getNext()
            }
            else break;
        }
        else {
            if (hasPrev()) {
                right = getPrev()
            }
            else break;
        }
    }

    return false
};