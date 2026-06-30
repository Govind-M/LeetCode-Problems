/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(arr) { 
    let result = []; 
    let backtrack = (path, start) => { 
        result.push([...path]); 
        for(let i = start; i < arr.length; i++){ 
            path.push(arr[i]); 
            backtrack(path, i+1); 
            path.pop(); 
        } 
    } 
    backtrack([], 0); 
    return result; 
};