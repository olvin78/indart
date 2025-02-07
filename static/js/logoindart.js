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


/*esta es la prueba para probar hacer un efecto en las imagenes al hacer click */

// Selecciona todas las imágenes con la clase 'vibration-image'
const images = document.querySelectorAll('.vibration-image');

images.forEach(image => {
    image.addEventListener('click', () => {
        navigator.vibrate(50); // Vibración breve
        image.style.transition = 'transform 0.05s ease';
        image.style.transform = 'translateX(-2px)';

        setTimeout(() => {
            image.style.transform = 'translateX(2px)';
        }, 50);

        setTimeout(() => {
            image.style.transform = 'translateX(0)';
        }, 100);
    });
});
