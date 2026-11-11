var reduce = function(nums, fn, init) {
    let val = init;
    for (const num of nums) {
        val = fn(val, num);
    }
    return val;
};