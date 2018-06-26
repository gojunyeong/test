const fs = require('fs');


function startFunction() {
  return new Promise(function (resolve, reject) {
    let fileName = './input/'
    if (process.argv[2] != undefined) {
      fileName = fileName + process.argv[2];
    } else {
      fileName = fileName + 'test.txt';
    }
    fs.readFile(fileName, 'utf-8', function (err, result) {
      if (err) reject(err);
      resolve(result);
    });
  });
}

startFunction()
  .then(checkBracket)
  .then(function (result) {
    console.log(result)
  });

function checkBracket(text) {
  return new Promise(function (resolve, reject) {
    let result = false;
    let count = 0;
    if (text.length > 100000) {
      for (let i = 0; i < text.length; i++) {
        if (text[i] == '(') {
          count++;
        } else if (text[i] === ')') {
          count--;
        }else{
          reject(new Error({
            error: 'An invalid value was entered. Please enter only \'(\' or \')\''
          }))
        }  
        if (count < 0) {
          break;
        }
      }
      if (count == 0)
        result = true;
      resolve(result);
    } else {
      reject(new Error({
        error: 'The data entered is too long. Please enter no more than 100000 strings.'
      }))
    }
  });


}