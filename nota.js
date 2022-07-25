const readline = require('readline-sync');

function calculaNota(){
    

    var media = 0
    while(media<7){


        var nota1 = readline.questionInt('Nota 1:');
        var nota2 = readline.questionInt('Nota 2:');

        media = (nota1 + nota2)/2;
        (media<7) ? console.log('Reprovado') : console.log('Aprovado');
    }
}

calculaNota();