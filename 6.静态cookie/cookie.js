// 获取cookie的js代码

document = {}
location = {
    reload: function (){}
}

var s = {}, u, c, U, r, i, l = 0, a, e = eval, w = String.fromCharCode, sucuri_cloudproxy_js = '',
    S = 'ej0nbFk1Jy5jaGFyQXQoMikrJ2YnICsgICAnJyArJycrIjFjIi5jaGFyQXQoMCkgKyAgJycgKycnKyI3IiArICAnJyArIAonS2UnLnNsaWNlKDEsMikrJzInICsgICIwc2VjIi5zdWJzdHIoMCwxKSArICcwZicuc2xpY2UoMSwyKSsiOXNlYyIuc3Vic3RyKDAsMSkgKyAiNHN1Ii5zbGljZSgwLDEpICsgICcnICsgCiI4cyIuY2hhckF0KDApICsgJzYnICsgICI2Ii5zbGljZSgwLDEpICsgIiIgKydiJyArICBTdHJpbmcuZnJvbUNoYXJDb2RlKDB4NjMpICsgJzR5SDInLnN1YnN0cigzLCAxKSArIiIgKydUczkyJy5zdWJzdHIoMywgMSkgKyAnJyArIAoiYXN1Ii5zbGljZSgwLDEpICsgImYiLnNsaWNlKDAsMSkgKyAnPDcnLnNsaWNlKDEsMikrICcnICsiOCIuc2xpY2UoMCwxKSArICAnJyArJ2QnICsgICAnJyArJycrImJuIi5jaGFyQXQoMCkgKyAiNiIgKyAiMnN1Y3VyIi5jaGFyQXQoMCkrICcnICsgCidGNicuc2xpY2UoMSwyKSsiNyIuc2xpY2UoMCwxKSArICAnJyArIApTdHJpbmcuZnJvbUNoYXJDb2RlKDB4MzkpICsgImIiICsgIjNzZWMiLnN1YnN0cigwLDEpICsgIiIgKyJic3VjdXIiLmNoYXJBdCgwKSsgJycgKyAKJzgnICsgICIiICsnJztkb2N1bWVudC5jb29raWU9J3MnKydzdWN1cnUnLmNoYXJBdCg1KSArICdjc3VjdXInLmNoYXJBdCgwKSsgJ3N1Y3VydScuY2hhckF0KDUpICsgJ3N1Y3VyJy5jaGFyQXQoNCkrICdzaScuY2hhckF0KDEpKydfc3VjJy5jaGFyQXQoMCkrICdjJysnJysnbCcrJ3N1Y3VybycuY2hhckF0KDUpICsgJ3UnLmNoYXJBdCgwKSsnc2QnLmNoYXJBdCgxKSsncHN1Y3UnLmNoYXJBdCgwKSAgKydyc3VjJy5jaGFyQXQoMCkrICdvc3VjdXJpJy5jaGFyQXQoMCkgKyAneHN1Y3UnLmNoYXJBdCgwKSAgKydzdXknLmNoYXJBdCgyKSsnX3N1Jy5jaGFyQXQoMCkgKyd1c3VjJy5jaGFyQXQoMCkrICd1Jy5jaGFyQXQoMCkrJ2knKydkJysnX3N1Y3UnLmNoYXJBdCgwKSAgKyc1c3VjdScuY2hhckF0KDApICArJ3N1Y3VhJy5jaGFyQXQoNCkrICdmJysnNCcrJ2JzdWN1cmknLmNoYXJBdCgwKSArICdzdWN1cjMnLmNoYXJBdCg1KSArICdzdWN1cmlmJy5jaGFyQXQoNikrJzcnKydzdWQnLmNoYXJBdCgyKSsiPSIgKyB6ICsgJztwYXRoPS87bWF4LWFnZT04NjQwMCc7IGxvY2F0aW9uLnJlbG9hZCgpOw==';
L = S.length;
U = 0;
r = '';
var A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
for (u = 0; u < 64; u++) {
    s[A.charAt(u)] = u;
}
for (i = 0; i < L; i++) {
    c = s[S.charAt(i)];
    U = (U << 6) + c;
    l += 6;
    while (l >= 8) {
        ((a = (U >>> (l -= 8)) & 0xff) || (i < (L - 2))) && (r += w(a));
    }
}
e(r);

function main() {
    return document.cookie
}
