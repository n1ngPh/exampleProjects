const yoyo1 = require("bindings")("yoyo");   // npm install --global bindings
var yoyo =  yoyo1.yoyo()
yoyo.name = "yoyo"
console.log("yoyo", yoyo)
console.log("typeof yoyo", typeof yoyo)
console.log("yoyo == undefined", yoyo == undefined)
debugger;