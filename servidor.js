const http = require("http");

const PORTA = process.PORT || 8888;

const servidor = http.createServer();

servidor.on("request",(request,response)=>{
    //response.write("Olá Mundo");
    response.end("Olá Mundo");
});

servidor.listen(PORTA,() =>{
    console.log(`Servidor Iniciado na porta ${PORTA}`);
});