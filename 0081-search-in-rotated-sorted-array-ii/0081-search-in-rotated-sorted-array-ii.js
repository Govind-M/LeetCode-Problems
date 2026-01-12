/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function (nums, target) {
    let l = 0
    let r = nums.length - 1

    while (l <= r) {
        let m = l + Math.floor((r - l) / 2)


        if (target === nums[m]) {
            return true
        }

        if (nums[l] === nums[m] && nums[r] === nums[m]) {
            l = l + 1
            r = r - 1
            continue;
        }

        if (nums[l] > nums[m]) {
            if (target > nums[m] && target <= nums[r]) {
                l = m + 1
            }
            else {
                r = m - 1
            }
        }
        else {
            if (target < nums[m] && target >= nums[l]) {
                r = m - 1
            }
            else {
                l = m + 1
            }
        }
    }

    return false
};