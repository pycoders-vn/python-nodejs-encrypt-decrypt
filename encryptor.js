var crypto = require('crypto');
var assert = require('assert');
var fs = require("fs");

var algorithm = 'aes256'; // or any other algorithm supported by OpenSSL
var secret_key = '7yBFR8L5wy42Pr9SAnEVp7PuKPQX7W3P';    // requied 32 characters
var iv = '0000000000000000';

// Read data in json
var data = fs.readFileSync('products.json', 'utf-8')
var text = JSON.stringify(data);

console.log(data)

// Encrypt with secret secret_key
var cipher = crypto.createCipheriv(algorithm, secret_key, iv);  
var encrypted = cipher.update(text, 'utf8', 'hex') + cipher.final('hex');
console.log('encrypted', encrypted, encrypted.length)
fs.writeFileSync('encrypted_by_node.txt', encrypted)