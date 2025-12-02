# Simple response logic for selected questions
def get_response(message):
    message = message.lower()
    
    responses = {
        "hi": "Hi there! How can I help you?",
        "hello": "Hello! Nice to meet you.",
        "how are you": "I'm a chatbot, but I'm doing great! You?",
        "what is your name": "I'm your friendly chatbot.",
        "bye": "Goodbye! Have a great day!"
    }
    
    return responses.get(message, f"You said: {message}")
