let bp = require("./balanceParens");

// Add more test cases!...
console.log(bp("abc(d)e(fgh))(i)j)k") === "abc(d)e(fgh)(i)jk")
console.log(bp("abc((d)e(fgh)(i)j(k") === "abc(d)e(fgh)(i)jk")

// Challenge: nested parentheses...
console.log(bp("abc(d)(ef(g(h))ij)k)lm()o)p") === "abc(d)(ef(g(h))ij)klm()op")