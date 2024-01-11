#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.foreach((cur) => {
    if (cur === searchElement) counter++;
  });
  return counter;
};
