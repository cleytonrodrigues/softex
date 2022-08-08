function primeiroBloco(callback){
    console.log("primeira");
    callback();
}

function segundoBloco(){
    console.log("segunda");
}

primeiroBloco(segundoBloco);