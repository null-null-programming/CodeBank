console.log(10 + 1);
console.log('10' + 1);
var today = new Date();
console.log(1234 + today);

console.log(0.2 * 3);
console.log(0.2 * 3 == 0.6);

var x = 1;
var y = x;
x = 2;
console.log(y);

var data1 = [0, 1, 2];
var data2 = data1;
data1[0] = 5;
console.log(data2); //!!!!!!!!

const data = [1, 2, 3];
data[1] = 10;
console.log(data); //!!!!!!!