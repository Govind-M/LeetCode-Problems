/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (t) {

    let n = t.length
    let ans = Array(n).fill(0)
    let stack = []

    ans[t.length-1] = 0
    stack.push(t.length - 1)

    for (let i = t.length - 2; i >= 0; i--) {
        while (stack.length) {
            if (t[i] >= t[stack[stack.length - 1]]) {
                stack.pop()
            }
            else
            {
                ans[i] = stack[stack.length-1] - i
                break
            }
        }

        if(stack.length === 0){
            ans[i] = 0
        }

        stack.push(i)
    }
    return ans
};