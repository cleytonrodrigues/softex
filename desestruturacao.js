var a, b, rest;
[a, b] = [1, 2];
console.log("a=" + a); //1
console.log("b=" +b); // 2

[a, b, ,c,...rest] = [1, 2, 3, 4, 5, 6, 7];
console.log(a); // 1
console.log(b); // 2
console.log(c); // 4
console.log(rest); // [5, 6, 7]

({a, b} = {a:1, b:2});
console.log(a); // 1
console.log(b); // 2

// trocando variáveis

var a = 1;
var b = 3;

[a, b] = [b, a];
console.log(a); // 3
console.log(b); // 1


