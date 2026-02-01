/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumCost = function(nums) {
    let n = nums.length
    let cost = nums[0]

    let newArr = nums.slice(1,n).sort(function(a,b){return a-b})

    return cost += newArr[0] + newArr[1]
};