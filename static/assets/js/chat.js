  // Predefined questions and answers
  const faq = [
    { question: "hai", answer: "Hai How can i help you ?" },
    { question: "hello", answer: "Hai How can i help you ?" },
    { question: "hi..", answer: "Hai How can i help you ?" },
    { question: "Hi..", answer: "Hai How can i help you ?" },
    { question: "Hi", answer: "Hai How can i help you ?" },
    { question: "goodbye", answer: "Talk to you later!" },
    { question: "nice talking to you!", answer: "I am glad I could help" },

    
    // Add more question-answer pairs here
  ];

  // Get necessary DOM elements
  const userInput = document.getElementById("chatbox-input");
  const sendBtn = document.getElementById("send-btn");
  const chatMessages = document.getElementById("chat-messages");
  const chatMessageBox = document.getElementById("chat-message-box");
  var isUserMessage = true

  // Function to display a message in the chat box
  function displayMessage(message) {
    const messageElement = document.createElement("div");
    messageElement.className = "message";
    messageElement.textContent = message;

    if (isUserMessage) {
      messageElement.classList.add("user-message");
      isUserMessage = false
     
    } else {
      messageElement.classList.add("bot-message");
      isUserMessage = true
     
    }
    
    chatMessages.appendChild(messageElement);
    chatMessageBox.scrollTop = chatMessageBox.scrollHeight;
    
  }

  // Event listener for send button click
  sendBtn.addEventListener("click", function () {
    console.log('User question..');
    const question = userInput.value.trim();
    userInput.value = ""; // Clear the input field

    if (question !== "") {
      displayMessage(question); // Display user question

      // Search for a matching question in the faq array
      const matchingQuestion = faq.find((entry) => entry.question.toLowerCase() === question.toLowerCase());
      if (matchingQuestion) {
        displayMessage(matchingQuestion.answer); // Display the corresponding answer
      } else {
        displayMessage("Please contact Us for more details.."); // Display default response
        isUserMessage = false
        displayMessage("Tel: +91 9074 156 818"); // Display default response
      }
    }
  });

  // Enter key press
userInput.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
      // Trigger the button element with a click
      sendBtn.click();
    }
  });