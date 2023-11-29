//Archivo .js

// Función para mostrar un mensaje de saludo
document.getElementById("saludoButton").addEventListener("click", function() {
    alert("¡Ejemplo de JavaScript vinculado!");
});

// Función para aumentar el contador
let contador = 0;
document.getElementById("contadorButton").addEventListener("click", function() {
    contador++;
    document.getElementById("contador").textContent = contador;
});
