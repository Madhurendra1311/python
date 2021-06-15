// ##1) Arithmetic operators

let x = 5;
let y = 3;

// addition
console.log('x + y = ', x + y)  // 8

// subtraction
console.log('x - y = ', x - y)  // 2

// multiplication
console.log('x * y = ', x * y)  // 15

// division
console.log('x / y = ', x / y)  // 1.6666666666666667

// remainder
console.log('x % y = ', x % y)   // 2

// increment
console.log('++x = ', ++x) // x is now 6
console.log('x++ = ', x++) // prints 6 and then increased to 7
console.log('x = ', x)     // 7

// decrement
console.log('--x = ', --x) // x is now 6
console.log('x-- = ', x--) // prints 6 and then decreased to 5
console.log('x = ', x);     // 5

//exponentiation
console.log('x ** y =', x ** y)

// ##2) Comparison operators

// equal operator
console.log(2 == 2); // true
console.log(2 == '2'); // true

// not equal operator
console.log(3 != 2); // true
console.log('hello' != 'Hello'); // true

// strict equal operator
console.log(2 === 2); // true
console.log(2 === '2'); // false

// strict not equal operator
console.log(2 !== '2'); // true
console.log(2 !== 2); // false

// ##3)Logical Operators

// logical AND
console.log(true && true); // true
console.log(true && false); // false

// logical OR
console.log(true || false); // true

// logical NOT
console.log(!true); // false

var a = 12, b = 25;

console.log((a != b) && (a < b)); // returns true

console.log((a > b) || (a == b)); // returns false

console.log((a < b) || (a == b)); // returns true

console.log(!(a < b)); // returns false

console.log(!(a > b)); // returns true

// ##4) Bitwise Operators

// bitwise AND operator example

// let a = 12; 
// let  b = 25; 

result = a & b;
console.log(result); // 8

// bitwise OR operator example

result = a | b;
console.log(result); // 29

result = a ^ b;
console.log(result); // 21

result = ~b;
console.log(result); // -26

// ##5) String operators

console.log('hello' + 'world');

let p = 'JavaScript';

p += ' tutorial';  // p = p + ' tutorial';
console.log(a);

// variables defined to hold different types of data
var techName = 'JavaScript'; // String literal 
var version = 6; // Number literal
var isDone = true; // Boolean literal

console.log('Learning ' + techName + version);

// variables defined to hold different types of data
var _firstName = 'JavaScript';
var $version = 6;
var $num_total1 = 10;

console.log('variables details: ' + _firstName + ' ' + $version + ' ' + $num_total1);

// traditional var syntax
var techName1 = 'JavaScript';

for (var i = 1; i <= 5; i++) {
    console.log('i : ' + i); // 1,2,3,4,5
    console.log('inside block:' + techName1);
    var version1 = 100;
}
console.log('outside: ' + i);
console.log('outside: ' + version1);

// ES6 syntax
let techName2 = 'LiveScript';

for (let n = 1; n <= 5; n++) {
    console.log('n : ' + n); // 1,2,3,4,5
    console.log('inside block:' + techName2);
    let version2 = 100;
}

// console.log(n); // undefined
// console.log('outside: ' + version2);  // undefined


// traditional var syntax
var PI1 = 3.14;
console.log(PI1); // 3.14

PI1 = 100;
console.log(PI1); // 100


// ES6 syntax
const PI2 = 6.28;
console.log('ES6 syntax const: ' + PI2); // 6.28

// string
var firstName = "Java";
var lastName = 'Script';
var message1 = "Welcome! How's you doing?";
var message2 = 'Welcome! How"s you doing?';


// number
let age = 35; // integer
var b = 29.03;  // floating-point number
const PI = 3.14;


// boolean
var isMale = true;
var isSenior = false;
var num1 = 10;
var num2 = 20;
var num3 = 10;

var isEqual = (num1 == num2);
console.log('isEqual: ' + isEqual);
console.log('num1 & num3 equal: ' + (num1 == num3));


// undefined
let dob;
console.log('dob1: ' + dob); // shows undefined

dob = undefined;
console.log('dob2: ' + dob); // shows undefined


// null
let technology = null;
console.log('technology: ' + technology); // shows undefined


// same variable can hold any type of data
let name = 'JavaScript'; // string
name = false; // boolean
name = 100; // number
console.log(name);
console.log(typeof (name));


// Arithmetic operators
var num1 = 10;
var num2 = 4;

console.log('Addition ' + (num1 + num2)); // 14
console.log('Subtraction ' + (num1 - num2)); // 6
console.log('Multiplication ' + num1 * num2); // 40
console.log('Division ' + num1 / num2); // 2.5
console.log('Modulus reminder ' + num1 % num2); // 2
num1++
console.log('after Increment ' + num1); // 11
num2--;
console.log('after Decrement ' + num2); // 3


num1 = 10;
num2 = 4;
console.log('Exponentiation ' + (num1 ** num2)); // (10 ** 4) = 10* 10 * 10 * 10 = 10000



// Logical operators - basic examples

// && (Logical AND) - returns true if both operands are true
console.log('true && true: ', true && true);
console.log('true && false: ', true && false);
console.log('false && true: ', false && true);

// || (Logical OR) - returns true if one of the operand is true
console.log('true || true: ', true || true);
console.log('true || false: ', true || false);
console.log('false || true: ', false || true);


// ! (Logical NOT) True if operand is not true (means I will be true if other is false)
var isSeniorCitizen = true;

var isYoungGeneration = !isSeniorCitizen;
console.log('isYoungGeneration: ', isYoungGeneration);


// Comparison (or Relational) operators
var num1 = 25;
var num2 = 35;
var num3 = "25";

console.log(num1 == num3);  // true
console.log(num1 === num3); // false
console.log(num1 != num2);  // true
console.log(num1 !== num3); // true
console.log(num1 < num2);   // true
console.log(num1 > num2);   // false
console.log(num1 <= num2);  // true
console.log(num1 >= num2);  // false


// Conditional (? or ternary) Operator

// age category
var currentAge = 100;
var category;

category = (currentAge < 18) ? 'Minor' : 'Major';
console.log('AGE category: ' + category);

// fees category
var isAuthorisedMember = true;
var fees;

fees = (isAuthorisedMember == true) ? 5 : 10;
console.log('fees / charges: ' + fees);

// Operator precedence
var result1 = 10 + 2 * 5
console.log('10 + 2 * 5 =  ' + result1); // answer is 20 NOT 60 (12 * 5 ), actually * or multiplication have higher precedence so the actual calculation is like 10 + ( 2*5 ) = 10 + 10 = 20

// change precedence with `parentheses ()` 
var result2 = (10 + 2) * 5;
console.log('(10 + 2) * 5 =  ' + result2); // (12) * 5 = 60

// same precedence operators
var result3 = 10 + 5 - 2
console.log('10 + 5 - 2 =  ' + result3); // 13 first addition than subtraction

var result4 = 10 + (5 - 2);
console.log('10 + (5 - 2) =  ' + result4); // 13 first subtraction ie. ( ) than addition

function showMessage() {
    //Body of function 
    //code to be executed
    console.log('welcome to JavaScript function');
}

//2. invoke / call the function
showMessage();

showMessage();



// var name = 'Dinanath';

// simple/normal function

//1. define / declare / create function
function sayHello() {
    //Body of function 
    //code to be executed
    console.log('Hello ' + name);
}

//2. invoke / call the function
sayHello();

name = 'Dino';

sayHello();


var total;
function calculateSum(num1, num2) {
    total = num1 + num2;
    console.log(total);
}

calculateSum(10, 20);
calculateSum(100, 200);



//1. define / declare / create function
function getSum(num1, num2) {
    //Body of function 
    //code to be executed
    var sum = num1 + num2;
    return (sum);
}

//2. invoke / call the function
console.log(getSum(10, 20));
console.log(getSum(100, 200));

var total = getSum(50, 50);
console.log(total);



// function declaration (Regular / normal function)
function getSum1(num1, num2) {
    var total = num1 + num2;
    return total;
}


// function expression - Anonymus
var getSum2 = function (num1, num2) {
    var total = num1 + num2;
    return total;
};

console.log(getSum2(10, 20));


// assign function to another variable
var sum1 = getSum2;
console.log(sum1(100, 200));

//   loops


for (let i = 1; i <= 5; i++) {
    console.log('Hello, The current index/num is: ' + i);
}


for (let i = 5; i >= 1; i--) {
    console.log('Hello, The current index/num is: ' + i);
}

let j = 1;

while (j <= 5) {
    console.log('Hello, The current index/num is: ' + j);
    j++;
}


do {
    console.log('Hello, The current index/num is: ' + j);
    j++;
}
while (j <= 5);


// An array with some elements
let arrColors = ["Red", "Green", "Blue", "Cyan", "Magenta", "Yellow", "Black"];

// Loop through all the elements in the array 
for (let color in arrColors) {
    console.log('Color is: ' + arrColors[color]);
}


// An object with some properties 
let objEmployee = { 'emp_name': 'Dinanath', 'emp_addres': 'Mumbai', 'emp_id': '029', 'emp_age': 35 };

// Loop through all the properties in the object  
for (emp in objEmployee) {
    console.log('Employee ' + emp + ' is: ' + objEmployee[emp]);
}


// Iterating over an array
let arrDays = ["Monday", "TuesDay", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

for (let day of arrDays) {
    console.log(day);
}

// Iterating over string
// let name = 'JavaScript';
for (let letter of name) {
    console.log(letter + ',');
}





// break continue statement

/* break */
// var arrDays = ["Monday", "TuesDay", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

var i = 1;
while (i <= 10) {
    if (i == 5) {
        break;
    }
    console.log(i);
    i++
}


for (var i = 0; i <= arrDays.length; i++) {
    if (i == 3) {
        break;
    }
    console.log(arrDays[i]);
}


/* continue */
i = 1;
while (i <= 20) {
    if (i % 2 == 0) {
        // console.log('Even Number ', i);
        i++;
        continue; // skip rest of the loop body

        i + 100; // non of use 
        console.log('just in even num continue'); // non of use 
    }
    console.log('Odd Number ', i);
    i++;
}


for (i = 1; i <= 10; i++) {
    if (i === 5) {
        continue; // skip rest of the loop body
        console.log('just after 5 continue...'); // non of use 
    }
    console.log(i);
}



let user = 'Dinanath';

if (user == 'Dinanath') {
    console.log('Welcome Dinanath!');
}

if (user == 'Dinanath') {
    console.log('Welcome Authorised User: ' + user + '!');
}


// let age = 20;

if (age >= 60) {
    console.log('SINIOR CIRIZEN!');
} else if (age < 18) {
    console.log('MINOR!');
} else {
    console.log('MAJOR - Middle Age!');
}


if (num1 == num2) {
    console.log('Both numbers are equal');
} else if (num1 < num2) {
    console.log('Number2 is greater!');
} else {
    console.log('Number1 is greater!');
}