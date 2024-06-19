var window = globalThis;
var navigator = {};
var document = {};
document.cookie = {
    match: function(){return}
}
document.createElement = function(aa){
    return `<${aa}></${aa}>`
}
window.window = window

window.navigator = {
    'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
window.location = {
    "ancestorOrigins": {},
    "href": "https://y.qq.com/n/ryqq/player",
    "origin": "https://y.qq.com",
    "protocol": "https:",
    "host": "y.qq.com",
    "hostname": "y.qq.com",
    "port": "",
    "pathname": "/n/ryqq/player",
    "search": "",
    "hash": ""
}



function createProxy(obj, name) {
    return new Proxy(obj, {
        set(target, property, value) {
            console.log("获取属性set", ' 名称:', name, ' 属性:', property, ' 类型:', typeof target[property]);
            console.table([{ "类型": "set", "调用者": target, "调用属性": property, "设置值": value }]);
            return Reflect.set(target, property, value);
        },
        get(target, property, receiver) {
            if (property === '需要debugger的属性') {
                debugger;
            }
            let value = target[property];
            console.log("获取属性get", ' 名称:', name, ' 属性:', property, ' 类型:', typeof value);
            console.table([{ "类型": "get", "调用者": target, "调用属性": property, "获取值": value }]);

            // 如果属性是对象，递归创建代理
            if (value && typeof value === 'object' && value !== target) {
                return createProxy(value, `${name}.${property.toString()}`);
            }

            return value;
        },
    });
}

// 创建代理并设置全局对象
// window = createProxy(window || {}, 'window');
// location = createProxy(location || {}, 'location');
// navigator = createProxy(navigator || {}, 'navigator');
// document = createProxy(document || {}, 'document');



!function (e) {
    var a = {}
        , n = {
            21: 0
        }
        , o = {
            21: 0
        }
        , f = [];
    function d(t) {
        if (a[t])
            return a[t].exports;
        var r = a[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(r.exports, r, r.exports, d),
            r.l = !0,
            r.exports
    };
    window.dd = d;

}([
    function(t, e, n) {
    var r = "undefined" !== typeof context && context.window && context.window.response
      , i = "undefined" !== typeof context && context.window && context.window.request
      , o = !1;
    try {
        o = "undefined" !== typeof document
    } catch (yn) {
        o = !1
    }
    var a, u, s, c = o, l = function(t) {
        var e = null;
        if (c) {
            var n = document.cookie.match(RegExp("(^|;\\s*)" + t + "=([^;]*)(;|$)"));
            e = n ? decodeURIComponent(n[2]) : ""
        } else
            e = (null === i || void 0 === i ? void 0 : i.cookies[t]) || "";
        return function(t) {
            if (!t)
                return t;
            for (; t !== decodeURIComponent(t); )
                t = decodeURIComponent(t);
            var e = ["<", ">", "'", '"', "%3c", "%3e", "%27", "%22", "%253c", "%253e", "%2527", "%2522"]
              , n = ["&#x3c;", "&#x3e;", "&#x27;", "&#x22;", "%26%23x3c%3B", "%26%23x3e%3B", "%26%23x27%3B", "%26%23x22%3B", "%2526%2523x3c%253B", "%2526%2523x3e%253B", "%2526%2523x27%253B", "%2526%2523x22%253B"];
            return e.forEach((function(r, i) {
                t = t.replace(new RegExp(e[i],"gi"), n[i])
            }
            )),
            t
        }(e)
    }, f = function(t) {
        var e, n = 5381;
        if (e = t ? l("qqmusic_key") || l("p_skey") || l("skey") || l("p_lskey") || l("lskey") : l("skey") || l("qqmusic_key"))
            for (var r = 0, i = e.length; r < i; ++r)
                n += (n << 5) + e.charCodeAt(r);
        return 2147483647 & n
    }, p = Object.freeze({
        __proto__: null,
        getCookie: l,
        delCookie: function(t, e, n) {
            document.cookie = t + "=; expires=Mon, 26 Jul 1997 05:00:00 GMT;" + (n ? "path=" + n + "; " : "path=/; ") + "domain=" + (e || window.location.host) + ";"
        },
        setCookie: function(t, e, n, r, i) {
            var o;
            i && (o = new Date).setTime(o.getTime() + 36e5 * i),
            document.cookie = t + "=" + e + "; " + (o ? "expires=" + o.toUTCString() + ";" : "") + "domain=" + (n || window.location.host) + ";path=" + (r || "/") + ";"
        },
        getACSRFToken: f,
        getGuid: function() {
            return l("qqmusic_guid") || ""
        }
    }), d = function() {
        return !!l("wxopenid")
    }, h = function() {
        var t = 0;
        return 0 === (t = (t = d() ? l("wxuin") : l("uin")) || l("p_uin")).indexOf("o") && (t = t.substring(1, t.length)),
        /^\d+$/.test(t) ? t.length < 14 && (t = parseInt(t, 10)) : t = 0,
        t
    }, v = Object.freeze({
        __proto__: null,
        getUin: h,
        isLogin: function() {
            return h() > 1e4
        },
        isWeiXin: d
    });
    if (c)
        if (u = 100 * (parseInt(l("qqmusic_version"), 10) || 0) + (parseInt(l("qqmusic_miniversion"), 10) || 0),
        -1 !== (a = window.navigator.userAgent).indexOf("Mac OS X")) {
            s = "mac";
            var m = (l("qqmusic_version_mac") || "0").split(".");
            u = 1e4 * (parseInt(m[0], 10) || 0) + 100 * (parseInt(m[1], 10) || 0) + (parseInt(m[2], 10) || 0)
        } else
            s = -1 !== a.indexOf("Edge") ? "uwp" : "pc";
    var g, y = {
        isBrowser: c,
        ua: a,
        version: u,
        client: s
    }, b = function(t) {
        return "[object Object]" === Object.prototype.toString.call(t)
    }, w = function(t) {
        return "string" === typeof t
    }, x = function(t) {
        return "number" === typeof t
    }, _ = function(t) {
        return b(t) && null !== t && t !== t.window && Object.getPrototypeOf(t) === Object.prototype
    }, E = "//y.qq.com/mediastyle/global/img/album_300.png?max_age=2592000", k = "//y.qq.com/mediastyle/global/img/singer_300.png?max_age=2592000", T = function(t) {
        for (var e, n = !1, r = arguments.length, i = new Array(r > 1 ? r - 1 : 0), o = 1; o < r; o++)
            i[o - 1] = arguments[o];
        "boolean" === typeof t ? (n = t,
        e = i.shift()) : e = t;
        var a = function t(e, n, r) {
            Object.keys(n).forEach((function(i) {
                var o = n[i];
                r && _(o) || Array.isArray(o) ? (_(o) && !_(e[i]) && (e[i] = {}),
                Array.isArray(n[i]) && !Array.isArray(e[i]) && (e[i] = []),
                t(e[i], n[i], r)) : void 0 !== o && (e[i] = o)
            }
            ))
        };
        return i.forEach((function(t) {
            a(e, t, n)
        }
        )),
        e
    }, S = function(t) {
        return function(t, e, n, r) {
            var i, o, a = {};
            if (!t || "string" !== typeof t)
                return a;
            "string" !== typeof e && (e = "&"),
            "string" !== typeof n && (n = ""),
            "string" !== typeof r && (r = "="),
            0 === t.indexOf("?") && (t = t.slice(1));
            var u = t.split(e);
            if (u && u.length)
                for (var s = 0, c = u.length; s < c; ++s)
                    (i = u[s].split(r)).length > 1 ? (o = i.slice(1).join(r).split(n),
                    a[i[0]] = o.slice(n.length, o.length - n.length).join(n)) : i[0] && (a[i[0]] = !0);
            return a
        }(t, "&")
    }, O = function(t, e) {
        var n;
        n = y.isBrowser ? e || window.location.href : e || "";
        var r = new RegExp("(\\?|&|#)" + t + "=(.*?)(#|&|$)","i")
          , i = n.match(r)
          , o = i ? i[2] : "";
        try {
            return decodeURIComponent(o)
        } catch (yn) {
            return o
        }
    }, C = function(t, e) {
        if (e = e || window.location.href,
        "object" !== typeof t && !t)
            return e;
        var n = t;
        return "object" === typeof t && (n = [],
        Object.keys(t).forEach((function(e) {
            n.push(encodeURIComponent(e) + "=" + encodeURIComponent(t[e]))
        }
        )),
        n = n.join("&")),
        e = /\?/.test(e) || /#/.test(e) ? /\?/.test(e) && !/#/.test(e) ? e + "&" + n : !/\?/.test(e) && /#/.test(e) ? e.replace("#", "?" + n + "#") : e.replace("?", "?" + n + "&") : e + "?" + n
    }, A = function(t) {
        var e = ("" + t).trim().match(/([^?#]*)(#.*)?$/);
        if (!e)
            return {};
        var n = e[0].split("&")
          , r = {};
        return n.forEach((function(t) {
            var e = t.split("=", 1)[0];
            if (e) {
                var n = decodeURIComponent(e)
                  , i = t.substring(n.length + 1);
                void 0 !== i && (i = decodeURIComponent(i)),
                n in r ? (r[n].constructor !== Array && (r[n] = [r[n]]),
                r[n].push(i)) : r[n] = i
            }
        }
        )),
        r
    }, P = function t(e) {
        var n = []
          , r = function(t, e) {
            n.push(encodeURIComponent(t) + "=" + encodeURIComponent(e))
        };
        return Object.keys(e).forEach((function(n) {
            var i = e[n];
            r(n, "object" === typeof i && i ? t(i) : i)
        }
        )),
        n.join("&").replace(/%20/g, "+")
    }, R = function(t) {
        return void 0 === t || null === t || "" === t || x(t) && isNaN(t)
    }, D = function(t) {
        return t.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\\/, "\uff3c").replace(/'/g, "\u2019").replace(/"/g, "\u201c").replace(/&#39;/g, "\u2019").replace(/&quot;/g, "\u201c").replace(/&acute;/g, "\u2019").replace(/%/g, "\uff05").replace(/\(/g, "\uff08").replace(/\)/g, "\uff09").replace(/\n/g, "")
    }, I = function(t) {
        return (t = "" + (t = t || "")) ? t.replace(/&#38;?/g, "&amp;").replace(/&amp;/g, "&").replace(/&#(\d+);?/g, (function(t, e) {
            return String.fromCharCode(e)
        }
        )).replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&nbsp;/g, " ").replace(/&#13;/g, "\n").replace(/(&#10;)|(&#x\w*;)/g, "").replace(/&amp;/g, "&") : ""
    }, j = function(t) {
        return {
            album: E,
            singer: k,
            mv: "//y.qq.com/mediastyle/global/img/mv_300.png?max_age=2592000",
            playlist: "//y.qq.com/mediastyle/global/img/playlist_300.png?max_age=2592000"
        }[t] || E
    }, N = Object.freeze({
        __proto__: null,
        getElementTop: function(t) {
            for (var e = t.offsetTop, n = t.offsetParent; null !== n; )
                e += n.offsetTop,
                n = n.offsetParent;
            return e
        },
        getElementLeft: function(t) {
            for (var e = t.offsetLeft, n = t.offsetParent; null !== n; )
                e += n.offsetLeft,
                n = n.offsetParent;
            return e
        },
        makePlayTime: function(t) {
            var e = Math.floor(t / 60)
              , n = parseInt((t % 60).toFixed(0), 10);
            return (e < 10 ? "0" + e : e) + ":" + (n < 10 ? "0" + n : n)
        },
        getEventPostion: function(t) {
            var e = (t.pageY || window.scrollY + t.clientY) + 35;
            return {
                left: (t.pageX || window.scrollX + t.clientX) + 20,
                top: e
            }
        },
        extend: T,
        isObject: b,
        albumDefaultImg: E,
        singerDefaultImg: k,
        formatComment: function(t) {
            return t.replace(/<br>/gi, "\n")
        },
        getDefaultImg: j,
        param: P,
        getParam: O,
        delParam: function(t, e) {
            var n = new RegExp("(\\?|#|&)(" + t + "=.*?)(#|&|$)")
              , r = (e = e || window.location.href).match(n);
            if (r && r.length >= 3 && r[2]) {
                var i = r[0]
                  , o = r[2];
                return "&" === i.charAt(0) && (o = "&" + o),
                e.replace(o, "")
            }
            return e
        },
        addParam: C,
        param2Obj: A,
        isPlainObject: _,
        isTrueEmpty: R,
        isEmpty: function(t) {
            return !!R(t) || (b(t) ? (Object.keys(t).forEach((function(t) {
                return !t && !0
            }
            )),
            !0) : Array.isArray(t) || w(t) ? 0 === t.length : x(t) ? 0 === t : "boolean" === typeof t && !t)
        },
        type: function(t) {
            return isNaN(t) ? "nan" : Object.prototype.toString.call(t).slice(8, -1).toLowerCase()
        },
        cloneObj: function t(e, n, r) {
            if ("object" === typeof e) {
                var i = Array.isArray(e) ? [] : {};
                return Object.keys(e).forEach((function(o) {
                    o !== n && (i[o] = r ? e[o] : t(e[o], n, r))
                }
                )),
                i
            }
            if ("function" === typeof e) {
                var o = e.toString();
                return r ? e : new Function(o.substring(o.indexOf("{") + 1, o.length - 1))
            }
            return e
        },
        getRealLen: function(t, e) {
            if ("string" !== typeof t)
                return 0;
            if (!e)
                return t.replace(/[^\x00-\xFF]/g, "**").length;
            var n = t.replace(/[\x00-\xFF]/g, "");
            return t.length - n.length + encodeURI(n).length / 3
        },
        unitFormat: function(t) {
            var e = {
                comm: {
                    cv: 1700,
                    ct: 20
                }
            };
            return e = Object.assign(e, t),
            JSON.stringify(e)
        },
        fixUrl: function(t) {
            if (t && "[object String]" === Object.prototype.toString.call(t)) {
                /^http(s?):\/\//i.test(t) && (t = t.replace(/^http(s?):/i, ""));
                var e = new RegExp("imgcache.qq.com|imgcache.gtimg.cn|y.gtimg.cn","g");
                t = t.replace(e, "y.qq.com"),
                /\.(jpg|png|gif|css|js)$/i.test(t) && (t += "?max_age=2592000")
            } else
                t = "//y.qq.com/mediastyle/global/img/banner.png";
            return t
        },
        getAlbumPic: function(t, e) {
            var n = E;
            return "string" === typeof t && t.length >= 14 && (n = "//y.qq.com/music/photo_new/T002R" + (e || 300) + "x" + (e || 300) + "M000" + t + ".jpg?max_age=2592000"),
            n
        },
        myEncode: D,
        entityReplace: I,
        stringEncode: function(t) {
            return D(I(t.replace(/\\n/g, "\uff3cn"))).replace(/\\n|\uff3cn/g, "<br>")
        },
        formatTime: function(t, e) {
            if ("Invalid Date" === t)
                return "0000-00-00 00:00:00";
            var n = (t = t ? new Date(t) : new Date).getFullYear()
              , r = t.getMonth() + 1
              , i = t.getDate()
              , o = t.getHours()
              , a = t.getMinutes();
            return 1 === e ? n + "-" + (r < 10 ? "0" + r : r) + "-" + (i < 10 ? "0" + i : i) + " " + (o < 10 ? "0" + o : o) + ":" + (a < 10 ? "0" + a : a) : "undefined" === typeof e ? (o < 10 ? "0" + o : o) + ":" + (a < 10 ? "0" + a : a) : void 0
        },
        getSingerPic: function(t, e) {
            var n = k;
            return "string" === typeof t && t.length >= 14 && (n = "//y.qq.com/music/photo_new/T001R" + (e || 68) + "x" + (e || 68) + "M000" + t + ".jpg?max_age=2592000"),
            n
        },
        getParams: function(t) {
            var e = {}
              , n = function(t) {
                var e = document.createElement("a");
                return e.href = t,
                e
            }(t = t || location.href);
            return e = Object.assign(e, S(n.hash.split("#")[1]), S(n.search.split("?")[1]))
        },
        jumpWithKey: function(t, e) {
            (t = (t || "").trim()).indexOf("http:") < 0 && t.indexOf("https:") < 0 && (t = location.protocol + t),
            e = e || "";
            var n = parseInt(l("qqmusic_uin"), 10) || 0
              , r = l("qqmusic_key");
            if (n < 1e4)
                window.open(t);
            else {
                var i = "https://ssl.ptlogin2.qq.com/jump?pgv_ref=" + e + "&keyindex=14&clientuin=" + n + "&clientkey=" + r + "&u1=" + encodeURIComponent(t);
                window.open(i)
            }
        },
        getVideoPicUrl: function(t) {
            return t ? "//puui.qpic.cn/qqvideo_ori/0/" + t + "_228_128/0" : j("mv")
        },
        formatDate: function(t) {
            var e = new Date
              , n = e.getFullYear()
              , r = e.getMonth() + 1
              , i = e.getDate();
            if ("Invalid Date" === t)
                return "";
            if ("number" === typeof t && t > 0) {
                var o = new Date(1e3 * t)
                  , a = o.getFullYear()
                  , u = o.getMonth() + 1
                  , s = o.getDate()
                  , c = o.getHours()
                  , l = o.getMinutes()
                  , f = "";
                return a !== n && (f += a + "\u5e74"),
                a === n && u === r && s === i || (f += u + "\u6708" + s + "\u65e5 "),
                f + (c < 10 ? "0" + c : c) + ":" + (l < 10 ? "0" + l : l)
            }
            return ""
        },
        isString: w,
        copyText: function(t, e) {
            if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
                var n = document.createElement("textarea");
                n.textContent = t,
                n.style.position = "fixed",
                document.body.appendChild(n),
                n.select();
                try {
                    document.execCommand("copy"),
                    e && e()
                } catch (r) {} finally {
                    document.body.removeChild(n)
                }
            }
        },
        getSongSinglePic: function(t, e) {
            var n = E;
            return "string" === typeof t && t.length >= 14 && (n = "//y.qq.com/music/photo_new/T062R" + (e || 300) + "x" + (e || 300) + "M000" + t + ".jpg?max_age=2592000"),
            n
        }
    });
    y.isBrowser && (g = document.createElement("a"));
    var L = {
        type: "GET",
        data: {},
        dataType: "json",
        beforeSend: null,
        success: null,
        error: null,
        complete: null,
        accepts: {
            script: "text/javascript, application/javascript, application/x-javascript",
            json: "application/json",
            xml: "application/xml, text/xml",
            html: "text/html",
            text: "text/plain"
        },
        crossDomain: !0,
        time: 0
    }
      , B = function(t) {
        var e = T(!0, {}, L, t)
          , r = e.dataType.toLowerCase();
        e.url = C({ _: Date.now() }, e.url);
        if ("GET" === e.type.toUpperCase()) {
            e.url = C(e.data, e.url);
            e.data = void 0;
        } else {
            if ("string" !== typeof e.data && !(e.data instanceof FormData)) {
                e.data = JSON.stringify(e.data);
            }
        }
        // if (e.needSign && -1 !== e.url.indexOf("cgi-bin/musicu.fcg") && y.isBrowser) {
        if (e.needSign && -1 !== e.url.indexOf("cgi-bin/musicu.fcg")) {
            e.url = e.url.replace("cgi-bin/musicu.fcg", "cgi-bin/musics.fcg");
        }
        if (-1 !== e.url.indexOf("cgi-bin/musics.fcg")) {
            var i, o = n(1).default;
            if ("GET" === e.type.toUpperCase()) {
                i = o(e.data.data);
            } else {
                i = o(e.data);
                return i
            }

            e.url = C({ sign: i }, e.url);
        }


        var a, u = L.accepts[r], s = {}, c = /^([\w-]+:)\/\//.test(e.url) ? RegExp.$1 : window.location.protocol, l = new XMLHttpRequest;
        if (s.Accept = u || "*/*",
        !e.crossDomain) {
            var f = document.createElement("a");
            f.href = e.url,
            e.crossDomain = g.protocol + "//" + g.host !== f.protocol + "//" + f.host,
            s["X-Requested-With"] = "XMLHttpRequest"
        }
        if (e.mimeType) {
            if ((u = e.mimeType).indexOf(",") > -1) {
                var p = u.split(",", 2);
                u = p[0]
            }
            l.overrideMimeType && l.overrideMimeType(u)
        }
        return (e.contentType || e.data && "GET" !== e.type.toUpperCase() && !(e.data instanceof FormData)) && (s["Content-Type"] = e.contentType || "application/x-www-form-urlencoded"),
        s = Object.assign(s, e.headers),
        new Promise((function(t, n) {
            l.onreadystatechange = function() {
                if (4 === l.readyState) {
                    clearTimeout(a);
                    var e = null
                      , r = null;
                    if (l.status >= 200 && l.status <= 300 || 304 === l.status || 0 === l.status && "file:" === c) {
                        var i = u || l.getResponseHeader("content-type");
                        r = l.responseText;
                        try {
                            /^(?:text|application)\/xml/i.test(i) ? r = l.responseXML : "application/json" === i && (r = /^\s*$/.test(r) ? null : JSON.parse(r))
                        } catch (ue) {
                            e = ue
                        }
                        e ? n({
                            error: e,
                            xhr: l
                        }) : t({
                            result: r,
                            xhr: l
                        })
                    } else
                        n({
                            error: e,
                            xhr: l
                        })
                }
            }
            ,
            e.beforeSend && !1 === e.beforeSend() ? l.abort() : (l.open(e.type, e.url, e.async || !0, e.username, e.password),
            e.withCredentials && (l.withCredentials = !0),
            Object.keys(s).forEach((function(t) {
                l.setRequestHeader(t, s[t])
            }
            )),
            e.time > 0 && (a = setTimeout((function() {
                l.abort()
            }
            ), e.time)),
            l.send(e.data || null))
        }
        ))
    };
    window.B = B;
    var F = function(t) {
        var e = new Image
          , n = function() {
            e.onload = null,
            e.onerror = null,
            e.onabort = null,
            e = null
        };
        setTimeout((function() {
            e.onload = n,
            e.onerror = n,
            e.onabort = n,
            e.src = t
        }
        ))
    }
      , q = function(t, e, n, r) {
        var i;
        t && (r && "function" === typeof navigator.sendBeacon ? navigator.sendBeacon(t, e ? P(e) : null) : (e && (t = C(e, t)),
        n ? F(t) : "function" === typeof (i = function() {
            F(t)
        }
        ) && ("complete" === document.readyState ? i() : window.addEventListener("load", i, !1))))
    }
      , U = parseInt(O("debug"), 10);
    y.isBrowser && (window.rtpid || (window.rtpid = 1),
    window.debug);
    var z, Q = [], V = {}, J = function(t) {
        return t && (t < 0 || t >= 400 && t <= 699)
    }, W = function(t) {
        if (t.cgi && void 0 !== t.code && !isNaN(t.time)) {
            var e = {
                pid: window.rtpid > 0 ? window.rtpid : 1,
                cgi: ("" + t.cgi).split("?")[0],
                code: t.code,
                time: t.time || 0,
                rate: 100
            };
            if (t.pid > 0 && (e.pid = t.pid),
            t.rate > 0 && (e.rate = t.rate),
            void 0 !== t.totaltime && (e.totaltime = t.totaltime),
            void 0 !== t.code_sh && (e.code_sh = t.code_sh),
            void 0 !== t.code_sz && (e.code_sz = t.code_sz),
            void 0 !== t.time_sh && (e.time_sh = t.time_sh),
            void 0 !== t.time_sz && (e.time_sz = t.time_sz),
            t.area && (e.area = t.area),
            (J(t.code) || J(t.code_sh) || J(t.time_sh)) && (e.rate = 1,
            t.one = !1),
            t.one) {
                if (V[e.cgi])
                    return;
                V[e.cgi] = 1
            }
            0 === e.rate || e.rate > 1 && Math.random() * e.rate > 0 || function t(e) {
                e && Q.push(e),
                z || ((e = Q.shift()) && q("//stat6.y.qq.com/ext/fcgi-bin/fcg_web_access_stat.fcg", e, !1, !0),
                z = setTimeout((function() {
                    z = void 0,
                    Q.length && t()
                }
                ), 100))
            }(e)
        }
    }, Y = {
        abort: -601,
        error: -602,
        parsererror: -603,
        timeout: -604
    }, $ = 0, G = {
        cv: 4747474,
        ct: 24,
        format: "json",
        inCharset: "utf-8",
        outCharset: "utf-8",
        notice: 0,
        platform: "yqq.json",
        needNewCode: 1
    }, H = function(t) {
        var e = {
            data: G,
            time: 1e4,
            withCredentials: !0,
            cache: !1
        };
        e.data.uin = h() || 0,
        e.data.g_tk_new_20200303 = f(!0),
        e.data.g_tk = f(),
        t.postType && (e.data = {
            comm: e.data
        }),
        t.data && "string" === typeof t.data && (t.data = A(t.data)),
        y.isBrowser && t.data instanceof FormData ? e.data = t.data : e.data = T(!0, {}, e.data, t.data),
        delete t.data;
        var n = Object.assign(e, t);
        return y.isBrowser ? "jsonp" === t.format ? function(t) {
            return new Promise((function(e, n) {
                $ += 1;
                var r = t.jsonpCallback || "jsonp" + $
                  , i = document.createElement("script")
                  , o = null
                  , a = null;
                window[r] = function() {
                    for (var t = arguments.length, e = new Array(t), n = 0; n < t; n++)
                        e[n] = arguments[n];
                    o = e
                }
                ,
                t.url = C(t.data, t.url),
                i.src = C("jsonpCallback=" + r, t.url);
                var u = function(t) {
                    clearTimeout(a),
                    i.parentNode.removeChild(i),
                    "error" !== t.type && o ? e(o[0]) : n(t),
                    o = null
                };
                i.onload = u,
                i.onerror = u,
                t.beforeSend && !1 === t.beforeSend() ? n(null) : (document.head.appendChild(i),
                t.timeout > 0 && (a = setTimeout((function() {
                    n(null)
                }
                ), t.time)))
            }
            ))
        }(n) : function(t) {
            var e = document.createElement("a");
            e.href = t.url || "";
            var n, r, i, o, a = {
                cgi: e.protocol + "//" + e.host + e.pathname,
                code: null,
                totaltime: null,
                time: null,
                area: null,
                time_sh: null,
                time_sz: null,
                code_sz: null,
                code_sh: null,
                rate: 1
            }, u = e.hostname, s = !1 !== t.reportCode, c = !1 !== t.retry && /^(?:sz|sh)?[cu]6?\.y\.qq\.com$/.test(e.hostname), l = !1, f = !1, p = function(e) {
                u = e + (/(c|c6).y/.test(u) ? "c6.y" : "u6.y") + ".qq.com";
                t.url = t.url.replace(/(?:sz|sh)?[cu]6?\.y\.qq\.com/, u)
            };
            return p(""),
            s && (n = Number(new Date),
            r = Number(new Date)),
            new Promise((function(e, d) {
                var h = function(t) {
                    var n = t.result
                      , r = t.xhr;
                    a.code = null !== n.code ? n.code : n.retcode,
                    !(c && a.code < 0) || l && f ? e(n) : o = !0,
                    m(r)
                }
                  , v = function(t) {
                    var e = t.error
                      , n = t.xhr;
                    n && n.status && 200 !== n.status ? a.code = -n.status : a.code = Y[e] || -500,
                    !c || l && f ? d(e) : o = !0,
                    m(n || {})
                };
                B(t).then(h).catch(v);
                var m = function(e) {
                    var c, d;
                    i = Number(new Date),
                    o && (/sh/.test(u) ? c = "sh" : /sz/.test(u) ? c = "sz" : e.getResponseHeader && (c = e.getResponseHeader("area")),
                    d = /^sh|sz$/.test(c) ? "sh" === c ? "sz" : "sh" : Math.random() < .5 ? "sh" : "sz",
                    "sh" !== c && "sh" !== d || (l = !0),
                    "sz" !== c && "sz" !== d || (f = !0),
                    a["time_" + c] = i - n,
                    a["code_" + c] = a.code,
                    p(d),
                    o = !1,
                    setTimeout((function() {
                        n = Number(new Date),
                        B(t).then(h).catch(v)
                    }
                    ))),
                    s && ((a = Object.assign(a, b(t.reportCode) && t.reportCode, b(e.reportCode) && e.reportCode)).time = i - n,
                    a.totaltime = i - r,
                    W(a))
                }
            }
            ))
        }(n) : function(t) {
            return new Promise((function(e, n) {
                var o = plug("ajax") || plug("qzone/ajax")
                  , a = plug("config")
                  , u = new URL(t.url).hostname
                  , s = {
                    url: t.url,
                    type: "GET",
                    dataType: "json",
                    l5api: null,
                    dcapi: null,
                    data: null,
                    headers: {
                        referer: "https://y.qq.com" + i.url
                    }
                };
                t.postType && (t.data = {
                    data: JSON.stringify(t.data)
                }),
                s.data = t.data,
                s.l5api = a.l5api[u] || null,
                s.dcapi = {
                    fromId: 205361524,
                    toId: 205364723,
                    interfaceId: 105103952
                },
                o.proxy(i, r).request(s).always((function(t) {
                    try {
                        var r = t.result;
                        e(r)
                    } catch (yn) {
                        n(t)
                    }
                }
                ))
            }
            ))
        }(n)
    }, X = {
        url: (y.isBrowser ? "" : "http:") + "//u.y.qq.com/cgi-bin/musicu.fcg",
        postType: !0,
        type: "POST",
        needSign: !0
    }, K = function(t) {
        var e = this;
        void 0 === t && (t = {
            data: null
        }),
        this.reqData = {},
        this.index = 0,
        this.initReq = function() {
            e.reqData = {},
            e.wait = null,
            e.index = 0
        }
        ,
        this.sendRequest = function() {
            return new Promise((function(t, n) {
                setTimeout((function() {
                    var r = T(!0, {}, e.options, {
                        data: e.reqData
                    });
                    return e.initReq(),
                    H(r).then((function(e) {
                        if (!e || 0 !== e.code)
                            return Promise.reject(e);
                        t(e)
                    }
                    )).catch((function(t) {
                        n(t)
                    }
                    ))
                }
                ))
            }
            ))
        }
        ,
        this.request = function(t) {
            var n = t instanceof Array ? t : [t];
            e.wait || (e.wait = e.sendRequest());
            var r = {};
            return n.forEach((function(t) {
                e.index += 1,
                t.param || (t.param = {}),
                r["req_" + e.index] = t
            }
            )),
            e.reqData = Object.assign(Object.assign({}, e.reqData), r),
            e.wait.then((function(t) {
                var e = Object.keys(r);
                return 0 === e.length ? [] : e.map((function(e) {
                    return t[e]
                }
                ))
            }
            ))
        }
        ,
        this.options = T({}, X, t)
    }, Z = new K, tt = function() {
        return Z
    }, et = function(t) {
        return new Promise((function(e, n) {
            var r = t.url
              , i = t.charset
              , o = t.isCors
              , a = /\.css(?:\?|#|$)/i.test(r)
              , u = document.createElement(a ? "link" : "script");
            i && (u.charset = i);
            var s = function(t) {
                u.onload = null,
                u.onerror = null,
                a || document.body.removeChild(u),
                u = null,
                "error" === t.type ? n() : e()
            };
            u.onload = s,
            u.onerror = s,
            a && u instanceof HTMLLinkElement ? (u.rel = "stylesheet",
            u.href = r) : u instanceof HTMLScriptElement ? (u.async = !0,
            u.src = r,
            o && (u.crossOrigin = "true")) : n(),
            document.body.appendChild(u)
        }
        ))
    }, nt = function(t, e, n, r) {
        var i = function(e) {
            n.call(t, e)
        };
        if (t.addEventListener) {
            var o = !1;
            return "object" === typeof r ? o = r.capture || !1 : "boolean" === typeof r && (o = r),
            t.addEventListener(e, i, r || !1),
            {
                remove: function() {
                    t.removeEventListener(e, i, o)
                }
            }
        }
        if (t.attachEvent)
            return t.attachEvent("on" + e, i),
            {
                remove: function() {
                    t.detachEvent("on" + e, i)
                }
            }
    };
    function rt(t, e) {
        for (var n = 0; n < e.length; n++) {
            var r = e[n];
            r.enumerable = r.enumerable || !1,
            r.configurable = !0,
            "value"in r && (r.writable = !0),
            Object.defineProperty(t, r.key, r)
        }
    }
    var it = function() {
        function t(t) {
            var e = this;
            if (this.changeStorageFn = function(t) {
                try {
                    var n = JSON.parse(t.oldValue) ? JSON.parse(t.oldValue).value : null
                      , r = JSON.parse(t.newValue) ? JSON.parse(t.newValue).value : null;
                    e.cb && e.cb({
                        key: t.key,
                        oldValue: n,
                        newValue: r
                    })
                } catch (yn) {
                    e.cb && e.cb({
                        key: t.key,
                        oldValue: null,
                        newValue: null
                    })
                }
            }
            ,
            this.enable = !1,
            this.storage = t,
            this.storage)
                try {
                    this.storage.setItem(name + "_support_test", "true"),
                    this.storage.removeItem(name + "_support_test"),
                    this.enable = !0
                } catch (yn) {
                    this.enable = !1
                }
        }
        var e, n, r, i = t.prototype;
        return i.has = function(t) {
            return !!this.enable && Object.prototype.hasOwnProperty.call(this.storage, t)
        }
        ,
        i.get = function(t) {
            if (!this.enable)
                return null;
            try {
                return this.storage.getItem(t) || null
            } catch (ue) {
                return null
            }
        }
        ,
        i.set = function(t, e) {
            if (!this.enable)
                return !1;
            try {
                return this.storage.setItem(t, e),
                !0
            } catch (yn) {
                return !1
            }
        }
        ,
        i.getJson = function(t) {
            var e = this.get(t);
            if (e)
                try {
                    var n = JSON.parse(e)
                      , r = n.value
                      , i = n.expire;
                    return i && ((new Date).getTime() > i && i) ? (this.remove(t),
                    null) : r || null
                } catch (yn) {
                    return null
                }
            return null
        }
        ,
        i.setJson = function(t, e, n) {
            if (!this.enable)
                return !1;
            var r = JSON.stringify({
                value: e,
                expire: n
            });
            return this.set(t, r)
        }
        ,
        i.remove = function(t) {
            if (!this.enable)
                return !1;
            try {
                return this.storage.removeItem(t),
                !0
            } catch (yn) {
                return !1
            }
        }
        ,
        i.changeStorage = function(t) {
            this.cb = t,
            window.addEventListener("storage", this.changeStorageFn, !1)
        }
        ,
        i.removeChangeStorage = function() {
            window.removeEventListener("storage", this.changeStorageFn, !1)
        }
        ,
        e = t,
        (n = [{
            key: "isEnable",
            get: function() {
                return this.enable
            }
        }]) && rt(e.prototype, n),
        r && rt(e, r),
        t
    }()
      , ot = new it(window.localStorage);
    new it(window.sessionStorage);
    function at(t) {
        return (at = "function" === typeof Symbol && "symbol" === typeof Symbol.iterator ? function(t) {
            return typeof t
        }
        : function(t) {
            return t && "function" === typeof Symbol && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t
        }
        )(t)
    }
    function ut(t, e) {
        if (!(t instanceof e))
            throw new TypeError("Cannot call a class as a function")
    }
    function st(t, e) {
        for (var n = 0; n < e.length; n++) {
            var r = e[n];
            r.enumerable = r.enumerable || !1,
            r.configurable = !0,
            "value"in r && (r.writable = !0),
            Object.defineProperty(t, r.key, r)
        }
    }
    function ct(t, e, n) {
        return e && st(t.prototype, e),
        n && st(t, n),
        t
    }
    function lt(t, e, n) {
        return e in t ? Object.defineProperty(t, e, {
            value: n,
            enumerable: !0,
            configurable: !0,
            writable: !0
        }) : t[e] = n,
        t
    }
    function ft(t, e) {
        var n = Object.keys(t);
        if (Object.getOwnPropertySymbols) {
            var r = Object.getOwnPropertySymbols(t);
            e && (r = r.filter((function(e) {
                return Object.getOwnPropertyDescriptor(t, e).enumerable
            }
            ))),
            n.push.apply(n, r)
        }
        return n
    }
    function pt(t) {
        for (var e = 1; e < arguments.length; e++) {
            var n = null != arguments[e] ? arguments[e] : {};
            e % 2 ? ft(Object(n), !0).forEach((function(e) {
                lt(t, e, n[e])
            }
            )) : Object.getOwnPropertyDescriptors ? Object.defineProperties(t, Object.getOwnPropertyDescriptors(n)) : ft(Object(n)).forEach((function(e) {
                Object.defineProperty(t, e, Object.getOwnPropertyDescriptor(n, e))
            }
            ))
        }
        return t
    }
    function dt(t, e) {
        return function(t) {
            if (Array.isArray(t))
                return t
        }(t) || function(t, e) {
            if ("undefined" === typeof Symbol || !(Symbol.iterator in Object(t)))
                return;
            var n = []
              , r = !0
              , i = !1
              , o = void 0;
            try {
                for (var a, u = t[Symbol.iterator](); !(r = (a = u.next()).done) && (n.push(a.value),
                !e || n.length !== e); r = !0)
                    ;
            } catch (s) {
                i = !0,
                o = s
            } finally {
                try {
                    r || null == u.return || u.return()
                } finally {
                    if (i)
                        throw o
                }
            }
            return n
        }(t, e) || vt(t, e) || function() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }()
    }
    function ht(t) {
        return function(t) {
            if (Array.isArray(t))
                return mt(t)
        }(t) || function(t) {
            if ("undefined" !== typeof Symbol && Symbol.iterator in Object(t))
                return Array.from(t)
        }(t) || vt(t) || function() {
            throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
        }()
    }
    function vt(t, e) {
        if (t) {
            if ("string" === typeof t)
                return mt(t, e);
            var n = Object.prototype.toString.call(t).slice(8, -1);
            return "Object" === n && t.constructor && (n = t.constructor.name),
            "Map" === n || "Set" === n ? Array.from(t) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? mt(t, e) : void 0
        }
    }
    function mt(t, e) {
        (null == e || e > t.length) && (e = t.length);
        for (var n = 0, r = new Array(e); n < e; n++)
            r[n] = t[n];
        return r
    }
    var gt = function() {
        function t() {
            ut(this, t),
            lt(this, "i", void 0),
            lt(this, "j", void 0),
            lt(this, "S", void 0),
            this.i = 0,
            this.j = 0,
            this.S = []
        }
        return ct(t, [{
            key: "init",
            value: function(t) {
                var e, n, r;
                for (e = 0; e < 256; ++e)
                    this.S[e] = e;
                for (n = 0,
                e = 0; e < 256; ++e)
                    n = n + this.S[e] + t[e % t.length] & 255,
                    r = this.S[e],
                    this.S[e] = this.S[n],
                    this.S[n] = r;
                this.i = 0,
                this.j = 0
            }
        }, {
            key: "next",
            value: function() {
                this.i = this.i + 1 & 255,
                this.j = this.j + this.S[this.i] & 255;
                var t = this.S[this.i];
                return this.S[this.i] = this.S[this.j],
                this.S[this.j] = t,
                this.S[t + this.S[this.i] & 255]
            }
        }]),
        t
    }();
    var yt, bt, wt = [], xt = 0;
    if (null !== (yt = window.crypto) && void 0 !== yt && yt.getRandomValues) {
        var _t, Et = new Uint32Array(256);
        for (window.crypto.getRandomValues(Et),
        _t = 0; _t < Et.length; ++_t)
            wt[xt++] = 255 & Et[_t]
    }
    function kt() {
        if (null === bt || void 0 === bt) {
            for (bt = new gt; xt < 256; ) {
                var t = Math.floor(65536 * Math.random());
                wt[xt++] = 255 & t
            }
            for (bt.init(wt),
            xt = 0; xt < wt.length; ++xt)
                wt[xt] = 0;
            xt = 0
        }
        return bt.next()
    }
    var Tt = function() {
        function t() {
            ut(this, t)
        }
        return ct(t, [{
            key: "nextBytes",
            value: function(t) {
                for (var e = 0; e < t.length; ++e)
                    t[e] = kt()
            }
        }]),
        t
    }()
      , St = /^(?:[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}|00000000-0000-0000-0000-000000000000)$/i;
    function Ot(t) {
        return "string" === typeof t && St.test(t)
    }
    for (var Ct = [], At = 0; At < 256; ++At)
        Ct.push((At + 256).toString(16).substr(1));
    function Pt() {
        var t = new Tt
          , e = new Array(16);
        return t.nextBytes(e),
        e[6] = 15 & e[6] | 64,
        e[8] = 63 & e[8] | 128,
        function(t) {
            var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : 0
              , n = "".concat(Ct[t[e + 0]] + Ct[t[e + 1]] + Ct[t[e + 2]] + Ct[t[e + 3]], "-").concat(Ct[t[e + 4]]).concat(Ct[t[e + 5]], "-").concat(Ct[t[e + 6]]).concat(Ct[t[e + 7]], "-").concat(Ct[t[e + 8]]).concat(Ct[t[e + 9]], "-").concat(Ct[t[e + 10]]).concat(Ct[t[e + 11]]).concat(Ct[t[e + 12]]).concat(Ct[t[e + 13]]).concat(Ct[t[e + 14]]).concat(Ct[t[e + 15]]).toLowerCase();
            if (!Ot(n))
                throw TypeError("Stringified UUID is invalid");
            return n
        }(e)
    }
    var Mt = function(t, e) {
        e = "string" === typeof e ? e : JSON.stringify(e);
        var n = new XMLHttpRequest;
        n.open("POST", t),
        n.send(e)
    }
      , Rt = window || {}
      , Dt = Rt.location
      , It = Rt.navigator
      , jt = (It || {}).userAgent;
    function Nt(t) {
        return "0123456789abcdefghijklmnopqrstuvwxyz".charAt(t)
    }
    function Lt(t, e) {
        return t & e
    }
    function Bt(t, e) {
        return t | e
    }
    function Ft(t, e) {
        return t ^ e
    }
    function qt(t, e) {
        return t & ~e
    }
    function Ut(t) {
        if (0 == t)
            return -1;
        var e = 0;
        return 0 == (65535 & t) && (t >>= 16,
        e += 16),
        0 == (255 & t) && (t >>= 8,
        e += 8),
        0 == (15 & t) && (t >>= 4,
        e += 4),
        0 == (3 & t) && (t >>= 2,
        e += 2),
        0 == (1 & t) && ++e,
        e
    }
    function zt(t) {
        for (var e = 0; 0 != t; )
            t &= t - 1,
            ++e;
        return e
    }
    var Qt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
      , Vt = (1 << 26) / Qt[Qt.length - 1]
      , Jt = function() {
        function t(e, n, r) {
            ut(this, t),
            lt(this, "s", void 0),
            lt(this, "t", void 0),
            lt(this, "DB", void 0),
            lt(this, "DM", void 0),
            lt(this, "DV", void 0),
            lt(this, "FV", void 0),
            lt(this, "F1", void 0),
            lt(this, "F2", void 0),
            lt(this, "am", void 0);
            var i = Zt
              , o = 28;
            It && "Microsoft Internet Explorer" == It.appName ? (i = Kt,
            o = 30) : It && "Netscape" != It.appName ? (i = Xt,
            o = 26) : (i = Zt,
            o = 28),
            this.am = i,
            this.DB = o,
            this.DM = (1 << o) - 1,
            this.DV = 1 << o;
            this.FV = Math.pow(2, 52),
            this.F1 = 52 - o,
            this.F2 = 2 * o - 52,
            null != e && ("number" === typeof e ? this.fromNumber(e, n, r) : null == n && "string" !== typeof e ? this.fromString(e, 256) : this.fromString(e, n))
        }
        return ct(t, [{
            key: "toString",
            value: function(t) {
                if (this.s < 0)
                    return "-".concat(this.negate().toString(t));
                var e;
                if (16 == t)
                    e = 4;
                else if (8 == t)
                    e = 3;
                else if (2 == t)
                    e = 1;
                else if (32 == t)
                    e = 5;
                else {
                    if (4 != t)
                        return this.toRadix(t);
                    e = 2
                }
                var n, r = (1 << e) - 1, i = !1, o = "", a = this.t, u = this.DB - a * this.DB % e;
                if (a-- > 0)
                    for (u < this.DB && (n = this[a] >> u) > 0 && (i = !0,
                    o = Nt(n)); a >= 0; )
                        u < e ? (n = (this[a] & (1 << u) - 1) << e - u,
                        n |= this[--a] >> (u += this.DB - e)) : (n = this[a] >> (u -= e) & r,
                        u <= 0 && (u += this.DB,
                        --a)),
                        n > 0 && (i = !0),
                        i && (o += Nt(n));
                return i ? o : "0"
            }
        }, {
            key: "negate",
            value: function() {
                var e = Ht();
                return t.ZERO.subTo(this, e),
                e
            }
        }, {
            key: "abs",
            value: function() {
                return this.s < 0 ? this.negate() : this
            }
        }, {
            key: "compareTo",
            value: function(t) {
                var e = this.s - t.s;
                if (0 != e)
                    return e;
                var n = this.t;
                if (0 != (e = n - t.t))
                    return this.s < 0 ? -e : e;
                for (; --n >= 0; )
                    if (0 != (e = this[n] - t[n]))
                        return e;
                return 0
            }
        }, {
            key: "bitLength",
            value: function() {
                return this.t <= 0 ? 0 : this.DB * (this.t - 1) + oe(this[this.t - 1] ^ this.s & this.DM)
            }
        }, {
            key: "mod",
            value: function(e) {
                var n = Ht();
                return this.abs().divRemTo(e, null, n),
                this.s < 0 && n.compareTo(t.ZERO) > 0 && e.subTo(n, n),
                n
            }
        }, {
            key: "modPowInt",
            value: function(t, e) {
                var n;
                return n = t < 256 || e.isEven() ? new Yt(e) : new $t(e),
                this.exp(t, n)
            }
        }, {
            key: "clone",
            value: function() {
                var t = Ht();
                return this.copyTo(t),
                t
            }
        }, {
            key: "intValue",
            value: function() {
                if (this.s < 0) {
                    if (1 == this.t)
                        return this[0] - this.DV;
                    if (0 == this.t)
                        return -1
                } else {
                    if (1 == this.t)
                        return this[0];
                    if (0 == this.t)
                        return 0
                }
                return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
            }
        }, {
            key: "byteValue",
            value: function() {
                return 0 == this.t ? this.s : this[0] << 24 >> 24
            }
        }, {
            key: "shortValue",
            value: function() {
                return 0 == this.t ? this.s : this[0] << 16 >> 16
            }
        }, {
            key: "signum",
            value: function() {
                return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
            }
        }, {
            key: "toByteArray",
            value: function() {
                var t = this.t
                  , e = [];
                e[0] = this.s;
                var n, r = this.DB - t * this.DB % 8, i = 0;
                if (t-- > 0)
                    for (r < this.DB && (n = this[t] >> r) != (this.s & this.DM) >> r && (e[i++] = n | this.s << this.DB - r); t >= 0; )
                        r < 8 ? (n = (this[t] & (1 << r) - 1) << 8 - r,
                        n |= this[--t] >> (r += this.DB - 8)) : (n = this[t] >> (r -= 8) & 255,
                        r <= 0 && (r += this.DB,
                        --t)),
                        0 != (128 & n) && (n |= -256),
                        0 == i && (128 & this.s) != (128 & n) && ++i,
                        (i > 0 || n != this.s) && (e[i++] = n);
                return e
            }
        }, {
            key: "equals",
            value: function(t) {
                return 0 == this.compareTo(t)
            }
        }, {
            key: "min",
            value: function(t) {
                return this.compareTo(t) < 0 ? this : t
            }
        }, {
            key: "max",
            value: function(t) {
                return this.compareTo(t) > 0 ? this : t
            }
        }, {
            key: "and",
            value: function(t) {
                var e = Ht();
                return this.bitwiseTo(t, Lt, e),
                e
            }
        }, {
            key: "or",
            value: function(t) {
                var e = Ht();
                return this.bitwiseTo(t, Bt, e),
                e
            }
        }, {
            key: "xor",
            value: function(t) {
                var e = Ht();
                return this.bitwiseTo(t, Ft, e),
                e
            }
        }, {
            key: "andNot",
            value: function(t) {
                var e = Ht();
                return this.bitwiseTo(t, qt, e),
                e
            }
        }, {
            key: "not",
            value: function() {
                for (var t = Ht(), e = 0; e < this.t; ++e)
                    t[e] = this.DM & ~this[e];
                return t.t = this.t,
                t.s = ~this.s,
                t
            }
        }, {
            key: "shiftLeft",
            value: function(t) {
                var e = Ht();
                return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
                e
            }
        }, {
            key: "shiftRight",
            value: function(t) {
                var e = Ht();
                return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
                e
            }
        }, {
            key: "getLowestSetBit",
            value: function() {
                for (var t = 0; t < this.t; ++t)
                    if (0 != this[t])
                        return t * this.DB + Ut(this[t]);
                return this.s < 0 ? this.t * this.DB : -1
            }
        }, {
            key: "bitCount",
            value: function() {
                for (var t = 0, e = this.s & this.DM, n = 0; n < this.t; ++n)
                    t += zt(this[n] ^ e);
                return t
            }
        }, {
            key: "testBit",
            value: function(t) {
                var e = Math.floor(t / this.DB);
                return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
            }
        }, {
            key: "setBit",
            value: function(t) {
                return this.changeBit(t, Bt)
            }
        }, {
            key: "clearBit",
            value: function(t) {
                return this.changeBit(t, qt)
            }
        }, {
            key: "flipBit",
            value: function(t) {
                return this.changeBit(t, Ft)
            }
        }, {
            key: "add",
            value: function(t) {
                var e = Ht();
                return this.addTo(t, e),
                e
            }
        }, {
            key: "subtract",
            value: function(t) {
                var e = Ht();
                return this.subTo(t, e),
                e
            }
        }, {
            key: "multiply",
            value: function(t) {
                var e = Ht();
                return this.multiplyTo(t, e),
                e
            }
        }, {
            key: "divide",
            value: function(t) {
                var e = Ht();
                return this.divRemTo(t, e, null),
                e
            }
        }, {
            key: "remainder",
            value: function(t) {
                var e = Ht();
                return this.divRemTo(t, null, e),
                e
            }
        }, {
            key: "divideAndRemainder",
            value: function(t) {
                var e = Ht()
                  , n = Ht();
                return this.divRemTo(t, e, n),
                [e, n]
            }
        }, {
            key: "modPow",
            value: function(t, e) {
                var n, r, i = t.bitLength(), o = ie(1);
                if (i <= 0)
                    return o;
                n = i < 18 ? 1 : i < 48 ? 3 : i < 144 ? 4 : i < 768 ? 5 : 6,
                r = i < 8 ? new Yt(e) : e.isEven() ? new Gt(e) : new $t(e);
                var a = []
                  , u = 3
                  , s = n - 1
                  , c = (1 << n) - 1;
                if (a[1] = r.convert(this),
                n > 1) {
                    var l = Ht();
                    for (r.sqrTo(a[1], l); u <= c; )
                        a[u] = Ht(),
                        r.mulTo(l, a[u - 2], a[u]),
                        u += 2
                }
                var f, p, d = t.t - 1, h = !0, v = Ht();
                for (i = oe(t[d]) - 1; d >= 0; ) {
                    for (i >= s ? f = t[d] >> i - s & c : (f = (t[d] & (1 << i + 1) - 1) << s - i,
                    d > 0 && (f |= t[d - 1] >> this.DB + i - s)),
                    u = n; 0 == (1 & f); )
                        f >>= 1,
                        --u;
                    if ((i -= u) < 0 && (i += this.DB,
                    --d),
                    h)
                        a[f].copyTo(o),
                        h = !1;
                    else {
                        for (; u > 1; )
                            r.sqrTo(o, v),
                            r.sqrTo(v, o),
                            u -= 2;
                        u > 0 ? r.sqrTo(o, v) : (p = o,
                        o = v,
                        v = p),
                        r.mulTo(v, a[f], o)
                    }
                    for (; d >= 0 && 0 == (t[d] & 1 << i); )
                        r.sqrTo(o, v),
                        p = o,
                        o = v,
                        v = p,
                        --i < 0 && (i = this.DB - 1,
                        --d)
                }
                return r.revert(o)
            }
        }, {
            key: "modInverse",
            value: function(e) {
                var n = e.isEven();
                if (this.isEven() && n || 0 == e.signum())
                    return t.ZERO;
                for (var r = e.clone(), i = this.clone(), o = ie(1), a = ie(0), u = ie(0), s = ie(1); 0 != r.signum(); ) {
                    for (; r.isEven(); )
                        r.rShiftTo(1, r),
                        n ? (o.isEven() && a.isEven() || (o.addTo(this, o),
                        a.subTo(e, a)),
                        o.rShiftTo(1, o)) : a.isEven() || a.subTo(e, a),
                        a.rShiftTo(1, a);
                    for (; i.isEven(); )
                        i.rShiftTo(1, i),
                        n ? (u.isEven() && s.isEven() || (u.addTo(this, u),
                        s.subTo(e, s)),
                        u.rShiftTo(1, u)) : s.isEven() || s.subTo(e, s),
                        s.rShiftTo(1, s);
                    r.compareTo(i) >= 0 ? (r.subTo(i, r),
                    n && o.subTo(u, o),
                    a.subTo(s, a)) : (i.subTo(r, i),
                    n && u.subTo(o, u),
                    s.subTo(a, s))
                }
                return 0 != i.compareTo(t.ONE) ? t.ZERO : s.compareTo(e) >= 0 ? s.subtract(e) : s.signum() < 0 ? (s.addTo(e, s),
                s.signum() < 0 ? s.add(e) : s) : s
            }
        }, {
            key: "pow",
            value: function(t) {
                return this.exp(t, new Wt)
            }
        }, {
            key: "gcd",
            value: function(t) {
                var e = this.s < 0 ? this.negate() : this.clone()
                  , n = t.s < 0 ? t.negate() : t.clone();
                if (e.compareTo(n) < 0) {
                    var r = e;
                    e = n,
                    n = r
                }
                var i = e.getLowestSetBit()
                  , o = n.getLowestSetBit();
                if (o < 0)
                    return e;
                for (i < o && (o = i),
                o > 0 && (e.rShiftTo(o, e),
                n.rShiftTo(o, n)); e.signum() > 0; )
                    (i = e.getLowestSetBit()) > 0 && e.rShiftTo(i, e),
                    (i = n.getLowestSetBit()) > 0 && n.rShiftTo(i, n),
                    e.compareTo(n) >= 0 ? (e.subTo(n, e),
                    e.rShiftTo(1, e)) : (n.subTo(e, n),
                    n.rShiftTo(1, n));
                return o > 0 && n.lShiftTo(o, n),
                n
            }
        }, {
            key: "isProbablePrime",
            value: function(t) {
                var e, n = this.abs();
                if (1 == n.t && n[0] <= Qt[Qt.length - 1]) {
                    for (e = 0; e < Qt.length; ++e)
                        if (n[0] == Qt[e])
                            return !0;
                    return !1
                }
                if (n.isEven())
                    return !1;
                for (e = 1; e < Qt.length; ) {
                    for (var r = Qt[e], i = e + 1; i < Qt.length && r < Vt; )
                        r *= Qt[i++];
                    for (r = n.modInt(r); e < i; )
                        if (r % Qt[e++] == 0)
                            return !1
                }
                return n.millerRabin(t)
            }
        }, {
            key: "copyTo",
            value: function(t) {
                for (var e = this.t - 1; e >= 0; --e)
                    t[e] = this[e];
                t.t = this.t,
                t.s = this.s
            }
        }, {
            key: "fromInt",
            value: function(t) {
                this.t = 1,
                this.s = t < 0 ? -1 : 0,
                t > 0 ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
            }
        }, {
            key: "fromString",
            value: function(e, n) {
                var r;
                if (16 == n)
                    r = 4;
                else if (8 == n)
                    r = 3;
                else if (256 == n)
                    r = 8;
                else if (2 == n)
                    r = 1;
                else if (32 == n)
                    r = 5;
                else {
                    if (4 != n)
                        return void this.fromRadix(e, n);
                    r = 2
                }
                this.t = 0,
                this.s = 0;
                for (var i = e.length, o = !1, a = 0; --i >= 0; ) {
                    var u = 8 == r ? 255 & +e[i] : re(e, i);
                    u < 0 ? "-" == e.charAt(i) && (o = !0) : (o = !1,
                    0 == a ? this[this.t++] = u : a + r > this.DB ? (this[this.t - 1] |= (u & (1 << this.DB - a) - 1) << a,
                    this[this.t++] = u >> this.DB - a) : this[this.t - 1] |= u << a,
                    (a += r) >= this.DB && (a -= this.DB))
                }
                8 == r && 0 != (128 & +e[0]) && (this.s = -1,
                a > 0 && (this[this.t - 1] |= (1 << this.DB - a) - 1 << a)),
                this.clamp(),
                o && t.ZERO.subTo(this, this)
            }
        }, {
            key: "clamp",
            value: function() {
                for (var t = this.s & this.DM; this.t > 0 && this[this.t - 1] == t; )
                    --this.t
            }
        }, {
            key: "dlShiftTo",
            value: function(t, e) {
                var n;
                for (n = this.t - 1; n >= 0; --n)
                    e[n + t] = this[n];
                for (n = t - 1; n >= 0; --n)
                    e[n] = 0;
                e.t = this.t + t,
                e.s = this.s
            }
        }, {
            key: "drShiftTo",
            value: function(t, e) {
                for (var n = t; n < this.t; ++n)
                    e[n - t] = this[n];
                e.t = Math.max(this.t - t, 0),
                e.s = this.s
            }
        }, {
            key: "lShiftTo",
            value: function(t, e) {
                for (var n = t % this.DB, r = this.DB - n, i = (1 << r) - 1, o = Math.floor(t / this.DB), a = this.s << n & this.DM, u = this.t - 1; u >= 0; --u)
                    e[u + o + 1] = this[u] >> r | a,
                    a = (this[u] & i) << n;
                for (var s = o - 1; s >= 0; --s)
                    e[s] = 0;
                e[o] = a,
                e.t = this.t + o + 1,
                e.s = this.s,
                e.clamp()
            }
        }, {
            key: "rShiftTo",
            value: function(t, e) {
                e.s = this.s;
                var n = Math.floor(t / this.DB);
                if (n >= this.t)
                    e.t = 0;
                else {
                    var r = t % this.DB
                      , i = this.DB - r
                      , o = (1 << r) - 1;
                    e[0] = this[n] >> r;
                    for (var a = n + 1; a < this.t; ++a)
                        e[a - n - 1] |= (this[a] & o) << i,
                        e[a - n] = this[a] >> r;
                    r > 0 && (e[this.t - n - 1] |= (this.s & o) << i),
                    e.t = this.t - n,
                    e.clamp()
                }
            }
        }, {
            key: "subTo",
            value: function(t, e) {
                for (var n = 0, r = 0, i = Math.min(t.t, this.t); n < i; )
                    r += this[n] - t[n],
                    e[n++] = r & this.DM,
                    r >>= this.DB;
                if (t.t < this.t) {
                    for (r -= t.s; n < this.t; )
                        r += this[n],
                        e[n++] = r & this.DM,
                        r >>= this.DB;
                    r += this.s
                } else {
                    for (r += this.s; n < t.t; )
                        r -= t[n],
                        e[n++] = r & this.DM,
                        r >>= this.DB;
                    r -= t.s
                }
                e.s = r < 0 ? -1 : 0,
                r < -1 ? e[n++] = this.DV + r : r > 0 && (e[n++] = r),
                e.t = n,
                e.clamp()
            }
        }, {
            key: "multiplyTo",
            value: function(e, n) {
                var r = this.abs()
                  , i = e.abs()
                  , o = r.t;
                for (n.t = o + i.t; --o >= 0; )
                    n[o] = 0;
                for (o = 0; o < i.t; ++o)
                    n[o + r.t] = r.am(0, i[o], n, o, 0, r.t);
                n.s = 0,
                n.clamp(),
                this.s != e.s && t.ZERO.subTo(n, n)
            }
        }, {
            key: "squareTo",
            value: function(t) {
                var e = this.abs();
                t.t = 2 * e.t;
                for (var n = t.t; --n >= 0; )
                    t[n] = 0;
                for (n = 0; n < e.t - 1; ++n) {
                    var r = e.am(n, e[n], t, 2 * n, 0, 1);
                    (t[n + e.t] += e.am(n + 1, 2 * e[n], t, 2 * n + 1, r, e.t - n - 1)) >= e.DV && (t[n + e.t] -= e.DV,
                    t[n + e.t + 1] = 1)
                }
                t.t > 0 && (t[t.t - 1] += e.am(n, e[n], t, 2 * n, 0, 1)),
                t.s = 0,
                t.clamp()
            }
        }, {
            key: "divRemTo",
            value: function(e, n, r) {
                var i = e.abs();
                if (!(i.t <= 0)) {
                    var o = this.abs();
                    if (o.t < i.t)
                        return null != n && n.fromInt(0),
                        void (null != r && this.copyTo(r));
                    null == r && (r = Ht());
                    var a = Ht()
                      , u = this.s
                      , s = e.s
                      , c = this.DB - oe(i[i.t - 1]);
                    c > 0 ? (i.lShiftTo(c, a),
                    o.lShiftTo(c, r)) : (i.copyTo(a),
                    o.copyTo(r));
                    var l = a.t
                      , f = a[l - 1];
                    if (0 != f) {
                        var p = f * (1 << this.F1) + (l > 1 ? a[l - 2] >> this.F2 : 0)
                          , d = this.FV / p
                          , h = (1 << this.F1) / p
                          , v = 1 << this.F2
                          , m = r.t
                          , g = m - l
                          , y = null == n ? Ht() : n;
                        for (a.dlShiftTo(g, y),
                        r.compareTo(y) >= 0 && (r[r.t++] = 1,
                        r.subTo(y, r)),
                        t.ONE.dlShiftTo(l, y),
                        y.subTo(a, a); a.t < l; )
                            a[a.t++] = 0;
                        for (; --g >= 0; ) {
                            var b = r[--m] == f ? this.DM : Math.floor(r[m] * d + (r[m - 1] + v) * h);
                            if ((r[m] += a.am(0, b, r, g, 0, l)) < b)
                                for (a.dlShiftTo(g, y),
                                r.subTo(y, r); r[m] < --b; )
                                    r.subTo(y, r)
                        }
                        null != n && (r.drShiftTo(l, n),
                        u != s && t.ZERO.subTo(n, n)),
                        r.t = l,
                        r.clamp(),
                        c > 0 && r.rShiftTo(c, r),
                        u < 0 && t.ZERO.subTo(r, r)
                    }
                }
            }
        }, {
            key: "invDigit",
            value: function() {
                if (this.t < 1)
                    return 0;
                var t = this[0];
                if (0 == (1 & t))
                    return 0;
                var e = 3 & t;
                return (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) > 0 ? this.DV - e : -e
            }
        }, {
            key: "isEven",
            value: function() {
                return 0 == (this.t > 0 ? 1 & this[0] : this.s)
            }
        }, {
            key: "exp",
            value: function(e, n) {
                if (e > 4294967295 || e < 1)
                    return t.ONE;
                var r = Ht()
                  , i = Ht()
                  , o = n.convert(this)
                  , a = oe(e) - 1;
                for (o.copyTo(r); --a >= 0; )
                    if (n.sqrTo(r, i),
                    (e & 1 << a) > 0)
                        n.mulTo(i, o, r);
                    else {
                        var u = r;
                        r = i,
                        i = u
                    }
                return n.revert(r)
            }
        }, {
            key: "chunkSize",
            value: function(t) {
                return Math.floor(Math.LN2 * this.DB / Math.log(t))
            }
        }, {
            key: "toRadix",
            value: function(t) {
                if (null == t && (t = 10),
                0 == this.signum() || t < 2 || t > 36)
                    return "0";
                var e = this.chunkSize(t)
                  , n = Math.pow(t, e)
                  , r = ie(n)
                  , i = Ht()
                  , o = Ht()
                  , a = "";
                for (this.divRemTo(r, i, o); i.signum() > 0; )
                    a = (n + o.intValue()).toString(t).substr(1) + a,
                    i.divRemTo(r, i, o);
                return o.intValue().toString(t) + a
            }
        }, {
            key: "fromRadix",
            value: function(e, n) {
                this.fromInt(0),
                null == n && (n = 10);
                for (var r = this.chunkSize(n), i = Math.pow(n, r), o = !1, a = 0, u = 0, s = 0; s < e.length; ++s) {
                    var c = re(e, s);
                    c < 0 ? "-" == e.charAt(s) && 0 == this.signum() && (o = !0) : (u = n * u + c,
                    ++a >= r && (this.dMultiply(i),
                    this.dAddOffset(u, 0),
                    a = 0,
                    u = 0))
                }
                a > 0 && (this.dMultiply(Math.pow(n, a)),
                this.dAddOffset(u, 0)),
                o && t.ZERO.subTo(this, this)
            }
        }, {
            key: "fromNumber",
            value: function(e, n, r) {
                if ("number" === typeof n)
                    if (e < 2)
                        this.fromInt(1);
                    else
                        for (this.fromNumber(e, r),
                        this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), Bt, this),
                        this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(n); )
                            this.dAddOffset(2, 0),
                            this.bitLength() > e && this.subTo(t.ONE.shiftLeft(e - 1), this);
                else {
                    var i = []
                      , o = 7 & e;
                    i.length = 1 + (e >> 3),
                    n.nextBytes(i),
                    o > 0 ? i[0] &= (1 << o) - 1 : i[0] = 0,
                    this.fromString(i, 256)
                }
            }
        }, {
            key: "bitwiseTo",
            value: function(t, e, n) {
                var r, i, o = Math.min(t.t, this.t);
                for (r = 0; r < o; ++r)
                    n[r] = e(this[r], t[r]);
                if (t.t < this.t) {
                    for (i = t.s & this.DM,
                    r = o; r < this.t; ++r)
                        n[r] = e(this[r], i);
                    n.t = this.t
                } else {
                    for (i = this.s & this.DM,
                    r = o; r < t.t; ++r)
                        n[r] = e(i, t[r]);
                    n.t = t.t
                }
                n.s = e(this.s, t.s),
                n.clamp()
            }
        }, {
            key: "changeBit",
            value: function(e, n) {
                var r = t.ONE.shiftLeft(e);
                return this.bitwiseTo(r, n, r),
                r
            }
        }, {
            key: "addTo",
            value: function(t, e) {
                for (var n = 0, r = 0, i = Math.min(t.t, this.t); n < i; )
                    r += this[n] + t[n],
                    e[n++] = r & this.DM,
                    r >>= this.DB;
                if (t.t < this.t) {
                    for (r += t.s; n < this.t; )
                        r += this[n],
                        e[n++] = r & this.DM,
                        r >>= this.DB;
                    r += this.s
                } else {
                    for (r += this.s; n < t.t; )
                        r += t[n],
                        e[n++] = r & this.DM,
                        r >>= this.DB;
                    r += t.s
                }
                e.s = r < 0 ? -1 : 0,
                r > 0 ? e[n++] = r : r < -1 && (e[n++] = this.DV + r),
                e.t = n,
                e.clamp()
            }
        }, {
            key: "dMultiply",
            value: function(t) {
                this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
                ++this.t,
                this.clamp()
            }
        }, {
            key: "dAddOffset",
            value: function(t, e) {
                if (0 != t) {
                    for (; this.t <= e; )
                        this[this.t++] = 0;
                    for (this[e] += t; this[e] >= this.DV; )
                        this[e] -= this.DV,
                        ++e >= this.t && (this[this.t++] = 0),
                        ++this[e]
                }
            }
        }, {
            key: "multiplyLowerTo",
            value: function(t, e, n) {
                var r = Math.min(this.t + t.t, e);
                for (n.s = 0,
                n.t = r; r > 0; )
                    n[--r] = 0;
                for (var i = n.t - this.t; r < i; ++r)
                    n[r + this.t] = this.am(0, t[r], n, r, 0, this.t);
                for (var o = Math.min(t.t, e); r < o; ++r)
                    this.am(0, t[r], n, r, 0, e - r);
                n.clamp()
            }
        }, {
            key: "multiplyUpperTo",
            value: function(t, e, n) {
                --e,
                n.t = this.t + t.t - e;
                var r = n.t;
                for (n.s = 0; --r >= 0; )
                    n[r] = 0;
                for (r = Math.max(e - this.t, 0); r < t.t; ++r)
                    n[this.t + r - e] = this.am(e - r, t[r], n, 0, 0, this.t + r - e);
                n.clamp(),
                n.drShiftTo(1, n)
            }
        }, {
            key: "modInt",
            value: function(t) {
                if (t <= 0)
                    return 0;
                var e = this.DV % t
                  , n = this.s < 0 ? t - 1 : 0;
                if (this.t > 0)
                    if (0 == e)
                        n = this[0] % t;
                    else
                        for (var r = this.t - 1; r >= 0; --r)
                            n = (e * n + this[r]) % t;
                return n
            }
        }, {
            key: "millerRabin",
            value: function(e) {
                var n = this.subtract(t.ONE)
                  , r = n.getLowestSetBit();
                if (r <= 0)
                    return !1;
                var i = n.shiftRight(r);
                (e = e + 1 >> 1) > Qt.length && (e = Qt.length);
                for (var o = Ht(), a = 0; a < e; ++a) {
                    o.fromInt(Qt[Math.floor(Math.random() * Qt.length)]);
                    var u = o.modPow(i, this);
                    if (0 != u.compareTo(t.ONE) && 0 != u.compareTo(n)) {
                        for (var s = 1; s++ < r && 0 != u.compareTo(n); )
                            if (0 == (u = u.modPowInt(2, this)).compareTo(t.ONE))
                                return !1;
                        if (0 != u.compareTo(n))
                            return !1
                    }
                }
                return !0
            }
        }, {
            key: "square",
            value: function() {
                var t = Ht();
                return this.squareTo(t),
                t
            }
        }, {
            key: "gcda",
            value: function(t, e) {
                var n = this.s < 0 ? this.negate() : this.clone()
                  , r = t.s < 0 ? t.negate() : t.clone();
                if (n.compareTo(r) < 0) {
                    var i = n;
                    n = r,
                    r = i
                }
                var o = n.getLowestSetBit()
                  , a = r.getLowestSetBit();
                if (a < 0)
                    e(n);
                else {
                    o < a && (a = o),
                    a > 0 && (n.rShiftTo(a, n),
                    r.rShiftTo(a, r));
                    setTimeout((function t() {
                        (o = n.getLowestSetBit()) > 0 && n.rShiftTo(o, n),
                        (o = r.getLowestSetBit()) > 0 && r.rShiftTo(o, r),
                        n.compareTo(r) >= 0 ? (n.subTo(r, n),
                        n.rShiftTo(1, n)) : (r.subTo(n, r),
                        r.rShiftTo(1, r)),
                        n.signum() > 0 ? setTimeout(t, 0) : (a > 0 && r.lShiftTo(a, r),
                        setTimeout((function() {
                            e(r)
                        }
                        ), 0))
                    }
                    ), 10)
                }
            }
        }, {
            key: "fromNumberAsync",
            value: function(e, n, r, i) {
                if ("number" === typeof n)
                    if (e < 2)
                        this.fromInt(1);
                    else {
                        this.fromNumber(e, r),
                        this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), Bt, this),
                        this.isEven() && this.dAddOffset(1, 0);
                        var o = this;
                        setTimeout((function r() {
                            o.dAddOffset(2, 0),
                            o.bitLength() > e && o.subTo(t.ONE.shiftLeft(e - 1), o),
                            o.isProbablePrime(n) ? setTimeout((function() {
                                i()
                            }
                            ), 0) : setTimeout(r, 0)
                        }
                        ), 0)
                    }
                else {
                    var a = []
                      , u = 7 & e;
                    a.length = 1 + (e >> 3),
                    n.nextBytes(a),
                    u > 0 ? a[0] &= (1 << u) - 1 : a[0] = 0,
                    this.fromString(a, 256)
                }
            }
        }]),
        t
    }();
    lt(Jt, "ONE", void 0),
    lt(Jt, "ZERO", void 0);
    var Wt = function() {
        function t() {
            ut(this, t)
        }
        return ct(t, [{
            key: "convert",
            value: function(t) {
                return t
            }
        }, {
            key: "revert",
            value: function(t) {
                return t
            }
        }, {
            key: "mulTo",
            value: function(t, e, n) {
                t.multiplyTo(e, n)
            }
        }, {
            key: "sqrTo",
            value: function(t, e) {
                t.squareTo(e)
            }
        }]),
        t
    }()
      , Yt = function() {
        function t(e) {
            ut(this, t),
            this.m = e
        }
        return ct(t, [{
            key: "convert",
            value: function(t) {
                return t.s < 0 || t.compareTo(this.m) >= 0 ? t.mod(this.m) : t
            }
        }, {
            key: "revert",
            value: function(t) {
                return t
            }
        }, {
            key: "reduce",
            value: function(t) {
                t.divRemTo(this.m, null, t)
            }
        }, {
            key: "mulTo",
            value: function(t, e, n) {
                t.multiplyTo(e, n),
                this.reduce(n)
            }
        }, {
            key: "sqrTo",
            value: function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
        }]),
        t
    }()
      , $t = function() {
        function t(e) {
            ut(this, t),
            this.m = e,
            lt(this, "mp", void 0),
            lt(this, "mpl", void 0),
            lt(this, "mph", void 0),
            lt(this, "um", void 0),
            lt(this, "mt2", void 0),
            this.mp = e.invDigit(),
            this.mpl = 32767 & this.mp,
            this.mph = this.mp >> 15,
            this.um = (1 << e.DB - 15) - 1,
            this.mt2 = 2 * e.t
        }
        return ct(t, [{
            key: "convert",
            value: function(t) {
                var e = Ht();
                return t.abs().dlShiftTo(this.m.t, e),
                e.divRemTo(this.m, null, e),
                t.s < 0 && e.compareTo(Jt.ZERO) > 0 && this.m.subTo(e, e),
                e
            }
        }, {
            key: "revert",
            value: function(t) {
                var e = Ht();
                return t.copyTo(e),
                this.reduce(e),
                e
            }
        }, {
            key: "reduce",
            value: function(t) {
                for (; t.t <= this.mt2; )
                    t[t.t++] = 0;
                for (var e = 0; e < this.m.t; ++e) {
                    var n = 32767 & t[e]
                      , r = n * this.mpl + ((n * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
                    for (t[n = e + this.m.t] += this.m.am(0, r, t, e, 0, this.m.t); t[n] >= t.DV; )
                        t[n] -= t.DV,
                        t[++n]++
                }
                t.clamp(),
                t.drShiftTo(this.m.t, t),
                t.compareTo(this.m) >= 0 && t.subTo(this.m, t)
            }
        }, {
            key: "mulTo",
            value: function(t, e, n) {
                t.multiplyTo(e, n),
                this.reduce(n)
            }
        }, {
            key: "sqrTo",
            value: function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
        }]),
        t
    }()
      , Gt = function() {
        function t(e) {
            ut(this, t),
            this.m = e,
            lt(this, "r2", void 0),
            lt(this, "q3", void 0),
            lt(this, "mu", void 0),
            this.r2 = Ht(),
            this.q3 = Ht(),
            Jt.ONE.dlShiftTo(2 * e.t, this.r2),
            this.mu = this.r2.divide(e)
        }
        return ct(t, [{
            key: "convert",
            value: function(t) {
                if (t.s < 0 || t.t > 2 * this.m.t)
                    return t.mod(this.m);
                if (t.compareTo(this.m) < 0)
                    return t;
                var e = Ht();
                return t.copyTo(e),
                this.reduce(e),
                e
            }
        }, {
            key: "revert",
            value: function(t) {
                return t
            }
        }, {
            key: "reduce",
            value: function(t) {
                for (t.drShiftTo(this.m.t - 1, this.r2),
                t.t > this.m.t + 1 && (t.t = this.m.t + 1,
                t.clamp()),
                this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
                this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); t.compareTo(this.r2) < 0; )
                    t.dAddOffset(1, this.m.t + 1);
                for (t.subTo(this.r2, t); t.compareTo(this.m) >= 0; )
                    t.subTo(this.m, t)
            }
        }, {
            key: "mulTo",
            value: function(t, e, n) {
                t.multiplyTo(e, n),
                this.reduce(n)
            }
        }, {
            key: "sqrTo",
            value: function(t, e) {
                t.squareTo(e),
                this.reduce(e)
            }
        }]),
        t
    }();
    function Ht() {
        return new Jt(null)
    }
    function Xt(t, e, n, r, i, o) {
        for (; --o >= 0; ) {
            var a = e * this[t++] + n[r] + i;
            i = Math.floor(a / 67108864),
            n[r++] = 67108863 & a
        }
        return i
    }
    function Kt(t, e, n, r, i, o) {
        for (var a = 32767 & e, u = e >> 15; --o >= 0; ) {
            var s = 32767 & this[t]
              , c = this[t++] >> 15
              , l = u * s + c * a;
            i = ((s = a * s + ((32767 & l) << 15) + n[r] + (1073741823 & i)) >>> 30) + (l >>> 15) + u * c + (i >>> 30),
            n[r++] = 1073741823 & s
        }
        return i
    }
    function Zt(t, e, n, r, i, o) {
        for (var a = 16383 & e, u = e >> 14; --o >= 0; ) {
            var s = 16383 & this[t]
              , c = this[t++] >> 14
              , l = u * s + c * a;
            i = ((s = a * s + ((16383 & l) << 14) + n[r] + i) >> 28) + (l >> 14) + u * c,
            n[r++] = 268435455 & s
        }
        return i
    }
    var te, ee, ne = [];
    for (te = "0".charCodeAt(0),
    ee = 0; ee <= 9; ++ee)
        ne[te++] = ee;
    for (te = "a".charCodeAt(0),
    ee = 10; ee < 36; ++ee)
        ne[te++] = ee;
    for (te = "A".charCodeAt(0),
    ee = 10; ee < 36; ++ee)
        ne[te++] = ee;
    function re(t, e) {
        var n = ne[t.charCodeAt(e)];
        return null == n ? -1 : n
    }
    function ie(t) {
        var e = Ht();
        return e.fromInt(t),
        e
    }
    function oe(t) {
        var e, n = 1;
        return 0 != (e = t >>> 16) && (t = e,
        n += 16),
        0 != (e = t >> 8) && (t = e,
        n += 8),
        0 != (e = t >> 4) && (t = e,
        n += 4),
        0 != (e = t >> 2) && (t = e,
        n += 2),
        0 != (e = t >> 1) && (t = e,
        n += 1),
        n
    }
    Jt.ZERO = ie(0),
    Jt.ONE = ie(1);
    var ae = new Jt("00D950477671A500894A74F50F029A2B17643EBECBC75BF44203D153419C2287CA40E8AD6EABD738FCBF479B437E5EFEE7788868C5636637F1A61AAED4BB849BE70863E4649046CD16479F5F0B3D2E9AEA9655AE0164031546D5160ACE3647DD3017205DBFA6ABABFD5AB364F513BCB9C43289E752801852363E383ECF355C64D3",16)
      , ue = parseInt("010001", 16)
      , se = ae.bitLength() + 7 >> 3;
    var ce = function(t) {
        var e = function(t, e) {
            if (e < t.length + 11)
                return null;
            for (var n = [], r = t.length - 1; r >= 0 && e > 0; ) {
                var i = t.charCodeAt(r--);
                i < 128 ? n[--e] = i : i > 127 && i < 2048 ? (n[--e] = 63 & i | 128,
                n[--e] = i >> 6 | 192) : (n[--e] = 63 & i | 128,
                n[--e] = i >> 6 & 63 | 128,
                n[--e] = i >> 12 | 224)
            }
            n[--e] = 0;
            for (var o = new Tt, a = []; e > 2; ) {
                for (a[0] = 0; 0 == a[0]; )
                    o.nextBytes(a);
                n[--e] = a[0]
            }
            return n[--e] = 2,
            n[--e] = 0,
            new Jt(n)
        }(t, se);
        if (null == e)
            return null;
        var n = e.modPowInt(ue, ae);
        if (null == n)
            return null;
        for (var r = n.toString(16), i = 2 * se, o = r.length, a = 0; a < i - o; a++)
            r = "0".concat(r);
        return r
    }
      , le = function(t) {
        var e, n, r = [], i = se - 20;
        if (i <= 0)
            return "";
        for (e = 0,
        n = t.length; e < n; e += i) {
            var o = ce(t.substring(e, e + i)) || "";
            r.push(o)
        }
        return r.join("|")
    };
    function fe(t) {
        return null === t || void 0 === t
    }
    var pe = !/Macintosh/.test(jt) && /\bQQMusic\//i.test(jt);
    function de(t, e, n, r) {
        !function(t) {
            pe && (window.WebViewJavascriptBridge ? t() : document.addEventListener("WebViewJavascriptBridgeReady", t))
        }((function() {
            var i, o, a = window.setTimeout((function() {
                a = 0,
                n({})
            }
            ), 3e3);
            null === (i = M) || void 0 === i || null === (o = i.client) || void 0 === o || o.invoke(t, e, r || {}, (function(t) {
                a && (clearTimeout(a),
                n(t && 0 === t.code && t.data || {}))
            }
            ))
        }
        ))
    }
    var he, ve = [], me = function(t) {
        Array.isArray(t) && t.length ? ve = ve.concat(t) : Array.isArray(t) || "object" !== at(t) || (ve = ve.concat([t]));
        he && clearTimeout(he),
        he = window.setTimeout((function() {
            he && clearTimeout(he),
            he = null,
            de("core", "support", (function(t) {
                t && 0 === +t.code && t.data && 1 === +t.data.isSupport ? de("other", "privacyReport", (function() {
                    ve = []
                }
                ), {
                    reportArray: ve
                }) : ve = []
            }
            ), {
                apiName: "other.privacyReport"
            })
        }
        ), 1e3)
    }, ge = !1, ye = function(t) {
        var e = t.name
          , n = t.value
          , r = t.domain
          , i = t.path
          , o = void 0 === i ? "/" : i
          , a = t.hour
          , u = t.date;
        if ("undefined" !== typeof document) {
            var s;
            (a || u) && (s = "string" === typeof u ? new Date(u) : new Date,
            a && s.setTime(s.getTime() + 36e5 * a));
            var c = "";
            s && (c = "expires=".concat(s.toUTCString(), ";")),
            document.cookie = "".concat(e, "=").concat(n, ";").concat(c, "domain=").concat(fe(r) ? Dt.host : r, ";path=").concat(o, ";")
        }
    }, be = function(t) {
        if ("undefined" === typeof document)
            return "";
        ge || (ge = !0,
        me({
            id: 203,
            purpose_id: 5,
            scene_id: 5,
            content: "\u7528\u6237cookie"
        }));
        var e = document.cookie.match(RegExp("(^|;\\s*)".concat(t, "=([^;]*)(;|$)")));
        return function(t) {
            var e = t;
            if (!e)
                return e;
            e !== decodeURIComponent(e) && (e = decodeURIComponent(e));
            for (var n = ["<", ">", "'", '"', "%3c", "%3e", "%27", "%22", "%253c", "%253e", "%2527", "%2522"], r = ["&#x3c;", "&#x3e;", "&#x27;", "&#x22;", "%26%23x3c%3B", "%26%23x3e%3B", "%26%23x27%3B", "%26%23x22%3B", "%2526%2523x3c%253B", "%2526%2523x3e%253B", "%2526%2523x27%253B", "%2526%2523x22%253B"], i = 0; i < n.length; i += 1)
                e = e.replace(new RegExp(n[i],"gi"), r[i]);
            return e
        }(e ? decodeURIComponent(e[2]) : "")
    };
    function we(t) {
        var e = t.split(".")
          , n = "qq.com";
        return e.length > 2 && (e = e.slice(e.length - 2)),
        2 == e.length && (n = e.join(".")),
        n
    }
    var xe, _e, Ee, ke = function(t, e, n) {
        var r = be(t) || "";
        return r || (r += e(),
        ye({
            name: t,
            date: n,
            value: r,
            domain: we(Dt.hostname)
        })),
        r
    }, Te = function() {
        var t = (new Date).getUTCMilliseconds()
          , e = Math.round(2147483647 * Math.abs(Math.random() - 1)) * t % 1e10;
        return "".concat(e)
    }, Se = function() {
        return ke("pgv_pvid", Te, "Mon, 18 Jan 2038 00:00:00 GMT")
    }, Oe = function() {
        return ke("fqm_pvqid", Pt, "Mon, 18 Jan 2038 00:00:00 GMT")
    }, Ce = function() {
        return ke("fqm_sessionid", Pt)
    }, Ae = !1, Pe = function() {
        var t, e, n = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : jt, r = "";
        (e = n.match(/(?:Android);?[\s/]+([\d.]+)?/)) ? (r = "android",
        n.match(/Mobile/) || (r = "androidpad")) : (e = n.match(/(?:iPad).*OS\s([\d_]+)/)) ? r = "ipad" : (e = n.match(/(?:iPhone\sOS)\s([\d_]+)/)) ? r = "iphone" : (e = n.match(/(?:iPod)(?:.*OS\s([\d_]+))?/)) ? r = "ipod" : /Macintosh/.test(n) && (e = n.match(/OS X ([\d_.]+)/)) ? r = "mac" : /Win\d|Windows/.test(n) && (e = n.match(/Windows NT ([\d.]+)/)) ? r = "windows" : /Linux/.test(n) && (r = "linux");
        var i = {
            platform: r || "other",
            version: (null === (t = e) || void 0 === t ? void 0 : t[1]) || ""
        };
        return Ae || (Ae = !0,
        i.version && me({
            id: 309,
            purpose_id: 17,
            scene_id: 5,
            content: i.version
        })),
        i
    }, Me = function() {
        var t, e, n = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : jt, r = "";
        return (e = n.match(/QQMUSIC\/(\d[.\d]*)/i)) ? (r = "music",
        /Macintosh/.test(n) && (r = "macmusic")) : (e = n.match(/pcqqmusic\/(\d[.\d]*)/i)) ? r = "pcmusic" : (e = n.match(/\bBLACKKEY\/(\d[.\d]*)/i)) ? r = "moo" : (e = n.match(/\bQQMUSICLITE\/(\d[.\d]*)/i)) ? r = "xiaomimusiclite" : (e = n.match(/\bQQMUSICLIGHT\/(\d[.\d]*)/i)) ? r = "musiclight" : (e = n.match(/\bQMfanlive\/(\d[.\d]*)/i)) ? r = "qmlive" : (e = n.match(/\blazyaudio\/(\d[.\d]*)/i)) ? r = "lazyaudio" : (e = n.match(/\bKWMusic\/(\d[.\d]*)/i)) ? r = "kuwo" : (e = n.match(/\bkucy\/(\d[.\d]*)/i)) ? r = "kucy" : (e = n.match(/\bFanxing2\/(\d[.\d]*)/i)) ? r = "fanxing" : (e = n.match(/\bKGBrowser\/(\d[.\d]*)/i) || n.match(/\bKugouBrowser\/(\d[.\d]*)/i)) ? r = "kugou" : (e = n.match(/MicroMessenger\/(\d[.\d]*)/i)) ? r = "weixin" : (e = n.match(/(?:iPad|iPhone|iPod).*? (?:IPad)?QQ\/([\d.]+)/) || n.match(/\bV1_AND_SQI?_(?:[\d.]+)(?:.*? QQ\/([\d.]+))?/)) ? r = "mqq" : (e = n.match(/\bqmkege\/(\d[.\d]*)/i)) ? r = "qmkege" : (e = n.match(/Weibo \(.*weibo__([\d.]+)/i)) ? r = "weibo" : (e = n.match(/^.*wxwork\/([\d.]+).*$/i)) ? r = "wxwork" : (e = n.match(/\/[\w. ]+MQQBrowser\/([\d.]+)/i)) ? r = "mqqbrowser" : (e = n.match(/Qzone\/V1_(?:AND|IPH)_QZ_([\d._]*\d)/i)) ? r = "qzone" : /WeSecure|MQQSecure/.test(n) ? r = "tcs" : (e = n.match(/Version\/([\d.]+)([^S](Safari)|[^M]*(Mobile)[^S]*(Safari))/)) ? r = "safari" : (e = n.match(/\/[\w. ]+QQBrowser\/([\d.]+)/i)) ? r = "qqbrowser" : (e = n.match(/Edge\/([\d.]+)/i)) ? r = "edge" : (e = n.match(/MSIE\s([\d.]+)/) || n.match(/Trident\/[\d](?=[^?]+).*rv:([0-9.]*)/)) ? r = "ie" : (e = n.match(/Firefox\/([\d.]+)/)) ? r = "firefox" : (e = n.match(/Chrome\/([\d.]+)/) || n.match(/CriOS\/([\d.]+)/)) && (r = "chrome"),
        {
            client: r || "other",
            version: (null === (t = e) || void 0 === t ? void 0 : t[1]) || ""
        }
    };
    !function(t) {
        t[t.NO = 0] = "NO",
        t[t.QQ = 1] = "QQ",
        t[t.WX = 2] = "WX",
        t[t.FB = 3] = "FB",
        t[t.MBN = 4] = "MBN",
        t[t.WB = 5] = "WB"
    }(xe || (xe = {})),
    function(t) {
        t[t.NO = 0] = "NO",
        t[t.YES = 1] = "YES"
    }(_e || (_e = {})),
    function(t) {
        t.PGLOAD = "pgload",
        t.PGEXP = "event_pgexp",
        t.PGDEXP = "event_pgdexp",
        t.ELEEXP = "event_eleexp",
        t.ELEDEXP = "event_eledexp",
        t.ELECLICK = "event_eleclick",
        t.VOTE = "event_vote",
        t.SHARE = "event_share",
        t.FAV = "event_favorite",
        t.PLAY = "event_play",
        t.INOUT = "event_inout",
        t.PUB = "event_publish",
        t.APPSHARE = "event_appshare"
    }(Ee || (Ee = {}));
    var Re, De = be("wxopenid"), Ie = function() {
        var t = De || ""
          , e = be("wxunionid") || ""
          , n = be("psrf_qqopenid") || ""
          , r = function() {
            var t = 0;
            return 0 === (t = (t = be(De ? "wxuin" : "uin")) || be("p_uin") || be("qqmusic_uin")).indexOf("o") && (t = t.substring(1, t.length)),
            /^\d+$/.test(t) ? t.length < 14 && (t = parseInt(t, 10)) : t = 0,
            (t || "").toString()
        }()
          , i = xe.NO;
        return r && r.length >= 14 ? i = xe.WX : r && r.length < 14 && (i = xe.QQ),
        {
            uin: r,
            wxopenid: t,
            wxunionid: e,
            qqopenid: n,
            accSource: i
        }
    }, je = function() {
        return be("nft_uin")
    };
    function Ne() {
        var t = jt.match(/\bNetType\/(\w+)/i);
        return t ? t[1] : "unknown"
    }
    function Le(t) {
        var e = Dt.href.split("#")[0].match(new RegExp("(\\?|&)".concat(t, "=(.*?)(#|&|$)"),"i"));
        return decodeURIComponent(e ? e[2] : "")
    }
    !function(t) {
        t.DEVICE = "getDeviceInfo",
        t.GUID = "getGuid"
    }(Re || (Re = {}));
    var Be = function(t) {
        return new Promise((function(e) {
            de("device", t, (function(t) {
                e(t || {})
            }
            ))
        }
        ))
    }
      , Fe = function() {
        return Promise.all([Be(Re.DEVICE), Be(Re.GUID)]).then((function(t) {
            var e = dt(t, 2)
              , n = e[0]
              , r = e[1];
            return {
                c_idfv: n.identifier || "",
                c_idfa: n.idfa || "",
                c_is_rooted: n.isBroken || "0",
                c_device_model: n.model || "",
                c_imsi: r.imsi || "",
                c_imei1: r.imei || "",
                c_uuid: r.uid || "",
                c_udid: r.uuid || "",
                c_operator_name: r.isp || ""
            }
        }
        ))
    };
    window.fqm_visit_id = window.fqm_visit_id || Pt();
    function qe(t) {
        this.url = [],
        this.init(t)
    }
    var Ue, ze, Qe, Ve, Je, We, Ye, $e, Ge, He, Xe, Ke, Ze, tn = "-", en = 0, nn = 0, rn = "tcss.3.1.5", on = {};
    "undefined" == typeof Ze && (Ze = 1);
    var an = {
        sck: [],
        sco: {},
        init: function() {
            var t = this.get("pgv_info=", !0);
            if (t != tn)
                for (var e = t.split("&"), n = 0; n < e.length; n++) {
                    var r = e[n].split("=");
                    this.set(r[0], unescape(r[1]))
                }
        },
        get: function(t, e) {
            var n, r, i = e ? Ue.cookie : this.get("pgv_info=", !0), o = tn;
            if ((n = i.indexOf(t)) > -1) {
                if (n += t.length,
                -1 == (r = i.indexOf(";", n)) && (r = i.length),
                !e) {
                    var a = i.indexOf("&", n);
                    a > -1 && (r = Math.min(r, a))
                }
                o = i.substring(n, r)
            }
            return o
        },
        set: function(t, e) {
            this.sco[t] = e;
            for (var n = !1, r = this.sck.length, i = 0; i < r; i++)
                if (t == this.sck[i]) {
                    n = !0;
                    break
                }
            n || this.sck.push(t)
        },
        setCookie: function(t, e, n) {
            var r = ze.hostname
              , i = an.get(t + "=", e);
            if (i != tn || n)
                i = n || i;
            else {
                switch (t) {
                case "ts_uid":
                    He.push("nw=1");
                    break;
                case "ssid":
                    en = 1
                }
                i = e ? "" : "s";
                var o = (new Date).getUTCMilliseconds();
                i += Math.round(2147483647 * Math.abs(Math.random() - 1)) * o % 1e10
            }
            if (e)
                switch (t) {
                case "ts_uid":
                    this.saveCookie(t + "=" + i, r, this.getExpires(1051200));
                    break;
                case "ts_refer":
                    this.saveCookie(t + "=" + i, r, this.getExpires(259200));
                    break;
                case "ts_last":
                    this.saveCookie(t + "=" + i, r, this.getExpires(30));
                    break;
                default:
                    this.saveCookie(t + "=" + i, We, "expires=Sun, 18 Jan 2038 00:00:00 GMT;")
                }
            else
                this.set(t, i);
            return i
        },
        getExpires: function(t) {
            var e = new Date;
            return e.setTime(e.getTime() + 60 * t * 1e3),
            "expires=" + e.toGMTString()
        },
        save: function() {
            var t = null;
            Ve.sessionSpan && (t = new Date).setTime(t.getTime() + 60 * Ve.sessionSpan * 1e3);
            for (var e = "", n = this.sck.length, r = 0; r < n; r++)
                e += this.sck[r] + "=" + this.sco[this.sck[r]] + "&";
            e = "pgv_info=" + e.substr(0, e.length - 1);
            var i = "";
            t && (i = "expires=" + t.toGMTString()),
            this.saveCookie(e, We, i)
        },
        saveCookie: function(t, e, n) {
            Ue.cookie = t + ";path=/;domain=" + e + ";" + n
        }
    };
    qe.prototype = {
        init: function(t) {
            if (Ve = t || {},
            Ue = document,
            !Ve.statIframe && window != window.top)
                try {
                    Ue = window.top.document
                } catch (_t) {}
            "undefined" == typeof Ue && (Ue = document),
            ze = Ue.location,
            Qe = Ue.body,
            He = [],
            Xe = [],
            Ke = []
        },
        run: function() {
            var t, e, n;
            t = (new Date).getTime(),
            an.init(),
            this.url.push(this.getDomainInfo()),
            this.coverCookie(),
            an.setCookie("ssid"),
            an.save(),
            this.url.unshift(window.location.protocol + "//pingfore." + this.getCookieSetDomain(Je) + "/pingd?"),
            this.url.push(this.getRefInfo(Ve));
            try {
                navigator.cookieEnabled ? this.url.push("&pvid=" + an.setCookie("pgv_pvid", !0)) : this.url.push("&pvid=NoCookie")
            } catch (u) {
                this.url.push("&pvid=NoCookie")
            }
            if (this.url.push(this.getMainEnvInfo()),
            this.url.push(this.getExtendEnvInfo()),
            on.pgUserType = "",
            Ve.pgUserType || Ve.reserved2) {
                var r = Ve.pgUserType || Ve.reserved2;
                r = escape(r.substring(0, 256)),
                on.pgUserType = r,
                Ke.push("pu=" + on.pgUserType)
            }
            this.url.push("&vs=" + rn),
            an.setCookie("ts_uid", !0),
            e = (new Date).getTime(),
            He.push("tm=" + (e - t)),
            en && He.push("ch=" + en),
            n = Ve.extParam ? Ve.extParam + "|" : "",
            this.url.push("&ext=" + escape(n + He.join(";"))),
            this.url.push("&hurlcn=" + escape(Xe.join(";"))),
            this.url.push("&rand=" + Math.round(1e5 * Math.random())),
            "undefined" == typeof window._speedMark ? this.url.push("&reserved1=-1") : this.url.push("&reserved1=" + (new Date - window._speedMark));
            var i = this.getSud();
            if (i && Ke.push("su=" + escape(i.substring(0, 256))),
            this.url.push("&tt=" + escape(Ke.join(";"))),
            this.sendInfo(this.url.join("")),
            1 == nn) {
                var o = this.getParameter("tcss_rp_dm", Ue.URL);
                if (o != on.dm) {
                    var a = this.url.join("").replace(/\?dm=(.*?)\&/, "?dm=" + o + "&");
                    this.sendInfo(a)
                }
            }
            Ve.hot && (document.attachEvent ? document.attachEvent("onclick", (function(t) {
                ln(t)
            }
            )) : document.addEventListener("click", (function(t) {
                ln(t)
            }
            ), !1)),
            Ve.repeatApplay && "true" == Ve.repeatApplay && "undefined" != typeof Ze && (Ze = 1)
        },
        getSud: function() {
            if (Ve.sessionUserType)
                return Ve.sessionUserType;
            var t = Ve.sudParamName || "sessionUserType";
            return this.getParameter(t, Ue.URL)
        },
        coverCookie: function() {
            if (Ve.crossDomain && "on" == Ve.crossDomain) {
                var t = this.getParameter("tcss_uid", Ue.URL)
                  , e = this.getParameter("tcss_sid", Ue.URL)
                  , n = this.getParameter("tcss_refer", Ue.URL)
                  , r = this.getParameter("tcss_last", Ue.URL);
                e && t && (nn = 1,
                an.setCookie("ssid", !1, e),
                an.save(),
                an.setCookie("ts_refer", !0, n),
                an.setCookie("ts_last", !0, r),
                an.setCookie("pgv_pvid", !0, t))
            }
        },
        getDomainInfo: function(t) {
            var e;
            return e = ze.hostname.toLowerCase(),
            Ve.virtualDomain && (Xe.push("ad=" + e),
            e = Ve.virtualDomain),
            this.getCurrentUrl(),
            on.dm = e,
            Je = on.dm,
            t && (on.dm += ".hot"),
            We || (We = this.getCookieSetDomain(ze.hostname.toLowerCase())),
            "dm=" + on.dm + "&url=" + on.url
        },
        getCurrentUrl: function() {
            var t = ""
              , e = tn;
            if (t = escape(ze.pathname),
            "" != ze.search && (e = escape(ze.search.substr(1))),
            Ve.senseParam) {
                var n = this.getParameter(Ve.senseParam, Ue.URL);
                n && (t += "_" + n)
            }
            Ve.virtualURL && (Xe.push("au=" + t),
            t = Ve.virtualURL),
            on.url = t,
            on.arg = e
        },
        getRefInfo: function(t) {
            var e, n, r, i = tn, o = tn, a = tn, u = Ue.referrer;
            if (e = t.tagParamName || "ADTAG",
            n = this.getParameter(e, Ue.URL),
            (r = u.indexOf("://")) > -1) {
                var s = u.match(/(\w+):\/\/([^\:|\/]+)(\:\d*)?(.*\/)([^#|\?|\n]+)?(#.*)?(\?.*)?/i);
                s && (i = s[2],
                o = s[4] + (s[5] ? s[5] : ""))
            }
            -1 != u.indexOf("?") && (r = u.indexOf("?") + 1,
            a = u.substr(r));
            var c, l = i;
            if (Ve.virtualRefDomain && (i != tn && Xe.push("ard=" + i),
            i = Ve.virtualRefDomain),
            Ve.virtualRefURL && (o != tn && Xe.push("aru=" + escape(o)),
            o = Ve.virtualRefURL),
            n && (c = i + o,
            i = "ADTAG",
            o = n),
            Ye = i,
            $e = escape(o),
            Ye == tn || "ADTAG" == Ye && l == tn) {
                var f = an.get("ts_last=", !0);
                f != tn && He.push("ls=" + f)
            }
            an.setCookie("ts_last", !0, escape((ze.hostname + ze.pathname).substring(0, 128)));
            var p = an.get("ts_refer=", !0);
            p != tn && He.push("rf=" + p);
            var d = ze.hostname;
            if (Ve.inner && (d = "," + d + "," + Ve.inner + ","),
            !(Ye == tn || ("," + d + ",").indexOf(Ye) > -1 || 1 == nn)) {
                var h = escape((Ye + o).substring(0, 128));
                h != p && (en = 2),
                an.setCookie("ts_refer", !0, h)
            }
            return on.rdm = Ye,
            on.rurl = $e,
            on.rarg = escape(a),
            c ? "&rdm=" + on.rdm + "&rurl=" + on.rurl + "&rarg=" + on.rarg + "&or=" + c : "&rdm=" + on.rdm + "&rurl=" + on.rurl + "&rarg=" + on.rarg
        },
        getMainEnvInfo: function() {
            var t = "";
            try {
                var e = tn
                  , n = tn
                  , r = tn
                  , i = navigator;
                window.self.screen && (e = window.self.screen.width + "x" + window.self.screen.height,
                n = window.self.screen.colorDepth + "-bit"),
                t = "&scr=" + e + "&scl=" + n + "&lang=" + (r = i.language ? i.language.toLowerCase() : i.browserLanguage ? i.browserLanguage.toLowerCase() : r) + "&java=" + (i.javaEnabled() ? 1 : 0) + "&pf=" + i.platform + "&tz=" + (new Date).getTimezoneOffset() / 60
            } catch (o) {} finally {
                return t
            }
        },
        getExtendEnvInfo: function() {
            var t = "";
            try {
                var e = ze.href
                  , n = tn;
                t += "&flash=" + this.getFlashInfo(),
                Qe.addBehavior && (Qe.addBehavior("#default#homePage"),
                Qe.isHomePage(e) && (t += "&hp=Y")),
                Qe.addBehavior && (Qe.addBehavior("#default#clientCaps"),
                n = Qe.connectionType),
                t += "&ct=" + n
            } catch (At) {} finally {
                return t
            }
        },
        getFlashInfo: function() {
            var t = tn
              , e = navigator;
            try {
                if (e.plugins && e.plugins.length) {
                    for (var n = 0; n < e.plugins.length; n++)
                        if (e.plugins[n].name.indexOf("Shockwave Flash") > -1) {
                            t = e.plugins[n].description.split("Shockwave Flash ")[1];
                            break
                        }
                } else if (window.ActiveXObject)
                    for (var r = 12; r >= 5; r--)
                        try {
                            if (new window.ActiveXObject("ShockwaveFlash.ShockwaveFlash." + r)) {
                                t = r + ".0";
                                break
                            }
                        } catch (i) {}
            } catch (o) {}
            return t
        },
        getParameter: function(t, e) {
            if (t && e) {
                var n = new RegExp("(\\?|#|&)" + t + "=([^&^#]*)(#|&|$)")
                  , r = e.match(n);
                return r ? r[2] : ""
            }
            return ""
        },
        getCookieSetDomain: function(t) {
            for (var e, n, r = [], i = 0, o = 0; o < t.length; o++)
                "." == t.charAt(o) && (r[i] = o,
                i++);
            return e = r.length,
            t.indexOf(".cn") > -1 && e--,
            n = "qq.com",
            n = 1 == e ? t : e > 1 ? t.substring(r[e - 2] + 1) : n
        },
        watchClick: function(t) {
            try {
                var e, n = !0, r = "";
                switch (((null === (e = (window.event ? window.event.srcElement : t.target) || {
                    tagName: ""
                }) || void 0 === e ? void 0 : e.tagName) || "").toUpperCase()) {
                case "A":
                    r = "<a href=" + e.href + ">" + e.innerHTML + "</a>";
                    break;
                case "IMG":
                    r = "<img src=" + e.src + " />";
                    break;
                case "INPUT":
                    r = "<input type=" + e.type + " value=" + e.value + " />";
                    break;
                case "BUTTON":
                    r = "<button>" + e.innerText + "</button>";
                    break;
                case "SELECT":
                    r = "select";
                    break;
                default:
                    n = !1
                }
                if (n) {
                    var i = new qe(Ve)
                      , o = i.getElementPos(e);
                    if (Ve.coordinateId) {
                        var a = i.getElementPos(document.getElementById(Ve.coordinateId));
                        o.x -= a.x
                    }
                    i.url.push(i.getDomainInfo(!0)),
                    i.url.push("&hottag=" + escape(r)),
                    i.url.push("&hotx=" + o.x),
                    i.url.push("&hoty=" + o.y),
                    i.url.push("&rand=" + Math.round(1e5 * Math.random())),
                    i.url.unshift(window.location.protocol + "//pingfore." + this.getCookieSetDomain(Je) + "/pingd?"),
                    i.sendInfo(i.url.join(""))
                }
            } catch (u) {}
        },
        getElementPos: function(t) {
            if (null === t.parentNode || "none" == t.style.display)
                return !1;
            var e, n, r, i, o, a = navigator.userAgent.toLowerCase(), u = null, s = [];
            if (t.getBoundingClientRect)
                return e = t.getBoundingClientRect(),
                n = Math.max(document.documentElement.scrollTop, document.body.scrollTop),
                r = Math.max(document.documentElement.scrollLeft, document.body.scrollLeft),
                i = document.body.clientTop,
                o = document.body.clientLeft,
                {
                    x: e.left + r - o,
                    y: e.top + n - i
                };
            if (document.getBoxObjectFor) {
                e = document.getBoxObjectFor(t);
                var c = t.style.borderLeftWidth ? Math.floor(t.style.borderLeftWidth) : 0
                  , l = t.style.borderTopWidth ? Math.floor(t.style.borderTopWidth) : 0;
                s = [e.x - c, e.y - l]
            } else {
                if (s = [t.offsetLeft, t.offsetTop],
                (u = t.offsetParent) != t)
                    for (; u; )
                        s[0] += u.offsetLeft,
                        s[1] += u.offsetTop,
                        u = u.offsetParent;
                (a.indexOf("opera") > -1 || a.indexOf("safari") > -1 && "absolute" == t.style.position) && (s[0] -= document.body.offsetLeft,
                s[1] -= document.body.offsetTop)
            }
            for (u = t.parentNode ? t.parentNode : null; u && u.tagName && "BODY" != u.tagName && "HTML" != u.tagName; )
                s[0] -= u.scrollLeft,
                s[1] -= u.scrollTop,
                u = u.parentNode ? u.parentNode : null;
            return {
                x: s[0],
                y: s[1]
            }
        },
        sendClick: function() {
            Ve.hottag && (this.url.push(this.getDomainInfo(!0)),
            this.url.push("&hottag=" + escape(Ve.hottag)),
            this.url.push("&hotx=9999&hoty=9999"),
            this.url.push("&rand=" + Math.round(1e5 * Math.random())),
            this.url.unshift(window.location.protocol + "//pingfore." + this.getCookieSetDomain(Je) + "/pingd?"),
            this.sendInfo(this.url.join("")))
        },
        pgvGetArgs: function() {
            this.getDomainInfo();
            var t = [];
            return t.push("tcss_rp_dm=" + on.dm),
            t.push("tcss_uid=" + an.get("pgv_pvid=", !0)),
            t.push("tcss_sid=" + an.get("ssid=", !0)),
            t.push("tcss_refer=" + an.get("ts_refer=", !0)),
            t.push("tcss_last=" + an.get("ts_last=", !0)),
            t.join("&")
        },
        sendInfo: function(t) {
            Ge = new Image(1,1),
            on.img = Ge,
            Ge.onload = Ge.onerror = Ge.onabort = function() {
                Ge.onload = Ge.onerror = Ge.onabort = null,
                on.img = null
            }
            ,
            Ge.src = t
        }
    };
    var un = []
      , sn = [];
    function cn(t, e) {
        var n = "";
        e ? (n = e,
        rn = "tcsso.3.1.5") : (n = t,
        rn = "tcss.3.1.5");
        try {
            if (1 != Ze)
                return;
            Ze = 2,
            new qe(n).run()
        } catch (r) {}
    }
    function ln(t, e) {
        var n = [].slice.apply(arguments)
          , r = "";
        e ? (r = e,
        rn = "tcsso.3.1.5") : (r = t,
        rn = "tcss.3.1.5");
        try {
            if (1 != Ze)
                return;
            Ze = 2;
            var i = new qe(r);
            i.watchClick && i.watchClick.apply(i, n)
        } catch (o) {}
    }
    function fn(t, e, n) {
        var r, i, o, a = fn;
        t && (n = n || {},
        r = "sndImg_" + a._sndCount++,
        (i = a._sndPool[r] = new Image).iid = r,
        i.onload = i.onerror = i.ontimeout = (o = i,
        function(t) {
            var e, r;
            t = t || window.event || {
                type: "timeout"
            },
            "function" == typeof n[t.type] && setTimeout((e = t.type,
            r = o._s_,
            function() {
                n[e]({
                    type: e,
                    duration: (new Date).getTime() - r
                })
            }
            ), 0),
            fn._clearFn(t, o)
        }
        ),
        "function" == typeof n.timeout && setTimeout((function() {
            i.ontimeout && i.ontimeout({
                type: "timeout"
            })
        }
        ), "number" == typeof n.timeoutValue ? Math.max(100, n.timeoutValue) : 5e3),
        "number" == typeof e ? setTimeout((function() {
            i._s_ = (new Date).getTime(),
            i.src = t
        }
        ), e = Math.max(0, e)) : i.src = t)
    }
    window.pgvWatchClick = ln,
    fn._sndPool = {},
    fn._sndCount = 0,
    fn._clearFn = function(t, e) {
        var n = fn;
        e && (n._sndPool[e.iid] = e.onload = e.onerror = e.ontimeout = e._s_ = null,
        delete n._sndPool[e.iid],
        n._sndCount--,
        e = null)
    }
    ;
    var pn, dn = {
        pgvMain: cn,
        pgvSendClick: function(t) {
            var e = [].slice.apply(arguments)
              , n = new qe(e[0]);
            n.sendClick && n.sendClick()
        },
        pgvWatchClick: ln,
        pingQQ: function(t, e, n) {
            for (var r = n || window.location.href, i = e || window.location.host, o = t || window.location.pathname, a = 0, u = un.length; a < u; a++)
                if (un[a][0].test(r)) {
                    i = un[a][1].substr(7);
                    break
                }
            for (var s = 0, c = sn.length; s < c; s++)
                if (sn[s][0].test(o)) {
                    i = sn[s][1].substr(7);
                    break
                }
            cn("", {
                virtualDomain: i,
                virtualURL: o
            })
        },
        setUrlMap: function(t) {
            Array.isArray(t) && (Array.isArray(t[0]) ? [].push.apply(un, t) : un.push(t))
        },
        setPathMap: function(t) {
            Array.isArray(t) && (Array.isArray(t[0]) ? [].push.apply(sn, t) : sn.push(t))
        },
        pingSender: fn
    };
    y.isBrowser && (pn = new function t() {
        var e, n, r = this, i = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
        ut(this, t),
        lt(this, "pageUrl", void 0),
        lt(this, "statUrl", "//stat6.y.qq.com/h5/"),
        lt(this, "version", "1.4.9"),
        lt(this, "com", void 0),
        lt(this, "items", []),
        lt(this, "timer", void 0),
        lt(this, "getShareParam", (function() {
            var t = Ce();
            return {
                share_origin_id: Le("share_origin_id") || t,
                share_session_id: t
            }
        }
        )),
        lt(this, "reportExposure", (function() {
            var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
            r.reportEvent(pt(pt({}, t), {}, {
                event_category: t.event_category || (t.element_id ? Ee.ELEEXP : Ee.PGEXP)
            }))
        }
        )),
        lt(this, "reportEleExposure", (function() {
            var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
            r.reportEvent(pt(pt({}, t), {}, {
                event_category: t.event_category || Ee.ELEEXP
            }))
        }
        )),
        lt(this, "reportClick", (function(t) {
            r.reportEvent(pt(pt({}, t), {}, {
                event_category: t.event_category || Ee.ELECLICK
            }))
        }
        )),
        lt(this, "reportEvent", (function(t) {
            var e;
            Object.keys(t || {}).forEach((function(e) {
                var n = e
                  , r = t[n];
                "string" !== typeof r && (t[n] = "object" === at(r) ? JSON.stringify(r) : (r || "").toString())
            }
            ));
            var n = pt(pt({
                event_id: Pt()
            }, t), {}, {
                hash: t.hash || "".concat(Dt.hash),
                event_category: t.event_category || Ee.PGEXP,
                app_trace_id: t.app_trace_id || (null === (e = window) || void 0 === e ? void 0 : e.app_trace_id) || "",
                adtag: t.adtag || Le("ADTAG"),
                share_from_uin: (null === t || void 0 === t ? void 0 : t.share_from_uin) || Le("uin") || "",
                operate_time: t.operate_time || Math.floor((new Date).getTime() / 1e3).toString(),
                url: t.url || r.pageUrl
            });
            r.items.push(n),
            r.send()
        }
        )),
        lt(this, "reportShare", (function() {
            var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
            r.reportEvent(pt(pt(pt({}, r.getShareParam()), t), {}, {
                event_category: t.event_category || Ee.APPSHARE
            }))
        }
        )),
        lt(this, "reportPlay", (function(t) {
            r.reportEvent(pt(pt({}, t), {}, {
                event_category: t.event_category || Ee.PLAY
            }))
        }
        )),
        lt(this, "clearSendTimer", (function() {
            r.timer && (clearTimeout(r.timer),
            r.timer = void 0)
        }
        )),
        lt(this, "send", (function() {
            r.clearSendTimer(),
            r.timer = window.setTimeout((function() {
                if (r.clearSendTimer(),
                r.items && !(r.items.length <= 0)) {
                    var t = pt(pt({}, r.com), {}, {
                        items: ht(r.items)
                    })
                      , e = window.encodeURIComponent(JSON.stringify(t))
                      , n = le(e);
                    r.items = [],
                    Mt(r.statUrl, n)
                }
            }
            ), 200)
        }
        ));
        var o = i.statUrl
          , a = void 0 === o ? "" : o
          , u = i.virtualUrl
          , s = i.com
          , c = void 0 === s ? {} : s;
        this.statUrl = a || this.statUrl,
        this.pageUrl = u || "".concat(Dt.hostname).concat(Dt.pathname);
        var l = Pe()
          , f = Me()
          , p = Ie();
        this.com = pt({
            c_appid: "qqmusich5",
            c_key: "landing",
            c_fqm_id: (null === (e = window) || void 0 === e || null === (n = e.__fqm_config__) || void 0 === n ? void 0 : n.appId) || "bcbc9157-72b0-4676-b1fb-dd9cd9a99358",
            c_app_name: "QQ\u97f3\u4e50",
            c_app_name_en: "qqmusic",
            c_event_type: _e.NO,
            c_uid: p.uin || "",
            c_uin: p.uin || "",
            c_nft_id: je() || "",
            c_account_source: p.accSource,
            c_qq_openid: p.qqopenid,
            c_wx_openid: p.wxopenid,
            c_wx_unionid: p.wxunionid,
            c_pgv_pvid: Se(),
            c_pvqid: Oe(),
            c_session_id: Ce(),
            c_visit_id: window.fqm_visit_id,
            c_network_type: Ne(),
            c_client_type: f.client,
            c_client_version: f.version,
            c_platform_type: l.platform,
            c_os_version: l.version,
            c_sdk_version: this.version,
            c_share_origin_id: Le("share_origin_id"),
            c_share_from_session_id: Le("share_session_id")
        }, c),
        pe && Fe().then((function(t) {
            r.com = pt(pt({}, r.com), t)
        }
        ))
    }
    );
    var hn, vn = [{
        k: /\/toplist\//,
        v: "TOPLIST"
    }, {
        k: /\/mv_toplist/,
        v: "MV_TOPLIST"
    }, {
        k: /\/album/,
        v: "ALBUM"
    }, {
        k: /\/album_mall/,
        v: "ALBUM_MALL"
    }, {
        k: /\/albumDetail/,
        v: "ALBUM_DETAIL"
    }, {
        k: /\/category/,
        v: "CATEGORY"
    }, {
        k: /\/singer_list/,
        v: "SINGERLIST"
    }, {
        k: /\/mv\//,
        v: "MV"
    }, {
        k: /\/mvList/,
        v: "MV_LIST"
    }, {
        k: /\/playlist\//,
        v: "PLAYLIST"
    }, {
        k: /\/playlist_edit\//,
        v: "PLAYLIST_EDIT"
    }, {
        k: /\/profile/,
        v: "PROFILE"
    }, {
        k: /\/search/,
        v: "SEARCH"
    }, {
        k: /\/player/,
        v: "PLAYER"
    }, {
        k: /\/singer\//,
        v: "SINGER"
    }, {
        k: /\/songDetail\//,
        v: "SONG_DETAIL"
    }], mn = [], gn = {
        doPvg: function(t) {
            void 0 === t && (t = "");
            var e = "y.qq.com";
            if (t = (t || "").toString()) {
                var n = new RegExp("http(s)?://y.qq.com","i");
                t = t.replace(n, ""),
                /http(s)?:\/\//i.test(t) && (t = t.replace(/http(s)?:\/\//i, ""),
                e = t.substring(0, t.indexOf("/")),
                t = t.substring(t.indexOf("/"), t.length)),
                "/" === (t = t.replace(/(\?|#).+/g, "")) && (t = "/portal/index.html"),
                setTimeout((function() {
                    dn.pgvMain("", {
                        repeatApplay: "true",
                        virtualURL: t,
                        virtualDomain: e,
                        reserved2: ""
                    }),
                    pn.reportExposure({
                        url: t
                    })
                }
                ), 200)
            }
        },
        pgvClickStat: function(t, e, n) {
            if (t && "" !== t) {
                e = e || "",
                n = n || "";
                try {
                    e && "" !== e || (e = function(t) {
                        var e = vn;
                        t = t || window.location.href.replace(/(\?|#).+/g, "").replace(/http:\/\//i, "").replace(/https:\/\//i, "");
                        for (var n = "OTHER", r = 0; r < e.length; r++) {
                            var i = e[r];
                            t.search(i.k) > 0 && (n = i.v,
                            r = e.length)
                        }
                        return "y.qq.com/" === t && (n = "INDEX"),
                        n
                    }());
                    var r = [t.toUpperCase()];
                    e && "" !== e && r.push(e.toUpperCase()),
                    n && "" !== n && r.push(n.toUpperCase()),
                    setTimeout((function() {
                        dn.pgvSendClick({
                            hottag: r.join("."),
                            virtualDomain: "y.qq.com"
                        }),
                        pn.reportClick({
                            url: "" + location.hostname + location.pathname,
                            element_id: r.join(".")
                        })
                    }
                    ), 200)
                } catch (i) {}
            }
        },
        pgvReportStat: function(t, e, n) {
            var r = {
                _appid: "qqmusic",
                _platform: 24,
                _uid: n || h(),
                _os: y.client
            };
            if (Array.isArray(e))
                for (var i = 0; i < e.length; i++) {
                    var o = {
                        _key: t,
                        _opertime: (Date.now() / 1e3 | 0).toString()
                    };
                    T(o, e[i]),
                    mn.push(o)
                }
            else {
                var a = {
                    _key: t,
                    _opertime: (Date.now() / 1e3 | 0).toString()
                };
                T(a, e),
                mn.push(a)
            }
            hn && clearTimeout(hn),
            hn = window.setTimeout((function() {
                var t = {
                    common: r,
                    items: mn
                };
                H({
                    url: "//stat6.y.qq.com/sdk/fcgi-bin/sdk.fcg",
                    data: {
                        data: JSON.stringify(t)
                    }
                }),
                mn.length = 0
            }
            ), 500)
        }
    }
    },
    function(t, e, n) {

        !function(t) {
            var n = "undefined" !== typeof t ? t : "undefined" !== typeof window ? window : "undefined" !== typeof self ? self : void 0;
            var r = function() {
                function t(e, n, r, i, o, a, u, s) {
                    var c = !i;
                    e = +e,
                    n = n || [0],
                    i = i || [[this], [{}]],
                    o = o || {};
                    var l, f = [], p = null;
                    Function.prototype.bind || (l = [].slice,
                    Function.prototype.bind = function(t) {
                        if ("function" != typeof this)
                            throw new TypeError("bind101");
                        var e = l.call(arguments, 1)
                          , n = e.length
                          , r = this
                          , i = function() {}
                          , o = function() {
                            return e.length = n,
                            e.push.apply(e, arguments),
                            r.apply(i.prototype.isPrototypeOf(this) ? this : t, e)
                        };
                        return this.prototype && (i.prototype = this.prototype),
                        o.prototype = new i,
                        o
                    }
                    );
                    for (var d = [function() {
                        i[i.length - 2] = i[i.length - 2] + i.pop()
                    }
                    , function() {
                        for (var a = n[e++], u = [], s = n[e++], c = n[e++], l = [], f = 0; f < s; f++)
                            u[n[e++]] = i[n[e++]];
                        for (f = 0; f < c; f++)
                            l[f] = n[e++];
                        i.push((function e() {
                            var i = u.slice(0);
                            i[0] = [this],
                            i[1] = [arguments],
                            i[2] = [e];
                            for (var s = 0; s < l.length && s < arguments.length; s++)
                                0 < l[s] && (i[l[s]] = [arguments[s]]);
                            return t(a, n, r, i, o)
                        }
                        ))
                    }
                    , function() {
                        i[i.length - 2] = i[i.length - 2] | i.pop()
                    }
                    , function() {
                        i.push(i[n[e++]][0])
                    }
                    , function() {
                        var t = n[e++]
                          , r = i[i.length - 2 - t];
                        i[i.length - 2 - t] = i.pop(),
                        i.push(r)
                    }
                    , , function() {
                        var t = n[e++]
                          , r = t ? i.slice(-t) : [];
                        i.length -= t,
                        t = i.pop(),
                        i.push(t[0][t[1]].apply(t[0], r))
                    }
                    , , , function() {
                        var t = n[e++];
                        i[i.length - 1] && (e = t)
                    }
                    , function() {
                        var t = n[e++]
                          , r = t ? i.slice(-t) : [];
                        i.length -= t,
                        r.unshift(null),
                        i.push(function() {
                            return function(t, e, n) {
                                return new (Function.bind.apply(t, e))
                            }
                            .apply(null, arguments)
                        }(i.pop(), r))
                    }
                    , function() {
                        i[i.length - 2] = i[i.length - 2] - i.pop()
                    }
                    , function() {
                        var t = i[i.length - 2];
                        t[0][t[1]] = i[i.length - 1]
                    }
                    , , function() {
                        var t = n[e++];
                        i[t] = void 0 === i[t] ? [] : i[t]
                    }
                    , , function() {
                        i.push(!i.pop())
                    }
                    , , , , function() {
                        i.push([n[e++]])
                    }
                    , function() {
                        i[i.length - 1] = r[i[i.length - 1]]
                    }
                    , , function() {
                        i.push("")
                    }
                    , , function() {
                        i[i.length - 2] = i[i.length - 2] << i.pop()
                    }
                    , , function() {
                        var t = i.pop();
                        i.push([i[i.pop()][0], t])
                    }
                    , function() {
                        i.push(i[i.pop()[0]][0])
                    }
                    , , function() {
                        i[i.length - 1] = n[e++]
                    }
                    , function() {
                        i[i.length - 2] = i[i.length - 2] >> i.pop()
                    }
                    , , function() {
                        i.push(!1)
                    }
                    , function() {
                        i[i.length - 2] = i[i.length - 2] > i.pop()
                    }
                    , , function() {
                        i[i.length - 2] = i[i.length - 2] ^ i.pop()
                    }
                    , function() {
                        i.push([i.pop(), i.pop()].reverse())
                    }
                    , function() {
                        i.pop()
                    }
                    , function() {
                        i[i[i.length - 2][0]][0] = i[i.length - 1]
                    }
                    , , , , function() {
                        i.push(i[i.length - 1])
                    }
                    , , function() {
                        return !0
                    }
                    , function() {
                        i.push([r, i.pop()])
                    }
                    , function() {
                        var t = n[e++]
                          , o = t ? i.slice(-t) : [];
                        i.length -= t,
                        i.push(i.pop().apply(r, o))
                    }
                    , function() {
                        i[i.length - 2] = i[i.length - 2] >= i.pop()
                    }
                    , , , function() {
                        i.length = n[e++]
                    }
                    , , function() {
                        var t = i.pop()
                          , e = i.pop();
                        i.push([e[0][e[1]], t])
                    }
                    , , function() {
                        i[i.length - 2] = i[i.length - 2] & i.pop()
                    }
                    , function() {
                        e = n[e++]
                    }
                    , , function() {
                        i[i.length - 1] += String.fromCharCode(n[e++])
                    }
                    , , , function() {
                        i[i.length - 2] = i[i.length - 2] === i.pop()
                    }
                    , function() {
                        i.push(void 0)
                    }
                    , function() {
                        var t = i.pop();
                        i.push(t[0][t[1]])
                    }
                    , , function() {
                        i.push(!0)
                    }
                    , , function() {
                        i[i.length - 2] = i[i.length - 2] * i.pop()
                    }
                    , function() {
                        i.push(n[e++])
                    }
                    , function() {
                        i.push(typeof i.pop())
                    }
                    ]; ; )
                        try {
                            for (var h = !1; !h; )
                                h = d[n[e++]]();
                            if (p)
                                throw p;
                            return c ? (i.pop(),
                            i.slice(3 + t.v)) : i.pop()
                        } catch (m) {
                            var v = f.pop();
                            if (void 0 === v)
                                throw m;
                            p = m,
                            e = v[0],
                            i.length = v[1],
                            v[2] && (i[v[2]][0] = p)
                        }
                }
                return t.v = 5,
                t(0, function(t) {
                    var e = t[1]
                      , n = []
                      , r = function(t) {
                        for (var e, n, r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".split(""), i = String(t).replace(/[=]+$/, ""), o = 0, a = 0, u = ""; n = i.charAt(a++); ~n && (e = o % 4 ? 64 * e + n : n,
                        o++ % 4) && (u += String.fromCharCode(255 & e >> (-2 * o & 6))))
                            n = function(t, e, n) {
                                if ("function" == typeof Array.prototype.indexOf)
                                    return Array.prototype.indexOf.call(t, e, n);
                                var r;
                                if (null == t)
                                    throw new TypeError('"array" is null or not defined');
                                var i = Object(t)
                                  , o = i.length >>> 0;
                                if (0 == o)
                                    return -1;
                                if (o <= (n |= 0))
                                    return -1;
                                for (r = Math.max(0 <= n ? n : o - Math.abs(n), 0); r < o; r++)
                                    if (r in i && i[r] === e)
                                        return r;
                                return -1
                            }(r, n);
                        return u
                    }(t[0])
                      , i = e.shift()
                      , o = e.shift()
                      , a = 0;
                    function u() {
                        for (; a === i; )
                            n.push(o),
                            a++,
                            i = e.shift(),
                            o = e.shift()
                    }
                    for (var s = 0; s < r.length; s++) {
                        var c = r.charAt(s).charCodeAt(0);
                        u(),
                        n.push(c),
                        a++
                    }
                    return u(),
                    n
                }(["MwgOAg4DDgQOBQ4GDgc4fzozCQ4CDgMOBA4FDgYOBw4IFzpkOmU6ZjppOm46ZRVFFzpmOnU6bjpjOnQ6aTpvOm49CUc4XzomFzpkOmU6ZjppOm46ZS4XOmE6bTpkNT8JaSYDAy8AOHwJJhc6ZDplOmY6aTpuOmUuAwMGASY+LQERAAEDOAMzCg4CDgMOBA4FDgYOBw4IDgkUCDg8MwgOAg4DDgQOBQ4GDgcXOmc6bDpvOmI6YTpsFUUXOnU6bjpkOmU6ZjppOm46ZTpkPRAJ1iY45gQmFzpnOmw6bzpiOmE6bBUtFzp3Omk6bjpkOm86dxVFFzp1Om46ZDplOmY6aTpuOmU6ZD0QCSY4BiYXOnc6aTpuOmQ6bzp3FS0XOnM6ZTpsOmYVRRc6dTpuOmQ6ZTpmOmk6bjplOmQ9EAkmOAEmFzpzOmU6bDpmFS0+LQGeAAAvACcmJhQJOA0zIg4CDgMOBA4FDgYOBw4IDgkOCg4LDgwODQ4ODg8OEA4RDhIOEw4UDhUOFg4XDhgOGQ4aDhsOHA4dDh4OHw4gFAkXOk86YjpqOmU6Yzp0FQoAKxc6MCVEAAwmJisXOjElRAEMJiYrFzoyJUQCDCYmKxc6MyVEAwwmJisXOjQlRAQMJiYrFzo1JUQFDCYmKxc6NiVEBgwmJisXOjclRAcMJiYrFzo4JUQIDCYmKxc6OSVECQwmJisXOkElRAoMJiYrFzpCJUQLDCYmKxc6QyVEDAwmJisXOkQlRA0MJiYrFzpFJUQODCYmKxc6RiVEI0QUCwwmJicmJhQKFzpBOkI6QzpEOkU6RjpHOkg6STpKOks6TDpNOk46TzpQOlE6UjpTOlQ6VTpWOlc6WDpZOlo6YTpiOmM6ZDplOmY6ZzpoOmk6ajprOmw6bTpuOm86cDpxOnI6czp0OnU6djp3Ong6eTp6OjA6MToyOjM6NDo1OjY6Nzo4Ojk6KzovOj0nJiYUCxQhFzpfOl86czppOmc6bjpfOmg6YTpzOmg6XzoyOjA6MjowOjA6MzowOjUbPwk4MyYhFCEXOl86XzpzOmk6ZzpuOl86aDphOnM6aDpfOjI6MDoyOjA6MDozOjA6NRsDAwYBBAAmFzp0Om86VTpwOnA6ZTpyOkM6YTpzOmUlBgAnJiYUDBc6dzppOm46ZDpvOncVRRc6bzpiOmo6ZTpjOnQ9CTgBJhc6bjphOnY6aTpnOmE6dDpvOnIVRRc6bzpiOmo6ZTpjOnQ9CTgDJhc6bDpvOmM6YTp0Omk6bzpuFUUXOm86YjpqOmU6Yzp0PScmJhQNAwwJOAomFzpSOmU6ZzpFOng6cBUXOkg6ZTphOmQ6bDplOnM6cxc6aS8CFzp0OmU6czp0JRc6bjphOnY6aTpnOmE6dDpvOnIuFzp1OnM6ZTpyOkE6ZzplOm46dDU/BgEnJiYUDhQhFzpfOl86cTptOmY6ZTpfOnM6aTpnOm46XzpjOmg6ZTpjOmsbP0QBPQkmAwwJOAkmAw0QCTg4Jhc6bDpvOmM6YTp0Omk6bzpuLhc6aDpvOnM6dDUXOmk6bjpkOmU6eDpPOmY1FzpxOnE6LjpjOm86bQYBRABEAQsiJyYmFA9BFzpBOnI6cjphOnkVCgArRAAlRC5EGQsMJiYrRAElRAQMJiYrRAIlRAkMJiYrRAMlRDVEGwsMJiYrRAQlRANEDQAMJiYrRAUlRABEFAAMJiYrRAYlRC9EFAsMJiYrRAclRC9EEQsMJiYXOm06YTpwJTgBMwsOAg4DDgQOBQ4GDgcOCBQJAwoJJgMDRAEAOAomAwMbPy0BAgEJCwoOAwYBFzpqOm86aTpuJQQAJhcGAScmJhQQFzpBOnI6cjphOnkVCgArRAAlRAZEDAAMJiYrRAElRAsMJiYrRAIlRAMMJiYrRAMlRAIMJiYrRAQlRAEMJiYrRAUlRAcMJiYrRAYlRAYMJiYrRAclRDlEIAsMJiYXOm06YTpwJTgxMwsOAg4DDgQOBQ4GDgcOCBQJAwoJJgMDRAEAOAEmAwMbPy0BAgEJCwoOAwYBFzpqOm86aTpuJRcGAScmJhQRFzpBOnI6cjphOnkVCgArRAAlRAhEEUQMQwAMJiYrRAElRAtEIgAMJiYrRAIlRDREHAAMJiYrRAMlRDxECAAMJiYrRAQlRA1EDkQNQwAMJiYrRAUlRAdEDEQNQwAMJiYrRAYlRAdEDUQMQwAMJiYrRAclRAtEEEQMQwAMJiYrRAglRAVECEQTQwAMJiYrRAklRApEDkQPQwAMJiYrRAolRBBEEUQOQwAMJiYrRAslRB1EPgAMJiYrRAwlRAxEEUMMJiYrRA0lRApERQAMJiYrRA4lRAdEYQAMJiYrRDxELQslRAYMJiYnJiYDDhAJJjgeJhQRFzpBOnI6cjphOnkVCgArRAAlRBVEBAAMJiYrRAElRBtEJwAMJiYrRAIlRAEMJiYrRAMlRDhEAgAMJiYrRAQlRANEVwAMJiYrRAUlRDVEGQAMJiYrRAYlRDlEQgAMJiYrRAclRBpELQAMJiYrRAglRCVEBAsMJiYrRAklRAwMJiYrRAolRAhECkQRQwAMJiYrRAslRDJEKwAMJiYrRAwlRCFEBwAMJiYrRA0lRApEDEQNQwAMJiYrRA4lRC5EEAAMJiYrRBFEAgslRAhED0QPQwAMJiYnJiYUEhc6QTpyOnI6YTp5FQoAJyYmFBNEACcmJhQTHEQTRAMLMBAJJjgUJhQUFAkUCwMTRAJDGz8bP0Q2RCYLQxQJFAsDE0QCQ0QBABs/Gz8AJyYmFBUUEQMTGz8nJiYUEhc6cDp1OnM6aBsDFAMVJAYBJhQTKxwrBAEEAEQBACcmHgAEAAImOEQUERQLFAkhJwQAJicEACYnJiYUHRcnJiYUHkQAJyYmFB4cRAUwEAkmOBQmFBYUEgMeRANDGz8nJiYUFxQSAx5EA0NEAQAbPycmJhQYFBIDHkQDQ0QCABs/JyYmFBkDFkQCHycmJhQaAxZEAzdEBBkDF0QEHwInJiYUGwMXRAVECgA3RAIZAxhEBh8CJyYmFBwDGEQ1RAoANycmJhQdAx0UCgMZGz8AFAoDGhs/ABQKAxsbPwAUCgMcGz8AJyYmFB4rHCsEAQQARAEAJyYeAAQAAiY4LxQdAx0UChQSRAhEBwAbP0QCHxs/ABQKFBJEC0QEABs/RAM3RAQZGz8AJyYmFBIhJyYmFB8UHRc6cjplOnA6bDphOmM6ZRsXOlI6ZTpnOkU6eDpwFRc6WzpcOi86KzpdFzpnLwIXBgInJiYUIBc6ejp6OmIDDwADHwADEAAnJiYUDxQQFB8UHRQKIScEACYnBAAmJwQAJicEACYnJiYUIBc6dDpvOkw6bzp3OmU6cjpDOmE6czplGwYALQEBASEIAycmJhQIFzpfOmc6ZTp0OlM6ZTpjOnU6cjppOnQ6eTpTOmk6ZzpuGwMJDCYmPi0BhwAALwEmPi0=", [133, 2628, 156, 340, 267, 272, 270, 288, 321, 326, 324, 338, 352, 2575, 786, 790, 788, 869, 904, 908, 906, 944, 945, 949, 947, 983, 991, 995, 993, 1085, 1133, 1217, 1138, 1142, 1140, 1146, 1147, 1151, 1149, 1217, 1336, 1375, 1359, 1369, 1367, 1372, 1376, 1338, 1508, 1547, 1531, 1541, 1539, 1544, 1548, 1510, 1813, 1818, 1816, 2036, 2073, 2078, 2076, 2174, 2172, 2062, 2213, 2218, 2216, 2389, 2387, 2205, 2576, 354]]), n)
            }();
            r.g = function() {
                return r.shift()[0]
            }
            ,
            n.__sign_hash_20200305 = function(t) {
                function e(t, e) {
                    var n = (65535 & t) + (65535 & e);
                    return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
                }
                function n(t, n, r, i, o, a) {
                    return e((u = e(e(n, t), e(i, a))) << (s = o) | u >>> 32 - s, r);
                    var u, s
                }
                function r(t, e, r, i, o, a, u) {
                    return n(e & r | ~e & i, t, e, o, a, u)
                }
                function i(t, e, r, i, o, a, u) {
                    return n(e & i | r & ~i, t, e, o, a, u)
                }
                function o(t, e, r, i, o, a, u) {
                    return n(e ^ r ^ i, t, e, o, a, u)
                }
                function a(t, e, r, i, o, a, u) {
                    return n(r ^ (e | ~i), t, e, o, a, u)
                }
                function u(t) {
                    return function(t) {
                        var e, n = "";
                        for (e = 0; e < 32 * t.length; e += 8)
                            n += String.fromCharCode(t[e >> 5] >>> e % 32 & 255);
                        return n
                    }(function(t, n) {
                        t[n >> 5] |= 128 << n % 32,
                        t[14 + (n + 64 >>> 9 << 4)] = n;
                        var u, s, c, l, f, p = 1732584193, d = -271733879, h = -1732584194, v = 271733878;
                        for (u = 0; u < t.length; u += 16)
                            s = p,
                            c = d,
                            l = h,
                            f = v,
                            p = r(p, d, h, v, t[u], 7, -680876936),
                            v = r(v, p, d, h, t[u + 1], 12, -389564586),
                            h = r(h, v, p, d, t[u + 2], 17, 606105819),
                            d = r(d, h, v, p, t[u + 3], 22, -1044525330),
                            p = r(p, d, h, v, t[u + 4], 7, -176418897),
                            v = r(v, p, d, h, t[u + 5], 12, 1200080426),
                            h = r(h, v, p, d, t[u + 6], 17, -1473231341),
                            d = r(d, h, v, p, t[u + 7], 22, -45705983),
                            p = r(p, d, h, v, t[u + 8], 7, 1770035416),
                            v = r(v, p, d, h, t[u + 9], 12, -1958414417),
                            h = r(h, v, p, d, t[u + 10], 17, -42063),
                            d = r(d, h, v, p, t[u + 11], 22, -1990404162),
                            p = r(p, d, h, v, t[u + 12], 7, 1804603682),
                            v = r(v, p, d, h, t[u + 13], 12, -40341101),
                            h = r(h, v, p, d, t[u + 14], 17, -1502002290),
                            p = i(p, d = r(d, h, v, p, t[u + 15], 22, 1236535329), h, v, t[u + 1], 5, -165796510),
                            v = i(v, p, d, h, t[u + 6], 9, -1069501632),
                            h = i(h, v, p, d, t[u + 11], 14, 643717713),
                            d = i(d, h, v, p, t[u], 20, -373897302),
                            p = i(p, d, h, v, t[u + 5], 5, -701558691),
                            v = i(v, p, d, h, t[u + 10], 9, 38016083),
                            h = i(h, v, p, d, t[u + 15], 14, -660478335),
                            d = i(d, h, v, p, t[u + 4], 20, -405537848),
                            p = i(p, d, h, v, t[u + 9], 5, 568446438),
                            v = i(v, p, d, h, t[u + 14], 9, -1019803690),
                            h = i(h, v, p, d, t[u + 3], 14, -187363961),
                            d = i(d, h, v, p, t[u + 8], 20, 1163531501),
                            p = i(p, d, h, v, t[u + 13], 5, -1444681467),
                            v = i(v, p, d, h, t[u + 2], 9, -51403784),
                            h = i(h, v, p, d, t[u + 7], 14, 1735328473),
                            p = o(p, d = i(d, h, v, p, t[u + 12], 20, -1926607734), h, v, t[u + 5], 4, -378558),
                            v = o(v, p, d, h, t[u + 8], 11, -2022574463),
                            h = o(h, v, p, d, t[u + 11], 16, 1839030562),
                            d = o(d, h, v, p, t[u + 14], 23, -35309556),
                            p = o(p, d, h, v, t[u + 1], 4, -1530992060),
                            v = o(v, p, d, h, t[u + 4], 11, 1272893353),
                            h = o(h, v, p, d, t[u + 7], 16, -155497632),
                            d = o(d, h, v, p, t[u + 10], 23, -1094730640),
                            p = o(p, d, h, v, t[u + 13], 4, 681279174),
                            v = o(v, p, d, h, t[u], 11, -358537222),
                            h = o(h, v, p, d, t[u + 3], 16, -722521979),
                            d = o(d, h, v, p, t[u + 6], 23, 76029189),
                            p = o(p, d, h, v, t[u + 9], 4, -640364487),
                            v = o(v, p, d, h, t[u + 12], 11, -421815835),
                            h = o(h, v, p, d, t[u + 15], 16, 530742520),
                            p = a(p, d = o(d, h, v, p, t[u + 2], 23, -995338651), h, v, t[u], 6, -198630844),
                            v = a(v, p, d, h, t[u + 7], 10, 1126891415),
                            h = a(h, v, p, d, t[u + 14], 15, -1416354905),
                            d = a(d, h, v, p, t[u + 5], 21, -57434055),
                            p = a(p, d, h, v, t[u + 12], 6, 1700485571),
                            v = a(v, p, d, h, t[u + 3], 10, -1894986606),
                            h = a(h, v, p, d, t[u + 10], 15, -1051523),
                            d = a(d, h, v, p, t[u + 1], 21, -2054922799),
                            p = a(p, d, h, v, t[u + 8], 6, 1873313359),
                            v = a(v, p, d, h, t[u + 15], 10, -30611744),
                            h = a(h, v, p, d, t[u + 6], 15, -1560198380),
                            d = a(d, h, v, p, t[u + 13], 21, 1309151649),
                            p = a(p, d, h, v, t[u + 4], 6, -145523070),
                            v = a(v, p, d, h, t[u + 11], 10, -1120210379),
                            h = a(h, v, p, d, t[u + 2], 15, 718787259),
                            d = a(d, h, v, p, t[u + 9], 21, -343485551),
                            p = e(p, s),
                            d = e(d, c),
                            h = e(h, l),
                            v = e(v, f);
                        return [p, d, h, v]
                    }(function(t) {
                        var e, n = [];
                        for (n[(t.length >> 2) - 1] = void 0,
                        e = 0; e < n.length; e += 1)
                            n[e] = 0;
                        for (e = 0; e < 8 * t.length; e += 8)
                            n[e >> 5] |= (255 & t.charCodeAt(e / 8)) << e % 32;
                        return n
                    }(t), 8 * t.length))
                }
                function s(t) {
                    return u(unescape(encodeURIComponent(t)))
                }
                return function(t) {
                    var e, n, r = "";
                    for (n = 0; n < t.length; n += 1)
                        e = t.charCodeAt(n),
                        r += "0123456789abcdef".charAt(e >>> 4 & 15) + "0123456789abcdef".charAt(15 & e);
                    return r
                }(s(t))
            }
            ;
            var i = n._getSecuritySign;
            delete n._getSecuritySign,
            e.default = i
        }
        .call(this, window)
    }
])


// window.dd(0)
// let t = {
//     "data": {
//         "comm": {
//             "cv": 4747474,
//             "ct": 24,
//             "format": "json",
//             "inCharset": "utf-8",
//             "outCharset": "utf-8",
//             "notice": 0,
//             "platform": "yqq.json",
//             "needNewCode": 1,
//             "uin": 0,
//             "g_tk_new_20200303": 5381,
//             "g_tk": 5381
//         },
//         "req_1": {
//             "module": "music.musicasset.SongFavRead",
//             "method": "IsSongFanByMid",
//             "param": {
//                 "v_songMid": [
//                     "004Zw6rF17dkcF"
//                 ]
//             }
//         },
//         "req_2": {
//             "module": "music.musichallSong.PlayLyricInfo",
//             "method": "GetPlayLyricInfo",
//             "param": {
//                 "songMID": "004Zw6rF17dkcF",
//                 "songID": 493556698
//             }
//         },
//         "req_3": {
//             "method": "GetCommentCount",
//             "module": "music.globalComment.GlobalCommentRead",
//             "param": {
//                 "request_list": [
//                     {
//                         "biz_type": 1,
//                         "biz_id": "493556698",
//                         "biz_sub_type": 0
//                     }
//                 ]
//             }
//         },
//         "req_4": {
//             "module": "music.musichallAlbum.AlbumInfoServer",
//             "method": "GetAlbumDetail",
//             "param": {
//                 "albumMid": "0000oWWx1m0XT4"
//             }
//         },
//         "req_5": {
//             "module": "vkey.GetVkeyServer",
//             "method": "CgiGetVkey",
//             "param": {
//                 "guid": "4715782620",
//                 "songmid": [
//                     "004Zw6rF17dkcF"
//                 ],
//                 "songtype": [
//                     0
//                 ],
//                 "uin": "0",
//                 "loginflag": 1,
//                 "platform": "20"
//             }
//         }
//     },
//     "time": 10000,
//     "withCredentials": true,
//     "cache": false,
//     "url": "//u6.y.qq.com/cgi-bin/musicu.fcg",
//     "postType": true,
//     "type": "POST",
//     "needSign": true
// };
//
// let sign = window.B(t);
// console.log(`模拟sign值: ${sign}`);
// console.log('正确sign值: zzba391d04ewchoj6q8zkdaxvr3w1ug6w1f5edbcf');
// console.log(`结果: ${sign == 'zzba391d04ewchoj6q8zkdaxvr3w1ug6w1f5edbcf'}`);


function get_sign(data){
    let t = {
        'data': data,
        "time": 10000,
        "withCredentials": true,
        "cache": false,
        "url": "//u6.y.qq.com/cgi-bin/musicu.fcg",
        "postType": true,
        "type": "POST",
        "needSign": true
    }
    window.dd(0)
    return window.B(t);

}