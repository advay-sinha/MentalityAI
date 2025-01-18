const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const micBtn = document.getElementById('mic-btn');

// Base URL for API endpoints (update if hosted on a specific domain)
const BASE_API_URL = "http://localhost:5000/api"; // Update to your backend's base URL if deployed

// Function to add a new message to the chat container
function appendMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender === 'bot' ? 'bot-message' : 'user-message');

    if (sender === 'bot') {
        const botLogo = document.createElement('div');
        botLogo.classList.add('bot-logo');
        botLogo.textContent = 'AI';
        messageDiv.appendChild(botLogo);
    }

    const textDiv = document.createElement('div');
    textDiv.textContent = content;
    messageDiv.appendChild(textDiv);

    chatContainer.appendChild(messageDiv);

    // Trigger animation
    setTimeout(() => messageDiv.classList.add('show'), 10);

    // Scroll to the latest message
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Display the default bot message when the page loads
window.addEventListener('DOMContentLoaded', () => {
    appendMessage('Hello! How can I assist you today?', 'bot');
});

// Handle user input and send button
sendBtn.addEventListener('click', () => {
    const userMessage = userInput.value.trim();

    if (userMessage) {
        appendMessage(userMessage, 'user');
        userInput.value = ''; // Clear input field
        sendMessageToChatbot(userMessage);
    }
});

// Allow pressing Enter to send message
userInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendBtn.click();
    }
});

// Handle microphone input for speech-to-text
micBtn.addEventListener('click', async () => {
    try {
        appendMessage('Listening...', 'bot');
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const mediaRecorder = new MediaRecorder(stream);
        const audioChunks = [];

        mediaRecorder.ondataavailable = event => audioChunks.push(event.data);
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            const formData = new FormData();
            formData.append('audio', audioBlob, 'audio.wav');

            try {
                const response = await fetch(`${BASE_API_URL}/speech-to-text`, {
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();
                if (data.transcript) {
                    appendMessage(data.transcript, 'user');
                    sendMessageToChatbot(data.transcript);
                } else {
                    appendMessage('Sorry, I couldn’t recognize any speech.', 'bot');
                }
            } catch (err) {
                appendMessage('Error processing speech. Please try again.', 'bot');
                console.error('Failed to send audio:', err);
            }
        };

        mediaRecorder.start();
        setTimeout(() => mediaRecorder.stop(), 3000); // Record for 3 seconds
    } catch (err) {
        appendMessage('Error: Unable to access the microphone.', 'bot');
        console.error('Microphone access error:', err);
    }
});

// Function to send message to chatbot
async function sendMessageToChatbot(userInput) {
    try {
        const response = await fetch(`${BASE_API_URL}/chatbot-response`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_input: userInput }),
        });

        const data = await response.json();
        if (data.response) {
            appendMessage(data.response, 'bot');
        } else {
            appendMessage('Error: Unable to get a response.', 'bot');
            console.error('Error:', data.error);
        }
    } catch (err) {
        appendMessage('Error: Unable to connect to the chatbot.', 'bot');
        console.error('Failed to communicate with the chatbot:', err);
    }
}