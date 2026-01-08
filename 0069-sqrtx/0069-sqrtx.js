/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
    if (x < 2) {
        return x
    }

    let left = 2
    let right = Math.floor(x / 2)

    let middle = 0

    while (left <= right) {

        middle = left + Math.floor((right - left) / 2)


        

        if (x == middle * middle) {
            return middle
        }
        else if (x < middle * middle) {
            right = middle - 1
        }
        else if (x > middle * middle) {
            left = middle + 1
        }
    }
    return right


};