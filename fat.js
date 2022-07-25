//expressao de função para criar fatorial
//usa operador
//opção 1
var fatorial = function fac1(n) {return n<2 ? 1 : n*fac1(n-1)};

//opção 2
var fatorial2 = function fac2(n) {
    return n<2 ? 1 : n*fac2(n-1);
};

//função padrão
//opção3
function fac3(n){
    if (n <= 2)
        return 1;
    return n * fac3(n-1);
}


console.log(fatorial(3));
console.log(fatorial2(5));
console.log(fac3(6));