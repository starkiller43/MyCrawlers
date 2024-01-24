const crypto = require("crypto-js");

function main2(t) {
    var e = crypto.enc.Utf8.parse('BE45D593014E4A4EB4449737660876CE')
      , n = crypto.enc.Utf8.parse('A8909931867B0425')
      , a = crypto.AES.decrypt(t, e, {
        iv: n,
        mode: crypto.mode.CBC,
        padding: crypto.pad.Pkcs7
    });
    return a.toString(crypto.enc.Utf8)
}
