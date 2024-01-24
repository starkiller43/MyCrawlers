const crypto = require("crypto-js");

function h(t) {
    var f = {
        "words": [
            1785673834,
            964118391,
            624314466,
            2019968622
        ],
        "sigBytes": 16
    }
    var m = {
        "words": [
            808530483,
            875902519,
            943276354,
            1128547654
        ],
        "sigBytes": 16
    }
    var e = crypto.enc.Hex.parse(t)
      , n = crypto.enc.Base64.stringify(e)
      , a = crypto.AES.decrypt(n, f, {
        iv: m,
        mode: crypto.mode.CBC,
        padding: crypto.pad.Pkcs7
    })
      , r = a.toString(crypto.enc.Utf8);
    return r.toString()
}

function main(x) {
    return h(x)
}
