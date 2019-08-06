let Member = function (firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.getName = function () {
        return this.lastName + ' ' + this.firstName;
    }
};

let mem = new Member("Tanaka", "Ichirou");
console.log(mem.getName());