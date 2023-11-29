// Función para mostrar un color y ocultar los demás
function mostrarColor(id) {
    ocultarTodosLosColores();
    document.getElementById(id).style.display = 'block';
}

// Función para ocultar todos los colores
function ocultarTodosLosColores() {
    document.getElementById("color1").style.display = 'none';
    document.getElementById("color2").style.display = 'none';
    document.getElementById("color3").style.display = 'none';
}

// Asociar eventos a botones
document.getElementById("mostrarColor1").addEventListener("click", function() {
    mostrarColor("color1");
});

document.getElementById("mostrarColor2").addEventListener("click", function() {
    mostrarColor("color2");
});

document.getElementById("mostrarColor3").addEventListener("click", function() {
    mostrarColor("color3");
});

document.getElementById("ocultarColores").addEventListener("click", function() {
    ocultarTodosLosColores();
});

