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
 * @return {number[]}
 */
// var preorderTraversal = function(root) {

//     let ans = []
//     function traversal(curr){
//         if(!curr) return
//         ans.push(curr.val)
//         traversal(curr.left)
//         traversal(curr.right)
//     }

//     traversal(root)
//     return ans
// };

var preorderTraversal = function(root) {

let stack = []
let ans = []

stack.push(root)

while(stack.length){

if(!root) return []

let curr = stack.pop()
ans.push(curr.val) 
curr.right && stack.push(curr.right)
curr.left && stack.push(curr.left)
}

return ans

};

