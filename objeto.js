function Carro(marca, modelo, ano, valor) {
    this.marca = marca;
    this.modelo = modelo;
    this.ano = ano;
    this.valor = valor;

    this.aumentaValor = function(){
        this.valor += (this.valor*0.1);
    }
  }

  var meucarro = new Carro('fiat','uno','1997',1000);
  console.log(meucarro.valor);
  meucarro.aumentaValor();
  console.log(meucarro.valor);