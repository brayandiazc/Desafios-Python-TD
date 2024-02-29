
// HTML 
var HTML1 = document.getElementById("HTML1");
var HTML2 = document.getElementById("HTML2");
var HTML3 = document.getElementById("HTML3");
var HTMLPromedio = document.getElementById("HTMLPromedio")

var nota1HTML = +prompt("Ingrese la Nota 1 de HTML")
var nota2HTML = +prompt("Ingrese la Nota 2 de HTML")
var nota3HTML = +prompt("Ingrese la Nota 3 de HTML")

HTML1.innerHTML = nota1HTML
HTML2.innerHTML = nota2HTML
HTML3.innerHTML = nota3HTML
HTMLPromedio.innerHTML = ((nota1HTML + nota2HTML + nota3HTML) / 3).toFixed(2)


// CSS

var CSS1 = document.getElementById("CSS1");
var CSS2 = document.getElementById("CSS2");
var CSS3 = document.getElementById("CSS3");
var CSSPromedio = document.getElementById("CSSPromedio")


var nota1CSS = +prompt("Ingrese la Nota 1 de CSS")
var nota2CSS = +prompt("Ingrese la Nota 2 de CSS")
var nota3CSS = +prompt("Ingrese la Nota 3 de CSS")

CSS1.innerHTML = nota1CSS
CSS2.innerHTML = nota2CSS
CSS3.innerHTML = nota3CSS
CSSPromedio.innerHTML = ((nota1CSS + nota2CSS + nota3CSS) / 3).toFixed(2)


// JAVASCRIPT

var JAVASCRIPT1 = document.getElementById("JAVASCRIPT1");
var JAVASCRIPT2 = document.getElementById("JAVASCRIPT2");
var JAVASCRIPT3 = document.getElementById("JAVASCRIPT3");
var JAVASCRIPTPromedio = document.getElementById("JAVASCRIPTPromedio")

var nota1JAVASCRIPT = +prompt("Ingrese la Nota 1 de JAVASCRIPT")
var nota2JAVASCRIPT = +prompt("Ingrese la Nota 2 de JAVASCRIPT")
var nota3JAVASCRIPT = +prompt("Ingrese la Nota 3 de JAVASCRIPT")

JAVASCRIPT1.innerHTML = nota1JAVASCRIPT
JAVASCRIPT2.innerHTML = nota2JAVASCRIPT
JAVASCRIPT3.innerHTML = nota3JAVASCRIPT
JAVASCRIPTPromedio.innerHTML = ((nota1JAVASCRIPT + nota2JAVASCRIPT + nota3JAVASCRIPT) / 3).toFixed(2)