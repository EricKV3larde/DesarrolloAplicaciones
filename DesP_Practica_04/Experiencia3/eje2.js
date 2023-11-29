//Captura de Excepciones Personalizadas
// Define una excepción personalizada llamada InvalidDayNo
function InvalidDayNo(message) {
    this.message = message;
    this.name = 'InvalidDayNo';
  }
  
  // Modifica la función getDayName para lanzar InvalidDayNo cuando el número de día está fuera de rango
  function getDayName(day) {
    if (day < 1 || day > 7) {
      throw new InvalidDayNo('El número de día es inválido');
    }
  
    const daysOfWeek = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
    return daysOfWeek[day - 1];
  }
  
  try {
    // Intenta obtener el nombre de un día con un número fuera de rango
    console.log(getDayName(8)); // Esto debería lanzar la excepción InvalidDayNo
  } catch (e) {
    // Maneja la excepción InvalidDayNo
    console.error(e.message, e.name); // Debería mostrar "El número de día es inválido InvalidDayNo"
  }
  