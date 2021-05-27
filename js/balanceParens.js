const balanceParens = (str) => {
  let openingParensArray = [];
  let balancedStrInitial = "";

  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (char === "(") {
      openingParensArray.push(balancedStrInitial.length);  // add the index of the "(" in balancedStrInitial to openingParensArray. Later, we loop through balancedStrInitial and remove the char if its index matches what's in openingParensArray
    } else if (char === ")") {
      if (openingParensArray.length === 0) {
        continue;
      } else {
        openingParensArray.pop();
      }
    }
    balancedStrInitial += char;  // adds all chars except unmatched ")"'s
  }

  let balancedStrFinal = ""
  if (openingParensArray.length > 0) {
    for (let i = 0; i < balancedStrInitial.length; i++) {
      if (!(openingParensArray.includes(i))) {
        balancedStrFinal += balancedStrInitial[i];
      }
    }
  } else {
    balancedStrFinal = balancedStrInitial;
  }

  return balancedStrFinal
}

console.log(balanceParens(")a(b)c)("));


module.exports = balanceParens;