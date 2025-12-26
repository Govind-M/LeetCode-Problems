/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
    let stack = []
    let map = {
        '+': (a, b) => a + b,
        '-': (a, b) => a - b,
        '/': (a, b) => Math.trunc(a / b),
        '*': (a, b) => a * b
    }
    for (let i = 0; i < tokens.length; i++) {
        if (!map[tokens[i]]) {
            stack.push(Number(tokens[i]))
        }
        else {
            let b = stack.pop()
            let a = stack.pop()
            let res = map[tokens[i]](a, b)
            stack.push(res)
        }
    }
    return stack.pop()
};