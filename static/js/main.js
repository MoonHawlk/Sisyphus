function sendMessage() {
    const messageInput = document.getElementById('message');
    const message = messageInput.value.trim();

    if (message !== '') {
        // Exibir símbolo de Loading
        const messagesDiv = document.getElementById('messages');

        // Criar container para o símbolo de Loading e o texto "Pensando..."
        const loadingContainer = document.createElement('div');
        loadingContainer.classList.add('loading-container');

        // Criar símbolo de Loading
        const loadingSymbol = document.createElement('div');
        loadingSymbol.classList.add('loading-symbol');
        loadingContainer.appendChild(loadingSymbol);

        // Criar texto "Pensando..."
        const thinkingText = document.createElement('div');
        thinkingText.textContent = 'Pensando...';
        loadingContainer.appendChild(thinkingText);

        messagesDiv.appendChild(loadingContainer);

        messageInput.value = '';

        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remover símbolo de Loading
            messagesDiv.removeChild(loadingContainer);

            // Adicionar mensagem recebida
            const newMessage = document.createElement('div');
            newMessage.textContent = data.response;
            messagesDiv.appendChild(newMessage);

            // Limpar barra de perguntas
            messageInput.value = '';
        })
        .catch(error => console.error('Error:', error));
    }
}
