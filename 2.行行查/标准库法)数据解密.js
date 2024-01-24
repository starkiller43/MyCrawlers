const crypto = require("crypto-js");

// 1.根据接口里面的域名后面的地址定位js文件
// 2.在js文件里面搜索有关标准库加密的关键字decrypt encrypt

function code(n, e) {
    var r = "3sd&d2"
      , c = "4h@$udD2s"
      , a = "*";
    e = e || "".concat(r).concat(c).concat(a);
    var t = crypto.enc.Utf8.parse(e)
      , i = crypto.AES.decrypt(n, t, {
        mode: crypto.mode.ECB,
        padding: crypto.pad.Pkcs7
    });
    return crypto.enc.Utf8.stringify(i).toString()
}

console.log(code())