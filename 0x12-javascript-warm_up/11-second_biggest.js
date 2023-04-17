#!/usr/bin/node

const args = process.argv.slice(2);
function SecondMax (myArgs) {
	if (myArgs.length < 2) {
		return (0);
	} else {
		myArgs.sort((x, y) => x - y);
		myArgs.pop();
		return (myArgs.pop());
	}
}
console.log(secondMax(args);

