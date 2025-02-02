/*este ezs el efecto rebote del logo de indart*/
// Seleccionar el logo
const logo = document.getElementById('logoRebote');

// Función para el efecto rebote
function iniciarRebote() {
    logo.style.animation = "rebote 1.5s ease infinite";
}

// Agregar la animación al cargar la página
window.addEventListener('load', iniciarRebote);

// Agregar los estilos de la animación
const estiloAnimacion = document.createElement("style");
estiloAnimacion.textContent = `
     @keyframes rebote {
         0%, 25%, 55%, 85%, 100% {
             transform: translateY(0);
         }
         40% {
             transform: translateY(-30px);
         }
         60% {
             transform: translateY(-15px);
         }
     }
 `;
document.head.appendChild(estiloAnimacion);