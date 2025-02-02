/* este es el javascript de la openai */

// Función para desplazarse automáticamente al final del chat
function scrollToBottom() {
    const chatContainer = document.getElementById('chat-container');
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Desplazar al final al abrir el modal
const modal = document.getElementById('exampleModal');
modal.addEventListener('shown.bs.modal', function () {
    scrollToBottom();
});

// Desplazar al final al enviar un mensaje
document.getElementById('send-button').addEventListener('click', function () {
    setTimeout(scrollToBottom, 100); // Espera un momento para asegurar que el mensaje ya se agregó
});

/*codigo de openai para el minibot assistant */
$(document).ready(function () {
    // Función para enviar mensaje
    function sendMessage() {
        let userMessage = $('#user-message').val();
        if (userMessage.trim() !== '') {
            // Limpiar el chat-box antes de agregar nuevos mensajes
            $('#chat-box').empty();

            $('#chat-box').append(`<p class="user-message"><strong>Tú:</strong> ${userMessage}</p>`);
            $('#user-message').val('');

            // Desplazarse automáticamente al final del chat
            $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);

            $.ajax({
                type: 'POST',
                url: '/assistant/api/get_response/',
                data: {
                    'message': userMessage,
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function (response) {
                    if (response.reply) {
                        $('#chat-box').append(`<p class="bot-message"><strong>Bot:</strong> ${response.reply}</p>`);
                        $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
                    } else {
                        $('#chat-box').append('<p class="bot-message"><strong>Error:</strong> Algo salió mal.</p>');
                    }
                },
                error: function () {
                    $('#chat-box').append('<p class="bot-message"><strong>Error:</strong> No se pudo conectar con el servidor.</p>');
                }
            });
        }
    }

    // Enviar mensaje al hacer clic en el botón
    $('#send-button').click(function () {
        sendMessage();
    });

    // Enviar mensaje al presionar Enter
    $('#user-message').keypress(function (e) {
        if (e.which === 13) {
            e.preventDefault();
            sendMessage();
        }
    });
});