const CryptoJS = require("crypto-js");


function desEncrypt(e, t) {
    var n = CryptoJS.enc.Utf8.parse(t);
    return CryptoJS.DES.encrypt(e, n, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString()
}

function rndString() {
    for (var e = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz", t = "", n = 0; n < 16; n++) {
        var a = Math.floor(Math.random() * e.length);
        t += e.substring(a, a + 1)
    }
    return t
}

var a = {
    "username": "koyomi",
    "password": "123456",
    "captcha": "15"
}
var i = rndString()
console.log(desEncrypt(JSON.stringify(a), i))