#!/usr/bin/node

const args = process.argv.slice(2);

let a = parseInt(args[0]);
let b = parseInt(args[1]);

function add(a, b) {
	return (a + b);
}
console.log(add(a, b));
