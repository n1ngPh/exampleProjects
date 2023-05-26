var CryptoJS = require('crypto-js')

function AESencrypt(_cRV, _2undefinedp){

         _2undefinedp = _2undefinedp.split("").reduce(function(_PUi, _JrX, _JP9) {
            return _JP9 % 2 == 0 ? _PUi + "" : _PUi + _JrX;}, "");
        _2undefinedp = CryptoJS.enc.Utf8.parse(_2undefinedp)

        _cRV = "string" == typeof _cRV ? _cRV : JSON.stringify(_cRV),
        _cRV  = CryptoJS.AES.encrypt(_cRV, _2undefinedp, {
            iv: _2undefinedp,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });

     return encodeURIComponent(_cRV.toString())
}

function AESdecrypt(_jzC, _73M){
    _73M = _73M.split("").reduce(function(_Szd, _PgX, _3fK){
        return _3fK % 2 == 0 ? _Szd + "" : _Szd + _PgX;
    },"");
    _73M = CryptoJS.enc.Utf8.parse(_73M)
    _jzC = CryptoJS.AES.decrypt(_jzC, _73M, {
            iv: _73M,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8);
    return JSON.parse(_jzC)
}
//
// var _jzC = '78pMZ9GVVT0D/bQ6DZN1liCIlz0nfw7y6ntqBQseE3qe3JdbduGoAnia6WfZc01THxmqUts0bnyHa3vcxuDZnmaxEZOfaif+oj8CESXoOAEq9XAW9qhhjIkNjnQzrV/a4d9Bwxp64cx9MOd/rTgdldehNH5QTnf5KZ1MWO2xANriDnrNrin74s+gdGx9YRhF2do5HtFeMZU6aCvqoh/f9FEfYZY237dIOKiO9KxEh2ySb10OFYfJjGrM20Yb/V3nd68/Kd5M9IsyFKdZh770DF7Hkekc4elRUEKoYqjHb0vZkMpFlra8Q4vUl7zJsyKYv5y27n8kn6BHXeShlq4AdzY5MUmeu7xnPmHoo5BIgS+dLtg78QtdNSQGxLcqNQOyd+2Zj34VX1VtBUIpEWhNZbivikGdwIwSdX6anbn5glA='
// var _73M = '4e255f72e268433db9fab3e3bee6f834'
//
// console.log(AESdecrypt(_jzC, _73M))