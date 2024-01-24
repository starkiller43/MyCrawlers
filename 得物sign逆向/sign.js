
function _ff (t, e, n, r, i, o, a) {
    var s = t + (e & n | ~e & r) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}

function _gg(t, e, n, r, i, o, a) {
    var s = t + (e & r | n & ~r) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}

function _hh(t, e, n, r, i, o, a) {
    var s = t + (e ^ n ^ r) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}

function _ii(t, e, n, r, i, o, a) {
    var s = t + (n ^ (e | ~r)) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}

function i_stringToBytes(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push(255 & t.charCodeAt(n));
    return e
}

function n_stringToBytes(t) {
    return i_stringToBytes(unescape(encodeURIComponent(t)))
}

function wordsToBytes(t) {
    for (var e = [], n = 0; n < 32 * t.length; n += 8)
        e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
    return e
}

function e_bytesToWords(t) {
    for (var e = [], n = 0, r = 0; n < t.length; n++,
    r += 8)
        e[r >>> 5] |= t[n] << 24 - r % 32;
    return e
}

function rotl(t, e) {
    return t << e | t >>> 32 - e
}

function e_endian(t) {
    if (t.constructor == Number)
        return 16711935 & rotl(t, 8) | 4278255360 & rotl(t, 24);
    for (var e = 0; e < t.length; e++)
        t[e] = e_endian(t[e]);
    return t
}

function o(o, a) {
    o.constructor == String ? o = a && "binary" === a.encoding ? i_stringToBytes(o) : n_stringToBytes(o) : r(o) ? o = Array.prototype.slice.call(o, 0) : Array.isArray(o) || (o = o.toString());
    for (var s = e_bytesToWords(o), c = 8 * o.length, u = 1732584193, l = -271733879, f = -1732584194, d = 271733878, h = 0; h < s.length; h++)
        s[h] = 16711935 & (s[h] << 8 | s[h] >>> 24) | 4278255360 & (s[h] << 24 | s[h] >>> 8);
    s[c >>> 5] |= 128 << c % 32,
    s[14 + (c + 64 >>> 9 << 4)] = c;
    var p = _ff
      , g = _gg
      , v = _hh
      , m = _ii;
    for (h = 0; h < s.length; h += 16) {
        var _ = u
          , y = l
          , b = f
          , w = d;
        u = p(u, l, f, d, s[h + 0], 7, -680876936),
        d = p(d, u, l, f, s[h + 1], 12, -389564586),
        f = p(f, d, u, l, s[h + 2], 17, 606105819),
        l = p(l, f, d, u, s[h + 3], 22, -1044525330),
        u = p(u, l, f, d, s[h + 4], 7, -176418897),
        d = p(d, u, l, f, s[h + 5], 12, 1200080426),
        f = p(f, d, u, l, s[h + 6], 17, -1473231341),
        l = p(l, f, d, u, s[h + 7], 22, -45705983),
        u = p(u, l, f, d, s[h + 8], 7, 1770035416),
        d = p(d, u, l, f, s[h + 9], 12, -1958414417),
        f = p(f, d, u, l, s[h + 10], 17, -42063),
        l = p(l, f, d, u, s[h + 11], 22, -1990404162),
        u = p(u, l, f, d, s[h + 12], 7, 1804603682),
        d = p(d, u, l, f, s[h + 13], 12, -40341101),
        f = p(f, d, u, l, s[h + 14], 17, -1502002290),
        l = p(l, f, d, u, s[h + 15], 22, 1236535329),
        u = g(u, l, f, d, s[h + 1], 5, -165796510),
        d = g(d, u, l, f, s[h + 6], 9, -1069501632),
        f = g(f, d, u, l, s[h + 11], 14, 643717713),
        l = g(l, f, d, u, s[h + 0], 20, -373897302),
        u = g(u, l, f, d, s[h + 5], 5, -701558691),
        d = g(d, u, l, f, s[h + 10], 9, 38016083),
        f = g(f, d, u, l, s[h + 15], 14, -660478335),
        l = g(l, f, d, u, s[h + 4], 20, -405537848),
        u = g(u, l, f, d, s[h + 9], 5, 568446438),
        d = g(d, u, l, f, s[h + 14], 9, -1019803690),
        f = g(f, d, u, l, s[h + 3], 14, -187363961),
        l = g(l, f, d, u, s[h + 8], 20, 1163531501),
        u = g(u, l, f, d, s[h + 13], 5, -1444681467),
        d = g(d, u, l, f, s[h + 2], 9, -51403784),
        f = g(f, d, u, l, s[h + 7], 14, 1735328473),
        l = g(l, f, d, u, s[h + 12], 20, -1926607734),
        u = v(u, l, f, d, s[h + 5], 4, -378558),
        d = v(d, u, l, f, s[h + 8], 11, -2022574463),
        f = v(f, d, u, l, s[h + 11], 16, 1839030562),
        l = v(l, f, d, u, s[h + 14], 23, -35309556),
        u = v(u, l, f, d, s[h + 1], 4, -1530992060),
        d = v(d, u, l, f, s[h + 4], 11, 1272893353),
        f = v(f, d, u, l, s[h + 7], 16, -155497632),
        l = v(l, f, d, u, s[h + 10], 23, -1094730640),
        u = v(u, l, f, d, s[h + 13], 4, 681279174),
        d = v(d, u, l, f, s[h + 0], 11, -358537222),
        f = v(f, d, u, l, s[h + 3], 16, -722521979),
        l = v(l, f, d, u, s[h + 6], 23, 76029189),
        u = v(u, l, f, d, s[h + 9], 4, -640364487),
        d = v(d, u, l, f, s[h + 12], 11, -421815835),
        f = v(f, d, u, l, s[h + 15], 16, 530742520),
        l = v(l, f, d, u, s[h + 2], 23, -995338651),
        u = m(u, l, f, d, s[h + 0], 6, -198630844),
        d = m(d, u, l, f, s[h + 7], 10, 1126891415),
        f = m(f, d, u, l, s[h + 14], 15, -1416354905),
        l = m(l, f, d, u, s[h + 5], 21, -57434055),
        u = m(u, l, f, d, s[h + 12], 6, 1700485571),
        d = m(d, u, l, f, s[h + 3], 10, -1894986606),
        f = m(f, d, u, l, s[h + 10], 15, -1051523),
        l = m(l, f, d, u, s[h + 1], 21, -2054922799),
        u = m(u, l, f, d, s[h + 8], 6, 1873313359),
        d = m(d, u, l, f, s[h + 15], 10, -30611744),
        f = m(f, d, u, l, s[h + 6], 15, -1560198380),
        l = m(l, f, d, u, s[h + 13], 21, 1309151649),
        u = m(u, l, f, d, s[h + 4], 6, -145523070),
        d = m(d, u, l, f, s[h + 11], 10, -1120210379),
        f = m(f, d, u, l, s[h + 2], 15, 718787259),
        l = m(l, f, d, u, s[h + 9], 21, -343485551),
        u = u + _ >>> 0,
        l = l + y >>> 0,
        f = f + b >>> 0,
        d = d + w >>> 0
    }
    return e_endian([u, l, f, d])
}

function i_bytesToString(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push(String.fromCharCode(t[n]));
    return e.join("")
}

function e_bytesToHex(t) {
    for (var e = [], n = 0; n < t.length; n++)
        e.push((t[n] >>> 4).toString(16)),
        e.push((15 & t[n]).toString(16));
    return e.join("")
}

function p(t, n) {
    if (void 0 === t || null === t)
        throw new Error("Illegal argument " + t);
    var r = wordsToBytes(o(t, n));
    return n && n.asBytes ? r : n && n.asString ? i_bytesToString(r) : e_bytesToHex(r)
}

function g(t, e, n) {
    void 0 === e && (e = "048a9c4943398714b356a696503d2d36"),
    void 0 === n && (n = !1);
    var r = function(t, e) {
        return null === e ? void 0 : e
    }
      , i = function(t) {
        if ([void 0, null, ""].includes(t))
            return "";
        if ("[object Object]" === Object.prototype.toString.call(t))
            return JSON.stringify(t, r);
        if (Array.isArray(t)) {
            var e = "";
            return t.forEach((function(n, i) {
                "[object Object]" === Object.prototype.toString.call(n) ? e += JSON.stringify(n, r) : [void 0, null].includes(n) ? e += null : e += n.toString(),
                i < t.length - 1 && (e += ",")
            }
            )),
            e
        }
        return t.toString()
    }
      , o = Object.keys(t).sort().reduce((function(e, n) {
        return void 0 === t[n] ? e : e + n + i(t[n])
    }
    ), "");
    return /[\u00A0\u3000]/g.test(o),
    o += e,
    p(o)
}

function S() {
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}
      , n = "";
    return n = "048a9c4943398714b356a696503d2d36",
    g(e, n)
}


function get_sign() {
    var params = {
    "tabId": "",
    "limit": 20,
    "lastId": 2,
    "platform": "h5",
    "version": "4.73.0",
    "isVisitor": false,
    "newAdvForH5": true
    }

    return S(params)
}