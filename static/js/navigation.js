document.addEventListener('DOMContentLoaded', function() {
    // Elementos principales
    const asistenteBtn = document.getElementById('asistente-flotante');
    const navPanel = document.getElementById('nav-panel');
    const chatPanel = document.getElementById('chat-panel');
    const closeNav = document.getElementById('close-nav');
    const closeChat = document.getElementById('close-chat');
    const openChatBtn = document.getElementById('open-chat');
    const backToNavBtn = document.getElementById('back-to-nav');
    const chatContent = document.getElementById('chat-content');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-chat');

    // Mostrar panel de navegación
    asistenteBtn.addEventListener('click', () => {
        navPanel.style.display = 'block';
        chatPanel.style.display = 'none';
    });

    // Cerrar panel de navegación
    closeNav.addEventListener('click', () => {
        navPanel.style.display = 'none';
    });

    // Abrir chat desde navegación
    openChatBtn.addEventListener('click', () => {
        navPanel.style.display = 'none';
        chatPanel.style.display = 'block';
        addMessage('¡Hola! Soy tu Cinematic Assistant. ¿En qué puedo ayudarte hoy?', 'assistant');
    });

    // Volver a navegación desde chat
    backToNavBtn.addEventListener('click', () => {
        chatPanel.style.display = 'none';
        navPanel.style.display = 'block';
    });

    // Cerrar chat
    closeChat.addEventListener('click', () => {
        chatPanel.style.display = 'none';
    });

    // Función para añadir mensaje al chat
    function addMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `mb-3 p-3 rounded ${sender === 'user' ? 'bg-primary bg-opacity-25' : 'bg-dark bg-opacity-50'}`;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'd-flex align-items-start';

        if (sender === 'assistant') {
            contentDiv.innerHTML = `
            <div class="me-2">
            <i class="bi bi-robot fs-4 text-primary"></i>
            </div>
            <div>
            <strong>C.A:</strong> ${message}
            </div>
            `;
        } else {
            contentDiv.innerHTML = `
            <div class="me-2">
            <i class="bi bi-person-circle fs-4 text-info"></i>
            </div>
            <div>
            <strong>Tú:</strong> ${message}
            </div>
            `;
        }

        messageDiv.appendChild(contentDiv);
        chatContent.appendChild(messageDiv);

        // Scroll al último mensaje
        chatContent.scrollTop = chatContent.scrollHeight;
    }

    // Función para enviar mensaje al servidor
    async function sendMessage(message) {
        try {
            const response = await fetch("{% url 'assistant:chat_api' %}", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();

            if (data.response) {
                addMessage(data.response, 'assistant');
            } else {
                addMessage('Lo siento, ocurrió un error. Inténtalo de nuevo.', 'assistant');
            }
        } catch (error) {
            addMessage('Error de conexión con el asistente.', 'assistant');
        }
    }

    // Enviar mensaje al hacer clic en enviar o presionar Enter
    sendBtn.addEventListener('click', () => {
        const message = chatInput.value.trim();
        if (message) {
            addMessage(message, 'user');
            sendMessage(message);
            chatInput.value = '';
        }
    });

    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const message = chatInput.value.trim();
            if (message) {
                addMessage(message, 'user');
                sendMessage(message);
                chatInput.value = '';
            }
        }
    });
});
