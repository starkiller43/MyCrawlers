const CryptoJS = require("crypto-js");

function _utf8_encode(f) {
var e, h, g;
for (f = f.replace(/\r\n/g, "\n"),
e = "",
h = 0; h < f.length; h++) {
    g = f.charCodeAt(h),
    128 > g ? e += String.fromCharCode(g) : g > 127 && 2048 > g ? (e += String.fromCharCode(192 | g >> 6),
    e += String.fromCharCode(128 | 63 & g)) : (e += String.fromCharCode(224 | g >> 12),
    e += String.fromCharCode(128 | 63 & g >> 6),
    e += String.fromCharCode(128 | 63 & g))
}
return e
}

Base64 = {
    keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    encode: function (t) {
        var key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
        var r, q, p, o, n, m, l, s = "", k = 0;
        for (t = _utf8_encode(t); k < t.length;) {
            r = t.charCodeAt(k++),
                q = t.charCodeAt(k++),
                p = t.charCodeAt(k++),
                o = r >> 2,
                n = (3 & r) << 4 | q >> 4,
                m = (15 & q) << 2 | p >> 6,
                l = 63 & p,
                isNaN(q) ? m = l = 64 : isNaN(p) && (l = 64),
                s = s + key.charAt(o) + key.charAt(n) + key.charAt(m) + key.charAt(l)
        }
        return s
    }
}


b = '2fc106cd29ef2b3d6a4cf1948d911af6{"identityId":"15373505183","credential":"123456","captcha":"","capId":"bff52ef77e6b4f37a333d2909580dfbc","accountType":"PERSONALITY","gotourl":"","ls":"","pid":""}'


d = {
    "words": [
        -146469181,
        1483898620,
        589906541,
        -2003892524
    ],
    "sigBytes": 16
}

info = CryptoJS.AES.encrypt(b, d, {
        mode: CryptoJS.mode.ECB
}).ciphertext.toString();
d = Base64.encode(info)

console.log(d)

