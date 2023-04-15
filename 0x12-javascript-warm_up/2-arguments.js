#!/usr/bin/node

const args = process.argv.slice(2);
let numArgs = args.length;
if (numArgs > 1) {
	console.log("Arguments found");
} else if (numArgs == 1) {
	console.log("Argument found");
} else {
	console.log("No Argument");
}
