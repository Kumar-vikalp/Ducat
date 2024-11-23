// Variables


// Using a variable without var, let, or const
a = 10; 
// Without var, let, or const, a is implicitly declared in the global scope
console.log(a); // 10

// Declaring a variable using 'var'
var a; 
console.log(a); // undefined
// Explanation: 
// - a was declared but not initialized, so its value is 'undefined'.

// Declaring a variable and assigning null
var b = null; 
console.log(b); // null
// Explanation: 
// - b is explicitly assigned 'null', which means it is intentionally empty (no value).

// Difference between null and undefined
// null = intentionally empty or no value
// undefined = variable is declared but not assigned a value yet
var c; // Declaration only
console.log(c); // undefined
// Explanation:
// - c is declared but not assigned any value, so its default value is 'undefined'.

// Hoisting in 'var' declarations
console.log(d); // undefined
var d = 10;
// Explanation:
// - 'var' declarations are hoisted to the top of the scope. 
//   The declaration part is moved up but not the initialization, so it's 'undefined' before assignment.

// Example 6: Using 'const' (constant variables)
// console.log(e); // ReferenceError: Cannot access 'e' before initialization
// const e = 10;
// Explanation:
// - 'const' variables are **not hoisted** like 'var', and they must be initialized before use.
// - 'const' also doesn't allow reassignment. It's fixed once set.

// Example 7: Demonstrating basic operators
let x = 10;
let y = 5;

// Arithmetic Operators (+, -, *, /, %, **)
console.log(x + y); // 15
console.log(x - y); // 5
console.log(x * y); // 50
console.log(x / y); // 2
console.log(x % y); // 0 (modulus)
console.log(x ** y); // 100000 (exponentiation)
// Comparison Operators (==, ===, !=, !==, <, >, <=, >=)
console.log(x == y);  // false (compares values)
console.log(x === y); // false (compares values and types)
console.log(x != y);  // true (compares values)
console.log(x !== y); // true (compares values and types)
console.log(x > y);   // true
console.log(x < y);   // false
console.log(x <= y);  // false
console.log(x >= y);  // true
// Logical Operators (&&, ||, !)
console.log(x > 5 && y < 10); // true (AND)
console.log(x > 15 || y < 10); // false (OR)
console.log(!(x == y));        // true (NOT)

// Ternary Operator (Condition ? value_if_true : value_if_false)
let result = (x > y) ? "x is greater" : "y is greater or equal";
console.log(result); // "x is greater"

// Assignment Operators (=, +=, -=, *=, /=, %=)
x += 5;  // x = x + 5
console.log(x);  // 15

x *= 2;  // x = x * 2
console.log(x);  // 30

x /= 3;  // x = x / 3
console.log(x);  // 10

x %= 3;  // x = x % 3
console.log(x);  // 1


// Increment and Decrement Operators (++, --)
let z = 5;
console.log(z++); // 5 (Post-increment: returns the current value, then increments)
console.log(z);   // 6

console.log(++z); // 7 (Pre-increment: increments first, then returns the value)

console.log(z--); // 7 (Post-decrement: returns the current value, then decrements)
console.log(z);   // 6

console.log(--z); // 5 (Pre-decrement: decrements first, then returns the value)
