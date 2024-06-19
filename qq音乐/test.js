// 给 URL 添加当前时间戳
e.url = C({ _: Date.now() }, e.url);

// 如果请求类型为 GET，将数据合并到 URL 中，并清空 e.data
if ("GET" === e.type.toUpperCase()) {
    e.url = C(e.data, e.url);
    e.data = void 0;
} else {
    // 如果数据类型为字符串或 FormData，保留原样
    // 否则将数据转换为 JSON 字符串
    if ("string" !== typeof e.data && !(e.data instanceof FormData)) {
        e.data = JSON.stringify(e.data);
    }
}

// 如果需要签名，且 URL 包含 "cgi-bin/musicu.fcg"，并且是在浏览器环境中，将其替换为 "cgi-bin/musics.fcg"
if (e.needSign && -1 !== e.url.indexOf("cgi-bin/musicu.fcg") && y.isBrowser) {
    e.url = e.url.replace("cgi-bin/musicu.fcg", "cgi-bin/musics.fcg");
}

// 如果 URL 包含 "cgi-bin/musics.fcg"，对数据进行签名处理
if (-1 !== e.url.indexOf("cgi-bin/musics.fcg")) {
    var i, o = n(147).default;

    // 根据请求类型对数据进行不同的处理
    if ("GET" === e.type.toUpperCase()) {
        i = o(e.data.data);
    } else {
        i = o(e.data);
    }

    // 将签名添加到 URL 中
    e.url = C({ sign: i }, e.url);
}
