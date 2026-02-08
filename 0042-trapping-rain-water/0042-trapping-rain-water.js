/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (arr) {
    let maxL = []
    maxL[0] = arr[0]
    let maxR = []
    maxR[arr.length - 1] = arr[arr.length - 1]

    for (let i = 1; i < arr.length; i++) {
        maxL[i] = Math.max(maxL[i - 1], arr[i])
        maxR[arr.length - i - 1] = Math.max(arr[arr.length - i - 1], maxR[arr.length - i])
    }

    let ans = 0

    for (let i = 0; i < arr.length; i++) {
        let waterTrapped = Math.min(maxL[i], maxR[i]) - arr[i]
        ans = ans + (waterTrapped < 0 ? 0 : waterTrapped)
    }

    return ans
};