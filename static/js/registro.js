window.addEventListener('DOMContentLoaded', function() {
    var registroExitoso = document.getElementById('cuadro-exito').getAttribute('data-registro-exitoso');
    if (registroExitoso === 'True') {
      var cuadroExito = document.getElementById('cuadro-exito');
      cuadroExito.classList.remove('oculto');
    }
  });
  
  function ocultarCuadroExito() {
    var cuadroExito = document.getElementById('cuadro-exito');
    cuadroExito.classList.remove('exito');
    cuadroExito.classList.add('oculto');
  }
  