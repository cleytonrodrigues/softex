var exibeMensagem = function () { 
    var mensagemForaDoIf = 'Softex'; 
    if(true) { 
        var mensagemDentroDoIf = 'BackSegunda'; 
        console.log(mensagemDentroDoIf);
    } 
    console.log(mensagemForaDoIf); 

    console.log(mensagemDentroDoIf); 
}

var exibeMensagem2 = function() {
    if(true) { 
        var escopoFuncao = 'Softex'; 
        let escopoBloco = 'BackSegunda';

       console.log(escopoBloco); // Alura 
   } 
   console.log(escopoFuncao); // Caelum 
   console.log(escopoBloco); 
}

exibeMensagem()
exibeMensagem2()

//Em JavaScript, toda variável é “elevada/içada” (hoisting) até o topo do seu contexto de execução. Esse mecanismo move as variáveis para o topo do seu escopo antes da execução do código.
//https://www.alura.com.br/artigos/entenda-diferenca-entre-var-let-e-const-no-javascript?gclid=Cj0KCQjw2_OWBhDqARIsAAUNTTEkUGHTj3vCi8l_xNrcPO4zjWJq-NwJbaH39uHHGaTENKZVKZy3b5YaAj0sEALw_wcB
