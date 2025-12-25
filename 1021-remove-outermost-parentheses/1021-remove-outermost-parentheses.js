/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function (s) {
    //Using counter approach
    let depth = 0
    let ans = ''
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            depth += 1
            if (depth > 1) {
                ans = ans + s[i]
            }
        }
        else {
            if (depth > 1) {
                ans = ans + s[i]
            }
            depth -= 1
        }
    }
    return ans
};