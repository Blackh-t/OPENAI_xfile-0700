import os
import subprocess
import warnings

import openai  # Import OpenAI library

from data import DATA

# ANSI color codes for colored output
LIGHT_BLUE = "\033[38;2;173;216;230m"
RESET = "\033[0m"


# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Model configurations
EMBEDDING_MODEL = "text-embedding-ada-002"
LLM = "gpt-4o-mini"


def find_chat(file_name: str) -> str:
    content = ""

    # Check if chat name is defined
    for filename in os.listdir("chatlog/"):
        if filename == file_name + ".txt":
            print("Resume old chat: " + file_name)

            # Fetch
            with open("chatlog/" + filename, "r") as file:
                content = file.read()
    return content


def store_chat(file_name: str, chat: str) -> None:
    # Save chat
    path = "chatlog/"
    filename = path + file_name
    with open(filename, "w") as file:
        # Skriver innholdet av variabelen til filen
        file.write(chat)
        print("Chat saved")


def TTS(text: str) -> None:
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="echo",
        input=text,
    )
    warnings.filterwarnings("ignore")
    response.stream_to_file("speech.mp3")

    subprocess.Popen(
        ["mpg123", "speech.mp3"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main():
    """
    Main function to interact with the user and generate philosophy-related questions
    using OpenAI's chat completion model.
    """
    # Input from the user
    chat_name = input("Enter chat name: ")
    content = find_chat(chat_name)

    user_input = (
        "Velg et tilfelle tema og forsatt på tidligere samtale hvis det finnes: "
        + content
    )

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

        # speech
        TTS(ai_response)

        # Update Memory
        user_input += ai_response + "\n"

        # Get new input
        user_feedback = input("Input (type 'new' to reset, or add comments): ")

        # Reset memory buffer if input == "new"
        if user_feedback == "new":
            store_chat(chat_name + ".txt", user_input)
            user_input = ""
        else:
            user_input += "\nInput: " + user_feedback


if __name__ == "__main__":
    main()
