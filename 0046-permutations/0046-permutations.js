/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(arr) {
    let result = [];
    let n = arr.length;
    let backtrack = (path) => {
        if(path.length === n){
            result.push([...path]);
        }
        for(let i=0; i < n; i++){
            if(!path.includes(arr[i])){
                path.push(arr[i]);
                backtrack(path);
                path.pop();
            }
        }
    }
    backtrack([]);
    return result;
};