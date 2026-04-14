/**
 * // Definition for a _Node.
 * function _Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {_Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    if(!root) return []
    let ans = []
    let stack = []
    stack.push(root)
    while(stack.length){
        let curr = stack.pop()
        ans.push(curr.val)
        for(let i = curr.children.length-1;i>=0;i--){
            curr.children[i] && stack.push(curr.children[i])
        }
    }
    return ans
};