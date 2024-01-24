
function l(e, t) {
    var n = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
}

function a(e, t, n, o, r, i) {
    return l((t = l(l(t, e), l(o, i))) << r | t >>> 32 - r, n)
}

function p(e, t, n, o, r, i, s) {
    return a(t & n | ~t & o, e, t, r, i, s)
}

function f(e, t, n, o, r, i, s) {
    return a(t & o | n & ~o, e, t, r, i, s)
}

function m(e, t, n, o, r, i, s) {
    return a(t ^ n ^ o, e, t, r, i, s)
}

function g(e, t, n, o, r, i, s) {
    return a(n ^ (t | ~o), e, t, r, i, s)
}

function s(e, t) {
    e[t >> 5] |= 128 << t % 32,
        e[14 + (t + 64 >>> 9 << 4)] = t;
    for (var n, o, r, d, i = 1732584193, s = -271733879, a = -1732584194, c = 271733878, u = 0; u < e.length; u += 16)
        i = p(n = i, o = s, r = a, d = c, e[u], 7, -680876936),
            c = p(c, i, s, a, e[u + 1], 12, -389564586),
            a = p(a, c, i, s, e[u + 2], 17, 606105819),
            s = p(s, a, c, i, e[u + 3], 22, -1044525330),
            i = p(i, s, a, c, e[u + 4], 7, -176418897),
            c = p(c, i, s, a, e[u + 5], 12, 1200080426),
            a = p(a, c, i, s, e[u + 6], 17, -1473231341),
            s = p(s, a, c, i, e[u + 7], 22, -45705983),
            i = p(i, s, a, c, e[u + 8], 7, 1770035416),
            c = p(c, i, s, a, e[u + 9], 12, -1958414417),
            a = p(a, c, i, s, e[u + 10], 17, -42063),
            s = p(s, a, c, i, e[u + 11], 22, -1990404162),
            i = p(i, s, a, c, e[u + 12], 7, 1804603682),
            c = p(c, i, s, a, e[u + 13], 12, -40341101),
            a = p(a, c, i, s, e[u + 14], 17, -1502002290),
            i = f(i, s = p(s, a, c, i, e[u + 15], 22, 1236535329), a, c, e[u + 1], 5, -165796510),
            c = f(c, i, s, a, e[u + 6], 9, -1069501632),
            a = f(a, c, i, s, e[u + 11], 14, 643717713),
            s = f(s, a, c, i, e[u], 20, -373897302),
            i = f(i, s, a, c, e[u + 5], 5, -701558691),
            c = f(c, i, s, a, e[u + 10], 9, 38016083),
            a = f(a, c, i, s, e[u + 15], 14, -660478335),
            s = f(s, a, c, i, e[u + 4], 20, -405537848),
            i = f(i, s, a, c, e[u + 9], 5, 568446438),
            c = f(c, i, s, a, e[u + 14], 9, -1019803690),
            a = f(a, c, i, s, e[u + 3], 14, -187363961),
            s = f(s, a, c, i, e[u + 8], 20, 1163531501),
            i = f(i, s, a, c, e[u + 13], 5, -1444681467),
            c = f(c, i, s, a, e[u + 2], 9, -51403784),
            a = f(a, c, i, s, e[u + 7], 14, 1735328473),
            i = m(i, s = f(s, a, c, i, e[u + 12], 20, -1926607734), a, c, e[u + 5], 4, -378558),
            c = m(c, i, s, a, e[u + 8], 11, -2022574463),
            a = m(a, c, i, s, e[u + 11], 16, 1839030562),
            s = m(s, a, c, i, e[u + 14], 23, -35309556),
            i = m(i, s, a, c, e[u + 1], 4, -1530992060),
            c = m(c, i, s, a, e[u + 4], 11, 1272893353),
            a = m(a, c, i, s, e[u + 7], 16, -155497632),
            s = m(s, a, c, i, e[u + 10], 23, -1094730640),
            i = m(i, s, a, c, e[u + 13], 4, 681279174),
            c = m(c, i, s, a, e[u], 11, -358537222),
            a = m(a, c, i, s, e[u + 3], 16, -722521979),
            s = m(s, a, c, i, e[u + 6], 23, 76029189),
            i = m(i, s, a, c, e[u + 9], 4, -640364487),
            c = m(c, i, s, a, e[u + 12], 11, -421815835),
            a = m(a, c, i, s, e[u + 15], 16, 530742520),
            i = g(i, s = m(s, a, c, i, e[u + 2], 23, -995338651), a, c, e[u], 6, -198630844),
            c = g(c, i, s, a, e[u + 7], 10, 1126891415),
            a = g(a, c, i, s, e[u + 14], 15, -1416354905),
            s = g(s, a, c, i, e[u + 5], 21, -57434055),
            i = g(i, s, a, c, e[u + 12], 6, 1700485571),
            c = g(c, i, s, a, e[u + 3], 10, -1894986606),
            a = g(a, c, i, s, e[u + 10], 15, -1051523),
            s = g(s, a, c, i, e[u + 1], 21, -2054922799),
            i = g(i, s, a, c, e[u + 8], 6, 1873313359),
            c = g(c, i, s, a, e[u + 15], 10, -30611744),
            a = g(a, c, i, s, e[u + 6], 15, -1560198380),
            s = g(s, a, c, i, e[u + 13], 21, 1309151649),
            i = g(i, s, a, c, e[u + 4], 6, -145523070),
            c = g(c, i, s, a, e[u + 11], 10, -1120210379),
            a = g(a, c, i, s, e[u + 2], 15, 718787259),
            s = g(s, a, c, i, e[u + 9], 21, -343485551),
            i = l(i, n),
            s = l(s, o),
            a = l(a, r),
            c = l(c, d);
    return [i, s, a, c]
}

function c(e) {
    for (var t = "", n = 0; n < 32 * e.length; n += 8)
        t += String.fromCharCode(e[n >> 5] >>> n % 32 & 255);
    return t
}

function u(e) {
    var t, n = [];
    for (n[(e.length >> 2) - 1] = void 0,
             t = 0; t < n.length; t += 1)
        n[t] = 0;
    for (t = 0; t < 8 * e.length; t += 8)
        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}

function o(e) {
    for (var t, n = "0123456789abcdef", o = "", r = 0; r < e.length; r += 1)
        t = e.charCodeAt(r),
            o += n.charAt(t >>> 4 & 15) + n.charAt(15 & t);
    return o
}

function d(e) {
    return unescape(encodeURIComponent(e))
}

function r(e) {
    return c(s(u(e = d(e)), 8 * e.length))
}

function i(e, t) {
    var n, e = d(e), t = d(t), o = u(e), r = [], i = [];
    for (r[15] = i[15] = void 0,
         16 < o.length && (o = s(o, 8 * e.length)),
             n = 0; n < 16; n += 1)
        r[n] = 909522486 ^ o[n],
            i[n] = 1549556828 ^ o[n];
    return e = s(r.concat(u(t)), 512 + 8 * t.length),
        c(s(i.concat(e), 640))
}

function encode(e, t, n) {
    return t ? n ? i(t, e) : o(i(t, e)) : n ? r(e) : o(r(e))
}

function main(pwd){
    pass = encode(pwd.substr(0, 16))
    return pass
}
