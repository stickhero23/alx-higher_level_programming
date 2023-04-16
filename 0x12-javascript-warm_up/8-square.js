#!/usr/bin/node

const args = process.argv.slice(2);

let i = parseInt(args[0], 10);

if (isNaN(i)) {
	console.log("Missing size");
} else {
	for (let k = 0; k < i; k++) {
		console.log('X'.repeat(i));
	}
}
