/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    let i = 0
    let j = 0
    let maxWindowSize = 0
    let currWindowSize = 0
    const map = new Map()

    while (j < s.length) {
        if (map.has(s[j])) {
            i = Math.max(i, map.get(s[j]) + 1)

        }
        map.set(s[j],j)
        currWindowSize = (j - i) + 1
        j += 1

        maxWindowSize = currWindowSize > maxWindowSize ? currWindowSize : maxWindowSize
    }
    return maxWindowSize
};