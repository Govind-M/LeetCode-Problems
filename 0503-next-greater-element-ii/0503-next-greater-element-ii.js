/**
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
    let arr = [...nums, ...nums]
    let stack = []

    let ans = Array(arr.length).fill(-1)

    ans[arr.length-1] = -1
    stack.push(arr[arr.length - 1])

    for (let i = arr.length - 2; i >= 0; i--){
        while(stack.length){
            if(arr[i]<stack[stack.length-1]){
                ans[i] = stack[stack.length-1]
                break
            }
            else
            {
                stack.pop()
            }
        }
        if(stack.length === 0){
            ans[i] = -1
        }

        stack.push(arr[i])
    }

    return ans.slice(0,arr.length/2)

};