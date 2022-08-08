function replacer(key, value) {
    if (typeof value === "string") {
      return undefined;
    }
    return value;
  }
  
  var foo = {fundação: "Mozilla", modelo: "caixa", semana: 45, transporte: "carro", mês: 7};
  console.log(foo)

  var jsonString = JSON.stringify(foo);
  console.log(jsonString)
  
  var object = JSON.parse(jsonString)
  console.log(object)