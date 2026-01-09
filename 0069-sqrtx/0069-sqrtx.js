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

        middle = Math.floor(left + (right - left) / 2)


        

        if (x == middle * middle) {
            return middle
        }
        else if (x < middle * middle) {
            right = middle - 1
        }
        else  {
            left = middle + 1
        }
    }
    return right


};