#!/usr/bin/node

function myFactorial (number) {
  if (isNaN(number) || number === 0) {
    return 1;
  }
  if (number < 0) {
    return -1;
  }
  return number * myFactorial(number - 1);
}

console.log(myFactorial(Number(process.argv[2])));
