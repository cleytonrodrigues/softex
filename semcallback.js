function primeiroBloco(){
    setTimeout(function(){
        console.log("primeira");
    },5000);
}

function segundoBloco(){
    console.log("segunda");
}

primeiroBloco();
segundoBloco();