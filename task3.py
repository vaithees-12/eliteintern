import nltk
import random
import re

# First-time setup: download required NLTK data
nltk.download('punkt')

# Sample responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    "goodbye": ["Bye!", "Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["Sorry, I didn’t understand that.", "Can you say that again?"]
}

# Function to get intent
def get_intent(user_input):
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "greeting"
    elif re.search(r"\b(bye|goodbye|see you)\b", user_input):
        return "goodbye"
    elif re.search(r"\b(thank|thanks)\b", user_input):
        return "thanks"
    else:
        return "default"

# Chat loop
print("🤖 ChatBot: Hello! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("🤖 ChatBot: Bye! 👋")
        break
    intent = get_intent(user_input)
    response = random.choice(responses[intent])
    print("🤖 ChatBot:", response)
