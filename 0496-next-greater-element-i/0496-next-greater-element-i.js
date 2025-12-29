/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
    let map = {}
    let stack = []
    let ans = []

    stack.push(nums2[nums2.length - 1])
    map[nums2[nums2.length - 1]] = -1

    for (let i = nums2.length - 2; i >= 0; i--) {
        while (stack.length) {
            if (nums2[i] > stack[stack.length - 1]) {
                stack.pop()
            }
            else {
                map[nums2[i]] = stack[stack.length - 1]
                break
            }
        }
        if (!stack.length) {
            map[nums2[i]] = -1
        }

        stack.push(nums2[i])
    }

    for (let j = 0; j < nums1.length; j++) {
        ans.push(map[nums1[j]])
    }

    return ans
};