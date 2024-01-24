function _ff(e, t, n, r, o, i, a) {
    var s = e + (t & n | ~t & r) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}
function _gg(e, t, n, r, o, i, a) {
    var s = e + (t & r | n & ~r) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}
function _hh(e, t, n, r, o, i, a) {
    var s = e + (t ^ n ^ r) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}
function _ii(e, t, n, r, o, i, a) {
    var s = e + (n ^ (t | ~r)) + (o >>> 0) + a;
    return (s << i | s >>> 32 - i) + t
}

function i_stringToBytes(e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push(255 & e.charCodeAt(n));
    return t
}
function r_stringToBytes(e) {
    return i_stringToBytes(unescape(encodeURIComponent(e)))
}

function a(e, n) {
    e.constructor == String ? e = n && "binary" === n.encoding ? i_stringToBytes(e) : r_stringToBytes(e) : o(e) ? e = Array.prototype.slice.call(e, 0) : Array.isArray(e) || e.constructor === Uint8Array || (e = e.toString());
    for (var s = bytesToWords(e), u = 8 * e.length, c = 1732584193, l = -271733879, f = -1732584194, p = 271733878, d = 0; d < s.length; d++)
        s[d] = 16711935 & (s[d] << 8 | s[d] >>> 24) | 4278255360 & (s[d] << 24 | s[d] >>> 8);
    s[u >>> 5] |= 128 << u % 32,
    s[14 + (u + 64 >>> 9 << 4)] = u;
    var h = _ff
      , g = _gg
      , v = _hh
      , y = _ii;
    for (d = 0; d < s.length; d += 16) {
        var m = c
          , b = l
          , O = f
          , w = p;
        c = h(c, l, f, p, s[d + 0], 7, -680876936),
        p = h(p, c, l, f, s[d + 1], 12, -389564586),
        f = h(f, p, c, l, s[d + 2], 17, 606105819),
        l = h(l, f, p, c, s[d + 3], 22, -1044525330),
        c = h(c, l, f, p, s[d + 4], 7, -176418897),
        p = h(p, c, l, f, s[d + 5], 12, 1200080426),
        f = h(f, p, c, l, s[d + 6], 17, -1473231341),
        l = h(l, f, p, c, s[d + 7], 22, -45705983),
        c = h(c, l, f, p, s[d + 8], 7, 1770035416),
        p = h(p, c, l, f, s[d + 9], 12, -1958414417),
        f = h(f, p, c, l, s[d + 10], 17, -42063),
        l = h(l, f, p, c, s[d + 11], 22, -1990404162),
        c = h(c, l, f, p, s[d + 12], 7, 1804603682),
        p = h(p, c, l, f, s[d + 13], 12, -40341101),
        f = h(f, p, c, l, s[d + 14], 17, -1502002290),
        c = g(c, l = h(l, f, p, c, s[d + 15], 22, 1236535329), f, p, s[d + 1], 5, -165796510),
        p = g(p, c, l, f, s[d + 6], 9, -1069501632),
        f = g(f, p, c, l, s[d + 11], 14, 643717713),
        l = g(l, f, p, c, s[d + 0], 20, -373897302),
        c = g(c, l, f, p, s[d + 5], 5, -701558691),
        p = g(p, c, l, f, s[d + 10], 9, 38016083),
        f = g(f, p, c, l, s[d + 15], 14, -660478335),
        l = g(l, f, p, c, s[d + 4], 20, -405537848),
        c = g(c, l, f, p, s[d + 9], 5, 568446438),
        p = g(p, c, l, f, s[d + 14], 9, -1019803690),
        f = g(f, p, c, l, s[d + 3], 14, -187363961),
        l = g(l, f, p, c, s[d + 8], 20, 1163531501),
        c = g(c, l, f, p, s[d + 13], 5, -1444681467),
        p = g(p, c, l, f, s[d + 2], 9, -51403784),
        f = g(f, p, c, l, s[d + 7], 14, 1735328473),
        c = v(c, l = g(l, f, p, c, s[d + 12], 20, -1926607734), f, p, s[d + 5], 4, -378558),
        p = v(p, c, l, f, s[d + 8], 11, -2022574463),
        f = v(f, p, c, l, s[d + 11], 16, 1839030562),
        l = v(l, f, p, c, s[d + 14], 23, -35309556),
        c = v(c, l, f, p, s[d + 1], 4, -1530992060),
        p = v(p, c, l, f, s[d + 4], 11, 1272893353),
        f = v(f, p, c, l, s[d + 7], 16, -155497632),
        l = v(l, f, p, c, s[d + 10], 23, -1094730640),
        c = v(c, l, f, p, s[d + 13], 4, 681279174),
        p = v(p, c, l, f, s[d + 0], 11, -358537222),
        f = v(f, p, c, l, s[d + 3], 16, -722521979),
        l = v(l, f, p, c, s[d + 6], 23, 76029189),
        c = v(c, l, f, p, s[d + 9], 4, -640364487),
        p = v(p, c, l, f, s[d + 12], 11, -421815835),
        f = v(f, p, c, l, s[d + 15], 16, 530742520),
        c = y(c, l = v(l, f, p, c, s[d + 2], 23, -995338651), f, p, s[d + 0], 6, -198630844),
        p = y(p, c, l, f, s[d + 7], 10, 1126891415),
        f = y(f, p, c, l, s[d + 14], 15, -1416354905),
        l = y(l, f, p, c, s[d + 5], 21, -57434055),
        c = y(c, l, f, p, s[d + 12], 6, 1700485571),
        p = y(p, c, l, f, s[d + 3], 10, -1894986606),
        f = y(f, p, c, l, s[d + 10], 15, -1051523),
        l = y(l, f, p, c, s[d + 1], 21, -2054922799),
        c = y(c, l, f, p, s[d + 8], 6, 1873313359),
        p = y(p, c, l, f, s[d + 15], 10, -30611744),
        f = y(f, p, c, l, s[d + 6], 15, -1560198380),
        l = y(l, f, p, c, s[d + 13], 21, 1309151649),
        c = y(c, l, f, p, s[d + 4], 6, -145523070),
        p = y(p, c, l, f, s[d + 11], 10, -1120210379),
        f = y(f, p, c, l, s[d + 2], 15, 718787259),
        l = y(l, f, p, c, s[d + 9], 21, -343485551),
        c = c + m >>> 0,
        l = l + b >>> 0,
        f = f + O >>> 0,
        p = p + w >>> 0
    }
    return endian([c, l, f, p])
}
function rotl(e, t) {
    return e << t | e >>> 32 - t
}
function endian(e) {
    if (e.constructor == Number)
        return 16711935 & rotl(e, 8) | 4278255360 & rotl(e, 24);
    for (var t = 0; t < e.length; t++)
        e[t] = endian(e[t]);
    return e
}

function bytesToWords(e) {
    for (var t = [], n = 0, r = 0; n < e.length; n++,
    r += 8)
        t[r >>> 5] |= e[n] << 24 - r % 32;
    return t
}
function bytesToHex(e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push((e[n] >>> 4).toString(16)),
        t.push((15 & e[n]).toString(16));
    return t.join("")
}
function wordsToBytes(e) {
    for (var t = [], n = 0; n < 32 * e.length; n += 8)
        t.push(e[n >>> 5] >>> 24 - n % 32 & 255);
    return t
}

function o(e, n) {
    var r = wordsToBytes(a(e, n));
    return bytesToHex(r)
}

function get_code(time) {
    var n = time.toString()
        r = o(n + "9527" + n.substr(0, 6))
    return r
}
