/* CIUDADANO DE PRIMERA CLASE */

// Definición de una función arrow
const foo = () => {
    console.log("foobar");
  }
  
  // Llamada a la función foo
  foo(); // Imprime "foobar"
  
  /*
  Descripción del proceso anterior: 
  En este código, se define una función foo que imprime "foobar" en la consola. Luego, la función se invoca utilizando foo(), lo que resulta en la impresión de "foobar".
  */ 
  
  // Definición de una función sayHello que devuelve un saludo
  function sayHello() {
    return "Hello, ";
  }
  
  // Definición de una función greeting que toma un saludo y un nombre, e imprime el saludo seguido del nombre
  function greeting(helloMessage, name) {
    console.log(helloMessage() + name);
  }
  
  // Llamada a greeting pasando sayHello como argumento
  greeting(sayHello, "JavaScript!"); // Imprime "Hello, JavaScript!"
  
  /*
  Descripción del proceso anterior: 
  En este código, se definen dos funciones: sayHello, que devuelve un saludo, y greeting, que toma un saludo y un nombre y los imprime juntos. Luego, se llama a greeting pasando sayHello como argumento y "JavaScript!" como nombre, lo que resulta en la impresión de "Hello, JavaScript!".
  */ 
  
  // Definición de sayHello como una función que devuelve otra función que imprime "Hello!"
  function sayHello() {
    return () => {
      console.log("Hello!");
    }
  }
  
  /*
  Descripción del proceso anterior: 
  En este código, se redefine sayHello como una función que devuelve otra función. La función devuelta imprime "Hello!" cuando se llama.
  */
  
  /* CLOSURE */
  
  // Definición de una función makeFunc que tiene una variable name y devuelve una función displayName que imprime name
  function makeFunc() {
    const name = 'Mozilla';
    function displayName() {
      console.log(name);
    }
    return displayName;
  }
  
  // Asignación de la función retornada por makeFunc a la variable myFunc
  const myFunc = makeFunc();
  
  // Llamada a myFunc, que imprime "Mozilla" utilizando el concepto de closure
  myFunc();
  
  /*
  Descripción del proceso anterior: 
  En este código, se define una función makeFunc que tiene una variable name y devuelve una función interna displayName. La función makeFunc retorna displayName, que es una función que imprime el valor de name. Luego, se asigna la función retornada a la variable myFunc y se llama a myFunc, lo que imprime "Mozilla". Esto demuestra el concepto de closure, ya que displayName tiene acceso al ámbito léxico de makeFunc incluso después de que makeFunc haya terminado de ejecutarse.
  */
  
  /* ÁMBITO DE FUNCIÓN */
  
  // Intento de imprimir la variable x fuera de la función exampleFunction
  // Esto causará un error porque x solo está definida dentro de exampleFunction
  console.log(x); // Causa un error
  
  // Definición de la variable x fuera de la función exampleFunction
  const x = "declared outside function";
  
  // Llamada a exampleFunction, que imprime "Inside function" y el valor de x
  function exampleFunction() {
    console.log("Inside function");
    console.log(x);
  }
  
  // Imprime "Outside function" y el valor de x nuevamente
  console.log("Outside function");
  console.log(x);
  
  /*
  Descripción del proceso anterior: 
  En este código, se intenta imprimir la variable x fuera de la función exampleFunction, lo que causa un error porque x solo está definida dentro de la función. Luego, se define la variable x fuera de la función y se llama a exampleFunction, que imprime "Inside function" y el valor de x, que es "declared outside function". Después, se imprime "Outside function" seguido del valor de x nuevamente.
  */
  
  // Definición de una función f con try-catch-finally
  function f() {
    try {
      console.log(0);
      throw 'bogus';
    } catch (e) {
      console.log(1);
      return true; // Esta declaración de retorno se suspende
      // hasta que se complete el bloque finally
    } finally {
      console.log(3);
      return false; // Sobrescribe el retorno anterior
    }
    // La declaración de retorno "false" se ejecuta ahora
    console.log(5); // No se alcanza
  }
  
  // Llamada a la función f, que imprimirá 0, 1, 3 y luego devolverá false
  console.log(f()); // Imprime 0, 1, 3, false
  
  /*
  Descripción del proceso anterior: 
  En este código, se define una función f que contiene un bloque try-catch-finally. El bloque catch maneja una excepción, pero el bloque finally se ejecuta siempre, incluso si se arroja una excepción. Dentro del bloque finally, se devuelve false, lo que sobrescribe la declaración de retorno anterior (true) en el bloque catch. Como resultado, la función f devuelve false y no se ejecuta ningún código adicional después del bloque finally.
  */
  
  /* MANEJO DE EXCEPCIONES */
  
  // Definición de una función constructora UserException para crear excepciones personalizadas
  function UserException(message) {
    this.message = message;
    this.name = 'UserException';
  }
  
  // Definición de una función getMonthName que toma un número de mes y devuelve el nombre del mes
  function getMonthName(mo) {
    mo--; // Ajuste del número de mes para el índice del array (1 = Ene, 12 = Dic)
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
      'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    if (months[mo] !== undefined) {
      return months[mo];
    } else {
      throw new UserException('InvalidMonthNo');
    }
  }
  
  let monthName;
  
  try {
    // Declaraciones a intentar
    const myMonth = 15; // 15 está fuera de rango para provocar la excepción
    monthName = getMonthName(myMonth);
  } catch (e) {
    monthName = 'unknown';
    console.error(e.message, e.name); // Se pasa el objeto de excepción al manejador de errores
  }
  
  /*
  Descripción del proceso anterior: 
  En este código, se define una función constructora UserException para crear objetos de excepción personalizados. Luego, se define una función getMonthName que toma un número de mes y devuelve el nombre del mes correspondiente. Si el número de mes está fuera de rango, se arroja una excepción de tipo UserException. En el bloque try, se llama a getMonthName con un valor de mes fuera de rango (15), lo que provoca la excepción. En el bloque catch, se maneja la excepción asignando "unknown" a monthName y mostrando un mensaje de error en la consola.
  */
  