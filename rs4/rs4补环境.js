window = global;
top = window;
window.self = window;
Window = function Window(){}
Window.prototype = window.__proto__;

setTimeout = function () {return {}};
setInterval = function () {return{}};

document = {
    "cookie": '',
    "characterSet": 'UTF-8',
    "charset": "UTF-8",
    "scripts": ['script', 'script'],
};

navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54",
    vendor: "Google Inc.",
    webdriver: false,
    userActivation: { hasBeenActive: false, isActive: false },
    mimeTypes:[{"application/x-shockwave-flash":""}]
};

location = {
    "ancestorOrigins": {},
    "href": "https://hd.ghzyj.sh.gov.cn/2017/xxgk/zcjd/",
    "origin": "https://hd.ghzyj.sh.gov.cn",
    "protocol": "http:",
    "host": "hd.ghzyj.sh.gov.cn",
    "hostname": "hd.ghzyj.sh.gov.cn",
    "port": "",
    "pathname": "/2017/xxgk/zcjd/",
    "search": "",
    "hash": ""
};


div = {}
createElement = function () {
    console.log('创建对象：', arguments[0]);
    switch (arguments[0]) {
        case 'div':
            return div;
        default:
            return {};
    }
};
document.createElement = createElement;

getElementsByTagName = function () {
    console.log('获取元素：', arguments[0]);
    switch (arguments[0]) {
        case 'i':
            return [];
        default:
            return [];
    }
}
div.getElementsByTagName = getElementsByTagName;


getElementsByTagName = function () {
    console.log('获取元素：', arguments[0]);
    switch (arguments[0]) {
        case 'meta':
            return [{
                "content": content,
                "parentNode": {
                    removeChild: function () { }
                }
            }, {
                "content": content,
                "parentNode": {
                    removeChild: function () { }
                }
            }]
        default:
            return [];
    }
};
document.getElementsByTagName = getElementsByTagName;


document.documentElement = {"style":{}}

document.addEventListener = function () {
    console.log(arguments)
    return {}
};
document.attachEvent = function () { 
    console.log(arguments);
    return {} 
};

window.addEventListener = function () {
    console.log(arguments)
    return {}
};
window.attachEvent = function () { 
    console.log(arguments);
    return {} 
};
window.document = document;
window.navigator = navigator;
window.location = location;
delete __filename;
delete __dirname;


