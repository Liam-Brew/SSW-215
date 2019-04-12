//This section deals with the object description of my computer.
var computer = {
    manufacturer : "Microsoft",
    releaseYear : 2018,
    line : "Surface Pro",
    os : "Windows 10 Pro"
};
var year = 2019;
function ageCalculator(){
    var computerAge = year - computer.releaseYear;
    return computerAge;
};
console.log(computerAge)

//This section deals with the array of ten numbers.
var array = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var n = 0;
function squareArray(array){
    for (n; n < array.length; n++){
        array[n] = array[n] * array[n];
    }
    console.log(array);
}
squareArray(array);

//This section deals with the inventory object.
var inventory = {
    storeName: "Stevens Campus Bookstore",
    storeAddress: "Howe Center 1st Floor, 1 Castle Point on Hudson, Hoboken NJ 07030",
    stock: [
        {title: "In the Node", author: "Kevin Ryan", price: 232},
        {title: "Sofware Engineering 101", author: "Gregg Vesonder", price: 215},
        {title: "Welcome to Hell: A Materials Processing Story", author: "Woo Lee", price: 344},
        {title: "Quantitative Biology", author: "Nikolai Strigul", price: 250},
        {title: "Logic for Dummies ", author: "Sandeep Bhatt", price: 135}
    ]
};

