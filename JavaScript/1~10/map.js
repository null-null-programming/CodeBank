let m = new Map();
m.set('dog', 'wanwan');
m.set('cat', 'nya-');
m.set('mouse', 'chyu-');

for (let key of m.keys()) {
    console.log(key);
}

for (let value of m.values()) {
    console.log(value);
}

for (let [key, value] of m.entries()) {
    console.log(value);
}