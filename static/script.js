document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const themesDiv = document.getElementById("themes");

    // Charger les thèmes au démarrage
    loadThemes();

    // Envoyer un message avec Entrée
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    // Envoyer un message avec le bouton
    sendBtn.addEventListener("click", sendMessage);

    // Charger les thèmes
    function loadThemes() {
        fetch("/themes")
            .then((response) => response.json())
            .then((data) => {
                themesDiv.innerHTML = "";
                data.themes.forEach((theme) => {
                    const button = document.createElement("button");
                    button.textContent = theme;
                    button.addEventListener("click", () => {
                        userInput.value = theme;
                        loadThemes(); // Charger de nouveaux thèmes
                    });
                    themesDiv.appendChild(button);
                });
            });
    }

    // Envoyer un message au chatbot
    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            appendMessage("user-message", message);
            fetch("/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ question: message }),
            })
                .then((response) => response.json())
                .then((data) => {
                    appendMessage("bot-message", data.answer);
                });
            userInput.value = "";
        }
    }

    // Ajouter un message au chat
    function appendMessage(className, text) {
        const div = document.createElement("div");
        div.className = `message ${className}`;
        div.textContent = text;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
