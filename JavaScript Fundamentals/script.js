//These variables demonstrates prompt().
var firstName = prompt("What is your first name?");
var lastName = prompt("What is your last name?");
var age = prompt("How many years old are you?")

//This variable concatenates two strings.
var name = firstName + " " + lastName;

//This variable applies a method to a string.
var nameLength = name.length;

//This variable will be used later on in the while loop.
var i = 13;

//These variables will be used later on in the for loop.
var j;
var text = "";

//This variable contains a function which treats a string like an array.
console.log(firstName[3]);

//These statements demonstrate console.log().
console.log(nameLength);

//These functions demonstrate alert().
alert("Hello " + name);
alert("Your full name has " + nameLength + " characters in it.");

//These statements demonstrate comparison operators.
if (age < 18) console.log("I am a minor");
if (firstName == "Liam") console.log("Hi, Liam");
if (nameLength > 10) alert("Error");

//These statements demonstrate logical operators.
if (firstName == "Liam" && age == 19) console.log("We are the same");
if (nameLength == 9 || nameLength > 9) console.log("This is an alternative method of asking if >=.")
if (lastName != "Brew") alert("Stranger danger!");

//These statements demonstrate if-else if. 
if (firstName == "Liam"){
    console.log("Hey Liam");
}else if (firstName == "Allen"){
    console.log("Hi Allen");
}else{
    console.log("Who are you?");
}

if (age == 19){
    console.log("We are the same age.");
}else if (age >= 20){
    console.log("You are older than me.");
    if (age >= 30){
        console.log("You're old");
    }
}else if (age == 18){
    console.log("You are one year younger than me.");
}else{
    console.log("The difference of our ages is more than one year.");
}

//This statement demonstrates a while loop.
while (i > 10){
    console.log("My number is " + i);
    i--;
}

//This statement demonstrates a for loop.
for (j = 0; j < name.length; j++){
    text += "letter " + name[j] + ", ";
}
console.log(text);

//These functions do not contain arguments.
function functionWithoutArguments1(a, b){
    if (b === undefined) {
      b = 0;
      console.log(b);
    } 
}
functionWithoutArguments1();
function functionWithoutArguments2(c, d){
    if (c == undefined && d == undefined){
        var value = "N/A";
        console.log(value);
    }
}
functionWithoutArguments2();

//These functions do contain arguments.
function functionWithArguments1(w, x){
    sum = w + x;
    console.log(sum);
}
functionWithArguments1(2, 3);
function functionWithArguments2(y, z){
    product = y * z;
    console.log(product);
}
functionWithArguments2(4, 5);

//This statement demonstrates the scoping issue.
console.log(k);
for (k = 0; k < 5; k++){
    console.log(k);
}

//This section deals with array work.
var array1 = ["L", "I", "A", "M"];
var array2 = ["B", "R", "E", "W"];
console.log(array1.toString());
console.log(array2.pop())

