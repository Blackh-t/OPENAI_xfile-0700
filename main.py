import openai  # Import OpenAI library
from data import DATA

# ANSI color codes for colored output
LIGHT_BLUE = "\033[38;2;173;216;230m" 
RESET = "\033[0m"  


OPENAI_API_KEY = ""  # Add your API key here

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Model configurations
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM = "gpt-4o-mini"

def main():
    """
    Main function to interact with the user and generate philosophy-related questions 
    using OpenAI's chat completion model.
    """
    # Input from the user
    user_input = input("Enter a string to start the conversation: ")

    # Continuous loop for interactive Q&A
    while True:
        # Generate AI response
        chat_completion = client.chat.completions.create(
            model=LLM,
            messages=[
                {
                    "role": "system",
                    "content": DATA,
                },
                {"role": "user", "content": user_input},
            ],
        )
        # Extract the AI's response
        ai_response = chat_completion.choices[0].message.content
        print(f"\n\n{LIGHT_BLUE}{ai_response}{RESET}\n\n")

        # Update Memory
        user_input += ai_response + "\n"

        # Get new input
        user_feedback = input("Input (type 'new' to reset, or add comments): ")

        # Reset memory buffer if input == "new"
        if user_feedback.lower() == "new":
            user_input = ""
        else:
            user_input += user_feedback

if __name__ == "__main__":
    main()

