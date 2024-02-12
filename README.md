# recursion
 Recursion Examples

IF ALLAH gives permission tail call optimization is easy to grasp concept if you read this short article for converting any recursive function in tail call optimized form if compiler/interpereter doesn't make it implicitly : [https://medium.com/@JavaScript-World/javascript-recursion-and-tail-call-optimization-944be86bb3bb](https://medium.com/@JavaScript-World/javascript-recursion-and-tail-call-optimization-944be86bb3bb)


JavaScript: Recursion and Tail Call Optimization

The concept of recursion in computer science is a method where the solution to a problem depends on solutions to smaller instances of the same problem. Recursion can be a potent tool but, when used improperly, it can lead to issues like a stack overflow. This blog post will demystify the concepts of recursion in JavaScript and discuss the importance of tail call optimization.

# Understanding JavaScript Recursion

In JavaScript, a recursive function is a function that calls itself until it doesn’t. Let’s illustrate this with a basic example of calculating a factorial of a number:
```
function factorial(n) {
  // Base case: if n is 0 or 1, return 1
  if (n === 0 || n === 1) {
    return 1;
  }
  // Recursive case: n! = n * (n-1)!
  else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(5));  // Outputs: 120
```
In the above example, the function factorial calls itself to compute the factorial of a number. This is a simple and clean implementation, but it has a performance cost. Each recursive call adds a layer to the call stack, consuming memory. If the recursion is too deep, it could lead to a stack overflow error.

# Enter Tail Call Optimization

Tail Call Optimization (TCO) is a concept where the compiler converts a recursive call into an iterative loop, reducing the memory overhead. However, as of the date of this post, TCO is only supported in strict mode in ECMAScript 6 (ES6) and only in some JavaScript engines like Safari’s JavaScriptCore.

A function call is said to be in the tail position if it’s the final action of a function. In simpler terms, a tail call is when a function is called as the last operation in another function. Here’s how we can refactor the previous factorial function to make it tail-recursive:
```
function factorial(n, acc = 1) {
  // Base case: if n is 0 or 1, return the accumulator
  if (n === 0 || n === 1) {
    return acc;
  }
  // Recursive case: n! = n * (n-1)!, pass the accumulator along
  else {
    return factorial(n - 1, n * acc);
  }
}

console.log(factorial(5));  // Outputs: 120
```
Here, we introduced an accumulator (acc) to hold the result of the calculation as we go. This way, the last operation of the function is the recursive call, making it a tail call.

Motivational Quote

“The function of good software is to make the complex appear to be simple.” — Grady Booch

Remember, recursion is a powerful tool in your programming arsenal, but like any tool, it must be used wisely. Understanding how JavaScript handles recursion and tail calls is crucial in writing efficient, performant code
