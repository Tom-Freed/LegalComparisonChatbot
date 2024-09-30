import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=r'gemini.env')
api_key = os.getenv("API_KEY")

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a legal expert that compares legal principles, cases, or statutes between English law and American law. The user will input a legal topic or case, and you should generate a comparison between how the issue is treated under both legal systems. You should retrieve and cite relevant case summaries or legal principles from both jurisdictions, summarise the key similarities and differences in legal treatment and provide insights or potential challenges in applying principles from one jurisdiction to another."
    )
chat = model.start_chat()

# Ask the model to generate a few example topics for the user
initial_prompt = "Please suggest two one sentence examples of prompts users could suggest of legal topics comparing English and American law. Your response should only include the examples, no explantion or summary of this prompt."

# Generate the model's suggestions
suggestion_response = chat.send_message(initial_prompt)

# Welcome message with model-generated suggestions
print("""Hello, I am a legal chatbot aimed at comparing legal principles, cases, or statutes between English law and American law.

Please enter a topic or case you are interested in finding out more about.

Here are a couple of examples of topics you could explore:
""")
print(f"{suggestion_response.text}\n")

print("Type 'exit' or 'quit' to end the conversation.\n")

while True:
    # Get user input from the terminal
    user_input = input("User: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # Send the user's message to the chat model and get the response
    response = chat.send_message(
        user_input,
        generation_config=genai.types.GenerationConfig(temperature=0)
    )

    # Print the chatbot's response
    print(f"Chatbot: {response.text}\n")