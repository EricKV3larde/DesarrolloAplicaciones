// JavaScript en archivo externo (calculadora.js)
document.getElementById("sumarButton").addEventListener("click", function() {
    calcular("sumar");
});

document.getElementById("restarButton").addEventListener("click", function() {
    calcular("restar");
});

document.getElementById("multiplicarButton").addEventListener("click", function() {
    calcular("multiplicar");
});

document.getElementById("dividirButton").addEventListener("click", function() {
    calcular("dividir");
});

function calcular(operador) {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    let resultado;

    if (isNaN(num1) || isNaN(num2)) {
        resultado = "Error: Ingresa números válidos";
    } else {
        switch (operador) {
            case 'sumar':
                resultado = num1 + num2;
                break;
            case 'restar':
                resultado = num1 - num2;
                break;
            case 'multiplicar':
                resultado = num1 * num2;
                break;
            case 'dividir':
                if (num2 !== 0) {
                    resultado = num1 / num2;
                } else {
                    resultado = "Error: No puedes dividir por cero";
                }
                break;
            default:
                resultado = "Operación no válida";
                break;
        }
    }

    document.getElementById("resultado").textContent = resultado;
}
