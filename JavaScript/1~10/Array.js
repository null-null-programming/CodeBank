var data = [2, 3, 4, 5];
data.forEach(function (value, index, array) {
    console.log(value * value);
});

var result = data.map(function (value) {
    return value * value;
});
console.log(result);

var result2 = data.some(function (value) {
    return value % 3 == 0;
});
console.log(result2);

var get = data.filter(function (value, index, array) {
    return value % 2 == 1;
});
console.log(get);

var ary = [5, 25, 10];
console.log(ary.sort());
console.log(ary.sort(function (x, y) {
    return x - y;
}));