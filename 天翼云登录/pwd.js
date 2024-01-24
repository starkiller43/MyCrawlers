
const CryptoJS = require("crypto-js");

function T1(e) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
      , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
      , r = t.enc
      , a = void 0 === r ? "Utf8" : r
      , o = t.mode
      , c = void 0 === o ? "ECB" : o
      , i = t.padding
      , u = void 0 === i ? "Pkcs7" : i
      , d = CryptoJS.enc[a].parse(n)
      , s = {
        mode: CryptoJS.mode[c],
        padding: CryptoJS.pad[u]
    }
      , l = CryptoJS.TripleDES.encrypt(e, d, s);
    return l.toString()
}

function T2(e) {
            var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
            if (e && "string" === typeof e) {
                var t = n.text || "0"
                  , r = n.length || 24;
                if (e.length < r)
                    for (var a = e.length; a < r; a++)
                        e += t;
                else
                    e = e.substring(0, r);
                return e
            }
        }

function T3() {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "";
    return e.replace(/\s+/g, "")
}

function getpwd(pwd) {
    return T1(pwd, T2('123456@163.com'))
}
console.log(getpwd('123456'))