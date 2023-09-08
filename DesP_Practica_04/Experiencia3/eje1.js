//Función con Cierre (Closure) 
//Define una función createCounter que devuelve un contador
function createCounter() {
    let count = 0; // Inicializa el contador en 0
  
    // Devuelve una función interna que incrementa el contador
    return function () {
      count++;
      return count;
    };
  }
  
  // Crea dos contadores independientes
  const counter1 = createCounter();
  const counter2 = createCounter();
  
  // Llama a counter1 varias veces y muestra el valor del contador después de cada llamada
  console.log("Counter 1:");
  console.log(counter1()); // Debería mostrar 1
  console.log(counter1()); // Debería mostrar 2
  console.log(counter1()); // Debería mostrar 3
  
  // Llama a counter2 varias veces y muestra el valor del contador después de cada llamada
  console.log("Counter 2:");
  console.log(counter2()); // Debería mostrar 1
  console.log(counter2()); // Debería mostrar 2