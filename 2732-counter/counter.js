var createCounter = function(n) {
    let count = n;
    return function() {
        const current = count;
        count += 1;
        return current;
    };
};