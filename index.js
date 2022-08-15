//import express from "express";

var express = require('express');

var app = express();

app.listen(8888);

app.get('/',(request,response)=>{
    return response.send('Olá Mundo!');
});

app.get('/user',(request,response)=>{
    return response.send('Hello World!');
});

app.post('/', function (req, res) {
    return res.send('Got a POST request');
  });

app.put('/user', function (req, res) {
    res.send('Got a PUT request at /user');
  });

app.delete('/user', function (req, res) {
    res.send('Got a DELETE request at /user');
  });