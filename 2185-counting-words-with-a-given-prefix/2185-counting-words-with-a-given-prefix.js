/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function (words, pref) {
    let count = 0

    let prefLength = pref.length

    for (let i = 0; i < words.length; i++){
        if(words[i].slice(0,prefLength) === pref){
            count +=1
        }
    }
    return count
};