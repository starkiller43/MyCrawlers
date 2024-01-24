const CryptoJS = require("crypto-js");

function jslencode(text) {
    var aes_key = '397151C04723421F'
    var key = CryptoJS.enc.Utf8.parse(aes_key);
    var iv = CryptoJS.enc.Utf8.parse("");
    var srcs = CryptoJS.enc.Utf8.parse(text);
    var encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.ciphertext.toString(CryptoJS.enc.Hex)
}


// kbzw__user_login=7Obd08_P1ebax9aXwZmskauopbGVoIKvpuXK7N_u0ejF1dSesMLWk6etqaDdnKuWrcSq2qirx9OU2q3by6ye3JenwtuYrqXW2cXS1qCasqOtmaiWmLKgubXOvp-qq6Gro6yWqpmqmK6ltrG_0aTC2PPV487XkKylo5iJx8ri3eTg7IzFtpaSp6Wjs4HHyuKvqaSZ5K2Wn4G45-PkxsfG1sTe3aihqpmklK2Xm8OpxK7ApZXV4tfcgr3G2uLioYGzyebo4s6onaiUpJGlp6GogcPC2trn0qihqpmklK2XuNzIn5Klq6OZp52ulKiPras.; path=/