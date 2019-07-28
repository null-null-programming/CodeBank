function factorial(n) {
    if (n !== 0) return n * factorial(n - 1);
    return 1;
}

console.log(factorial(5));

function arrayWalk(data, f) {
    for (let key in data) {
        f(data[key], key);
    }
}

function showElement(value, key) {
    console.log(key + ':' + value);
}

var ary = [1, 2, 4, 8, 16];
arrayWalk(ary, showElement);

let result = 0;

function sumElement(value, key) {
    result += value;
}

arrayWalk(ary, sumElement);
console.log('合計値：' + result);