import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("Gemini connected successfully!")

chat_history = []

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot: Bye!")
        break

    chat_history.append({
        "role": "user",
        "parts": [{"text": question}]
    })

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=chat_history
    )

    print("AI:", response.text)

    chat_history.append({
        "role": "model",
        "parts": [{"text": response.text}]
    })
