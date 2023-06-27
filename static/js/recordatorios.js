// Obtener referencias a elementos del DOM
const reminderForm = document.getElementById('reminder-form');
const reminderList = document.getElementById('reminder-list');

// Manejar el envío del formulario
reminderForm.addEventListener('submit', function(event) {
  event.preventDefault();

  // Obtener valores del formulario
  const medicineName = document.getElementById('medicine-name').value;
  const dosage = document.getElementById('dosage').value;
  const reminderTime = document.getElementById('reminder-time').value;

  // Crear un nuevo elemento de recordatorio
  const reminderItem = document.createElement('div');
  reminderItem.classList.add('reminder-item');
  reminderItem.innerHTML = `
    <h3>${medicineName}</h3>
    <p>Dosis: ${dosage}</p>
    <p>Hora del recordatorio: ${reminderTime}</p>
  `;

  // Agregar el nuevo elemento al DOM
  reminderList.appendChild(reminderItem);

  // Limpiar el formulario
  reminderForm.reset();
});
