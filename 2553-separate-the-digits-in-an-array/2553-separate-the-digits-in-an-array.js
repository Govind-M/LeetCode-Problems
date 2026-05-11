/**
 * @param {number[]} nums
 * @return {number[]}
 */
var separateDigits = function(nums) {
    let result = [];

    for (let num of nums) {

        let digits = num.toString();

        for (let digit of digits) {
            result.push(Number(digit));
        }
    }

    return result;
};