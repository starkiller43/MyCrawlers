// getAllResponseHeaders



const jsdom = require('jsdom')
const { JSDOM } = jsdom
const dom = new JSDOM('<!doctype html><p> hello </p>')
window = dom.window
document = window.document
navigator = window.navigator

function _0x3ed467(_0x58f7d4) {
        for (var _0x4f1bcd = [-0x6f, 0x34, 0x5b, 0x41, -0x41, 0x74, 0x77, 0x6a, -0x79, -0x52, -0x5, 0x50, 0x33, 0x61, 0x44, -0x53, -0x70, -0x33, 0x17, -0x2e, -0x22, -0x72, -0x37, -0xb, -0x7f, 0x5a, 0x21, 0x16, -0x1f, 0x32, -0x11, 0x14, -0x2c, 0xf, -0x5e, -0x7b, 0x76, -0x17, -0x3d, 0x72, 0x47, -0x68, -0x7e, -0x75, -0x51, -0x36, -0x12, -0x6e, -0x4, -0x5f, -0x5b, 0x5e, -0x50, -0xe, 0x78, 0x69, 0x55, 0x68, -0x56, -0x6c, 0x43, 0x19, 0x65, 0x6c, 0x10, -0x69, 0x6f, -0xa, 0x75, -0x49, 0x4d, 0x59, -0x1d, -0x62, -0x44, 0x70, 0x6b, -0x1, 0x56, 0x79, 0x58, -0x65, -0x7c, 0x45, -0x1e, -0x8, -0x71, -0x4a, -0x76, 0x39, -0x19, 0xc, -0x73, -0x6a, 0x5f, 0x7f, 0x54, 0x7c, -0x66, -0x1c, 0x49, 0x2b, -0x3c, 0x1c, 0x2e, 0x73, 0x1e, 0x7a, -0x4b, 0x7d, -0x43, -0x4d, 0x3, -0x7, -0x35, -0xd, 0x35, 0x4e, -0x48, 0x1, 0xb, -0x47, -0x27, -0x4f, -0x3, 0x13, 0x29, 0x7e, -0x2b, -0x7d, -0x1b, 0x22, 0x3f, 0x8, 0x48, -0x23, -0x29, -0x3f, 0x3c, -0x18, 0x66, 0x2f, -0x77, -0x67, -0x16, 0x2d, 0x3b, 0x40, -0x60, 0x31, 0x53, -0x6b, -0x78, -0x39, -0x46, 0x0, -0x26, -0x54, -0x28, 0x18, 0xe, 0x30, 0x1d, 0x2c, -0x24, -0x2f, 0x38, -0x5c, 0x26, 0x25, 0x4, -0x32, 0x67, 0xa, -0x59, 0x37, 0x71, -0x1a, 0x6e, 0x36, 0x24, -0x14, -0x4e, -0xc, -0x74, 0x46, -0x25, 0x5, -0x3e, -0x4c, -0x30, -0x40, 0x4f, 0x64, 0x28, 0x6, -0x3a, -0x5a, -0x13, -0x9, 0x27, 0x5d, -0x63, 0x15, 0x7, 0x1a, -0x2, 0x1b, -0x2d, 0x51, 0x3a, -0x7a, 0x4c, -0x42, 0x2, 0x5c, -0x2a, 0x62, -0x10, 0x9, 0x3d, 0x3e, -0xf, 0x63, -0x15, 0x1f, -0x38, 0x57, 0x11, -0x34, -0x45, -0x21, -0x3b, -0x55, 0x42, 0x4a, 0x12, -0x5d, -0x80, -0x57, -0x20, 0x2a, 0x20, -0x58, 0x6d, 0x60, 0xd, -0x6, 0x4b, -0x64, -0x31, 0x23, -0x61, 0x52, -0x6d, 0x7b], _0x39eb66 = 0x0, _0x46445e = 0x0, _0x1360a5 = 0x0, _0x596013 = new Array(), _0x411913 = 0x0; _0x411913 < _0x58f7d4['length']; _0x411913++) {
            _0x39eb66 = _0x39eb66 + 0x1 & 0xff,
            _0x46445e = (0xff & _0x4f1bcd[_0x39eb66]) + _0x46445e & 0xff;
            var _0x5e20d4 = _0x4f1bcd[_0x39eb66];
            _0x4f1bcd[_0x39eb66] = _0x4f1bcd[_0x46445e],
            _0x4f1bcd[_0x46445e] = _0x5e20d4,
            _0x1360a5 = (0xff & _0x4f1bcd[_0x39eb66]) + (0xff & _0x4f1bcd[_0x46445e]) & 0xff,
            _0x596013['push'](_0x58f7d4[_0x411913] ^ _0x4f1bcd[_0x1360a5]);
        }
        return _0x596013;
    }

function _0x3ef903(_0x44e9d9) {
    for (var _0x39da63, _0x53f955, _0x16f530 = '', _0x134aef = 0x0; _0x134aef < _0x44e9d9['length']; )
        _0x39da63 = _0x44e9d9[_0x134aef],
        _0x53f955 = 0x0,
        _0x39da63 >>> 0x7 === 0x0 ? (_0x16f530 += String['fromCharCode'](_0x44e9d9[_0x134aef]),
        _0x134aef += 0x1) : 0xfc === (0xfc & _0x39da63) ? (_0x53f955 = (0x3 & _0x44e9d9[_0x134aef]) << 0x1e,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x1]) << 0x18,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x2]) << 0x12,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x3]) << 0xc,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x4]) << 0x6,
        _0x53f955 |= 0x3f & _0x44e9d9[_0x134aef + 0x5],
        _0x16f530 += String['fromCharCode'](_0x53f955),
        _0x134aef += 0x6) : 0xf8 === (0xf8 & _0x39da63) ? (_0x53f955 = (0x7 & _0x44e9d9[_0x134aef]) << 0x18,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x1]) << 0x12,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x2]) << 0xc,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x3]) << 0x6,
        _0x53f955 |= 0x3f & _0x44e9d9[_0x134aef + 0x4],
        _0x16f530 += String['fromCharCode'](_0x53f955),
        _0x134aef += 0x5) : 0xf0 === (0xf0 & _0x39da63) ? (_0x53f955 = (0xf & _0x44e9d9[_0x134aef]) << 0x12,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x1]) << 0xc,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x2]) << 0x6,
        _0x53f955 |= 0x3f & _0x44e9d9[_0x134aef + 0x3],
        _0x16f530 += String['fromCharCode'](_0x53f955),
        _0x134aef += 0x4) : 0xe0 === (0xe0 & _0x39da63) ? (_0x53f955 = (0x1f & _0x44e9d9[_0x134aef]) << 0xc,
        _0x53f955 |= (0x3f & _0x44e9d9[_0x134aef + 0x1]) << 0x6,
        _0x53f955 |= 0x3f & _0x44e9d9[_0x134aef + 0x2],
        _0x16f530 += String['fromCharCode'](_0x53f955),
        _0x134aef += 0x3) : 0xc0 === (0xc0 & _0x39da63) ? (_0x53f955 = (0x3f & _0x44e9d9[_0x134aef]) << 0x6,
        _0x53f955 |= 0x3f & _0x44e9d9[_0x134aef + 0x1],
        _0x16f530 += String['fromCharCode'](_0x53f955),
        _0x134aef += 0x2) : (_0x16f530 += String['fromCharCode'](_0x44e9d9[_0x134aef]),
        _0x134aef += 0x1);
    return _0x16f530;
}

function _0x4207c2(_0x2219f6) {
    for (var _0x9c7ad4 = window['atob'](_0x2219f6), _0x2dd788 = new Int8Array(_0x9c7ad4['length']), _0x7c7af6 = 0x0; _0x7c7af6 < _0x9c7ad4['length']; _0x7c7af6++)
        _0x2dd788[_0x7c7af6] = _0x9c7ad4['charCodeAt'](_0x7c7af6);
    return _0x2dd788;
}

function _0x563330(_0x1e29f9) {
    return _0x3ef903(_0x3ed467(_0x4207c2(_0x1e29f9)));
}

function main(x) {
    return JSON['parse'](_0x563330(x))
}
