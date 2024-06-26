from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environmental variables from a .env file
load_dotenv()

# Access the Google API key from the loaded environment variables
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the generative AI client with the API key
genai.configure(api_key=API_KEY)

# Select the generative AI model to use
model = genai.GenerativeModel('gemini-pro')

# Start a new chat session with an empty history
chat = model.start_chat(history=[])

# Instruction to the model for the style of responses
instruction = "In this chat, respond as if you are explaining to a five-year-old child."

# Enter a loop to continuously take user input and generate responses
while True:
    question = input("You: ")

    # Break the loop if the input is empty
    if question.strip() == '':
        break

    # Send the user's question along with the instruction to the chat model
    response = chat.send_message(instruction + question)

    # Print the bot's response
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')