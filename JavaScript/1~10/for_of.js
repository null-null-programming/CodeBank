var data = {
    a: 120,
    b: 11,
    c: 128
};
for (key in data) {
    console.log(key + '=' + data[key]);
}

var data = ['a', 'b', 'c'];
Array.prototype.hoge = function () {}
for (value of data) {
    console.log(value);
}