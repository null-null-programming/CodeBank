let data = [56, 40, 26, 82, 19, 17, 73, 99];
let [x0, x1, x2, x3, x4, x5, x6, x7] = data;
console.log(x0);
console.log(x1);
console.log(x2);
//....

console.log('');

let data2 = [28, 244, 13, 43, 11, 2345, 2, 4, 1];
let [y1, y2, y3, ...other1] = data2;
console.log(y1);
console.log(y2);
console.log(y3);
console.log(other1);

console.log('')

//swap
let x = 1;
let y = 2;
[x, y] = [y, x];
console.log(x, y);

console.log('')

//
let book1 = {
    title1: "Java",
    publish1: 'aaa',
    price1: 2800
};

let {
    price1,
    title1,
    memo1 = "null"
} = book1;

console.log(price1);
console.log(title1);
console.log(memo1);

console.log('');

//
let book = {
    title: "java",
    publish: "aaa",
    price: 2800,
    other: {
        keywd: "java SE 8",
        logo: "logo.jpg"
    }
};

let {
    title,
    other,
    other: {
        keywd
    }
} = book;

console.log(title);
console.log(other);
console.log(keywd);