/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function (arr) {
    let l = 0
    let r = arr.length - 1

    while (l <= r) {
        let m = l + Math.floor((r - l) / 2)

        if (arr[m] == arr[m - 1]) {
            let leftCount = m - 1 - l
            if (leftCount % 2 === 1) {
                r = m - 2
            }
            else {
                l = m + 1
            }
        }
        else if (arr[m] == arr[m + 1]) {
            let rightCount = r - (m + 1)
            if (rightCount % 2 === 1) {
                l = m + 2
            }
            else {
                r = m - 1
            }
        }
        else{
            return arr[m]
        }
    }
};