const crypto = require("crypto-js");

function main(e) {
    var t = crypto.enc.Utf8.parse("SecretIs")
      , n = crypto.DES.decrypt({
        ciphertext: crypto.enc.Base64.parse(e)
    }, t, {
        mode: crypto.mode.ECB,
        padding: crypto.pad.Pkcs7
    });
    return JSON.parse(n.toString(crypto.enc.Utf8))
}