"""
SMART CHATBOT PROJECT
=====================

Student Name: Lavi Aharon
Bot Name: Robi
Bot Purpose: Study Helper
"""

# Import random so the bot can choose random greetings, jokes, numbers, etc.
import random

# Name of the bot (used in many messages)
bot_name = "Robi"

# Print a visual separator line to make the chat easier to read
def print_seperator():
    print("=" * 50)

# Print a message from the bot
# This keeps all bot messages formatted the same way
def print_bot(message):
    print(f"🤖 {bot_name}: {message}")

# Ask the user for input while showing the bot name first
# Returns the user's input

def input_bot(message):
    return input(f"🤖 {bot_name}: {message} ")

# Show a random welcome message when the program starts

def welcome_user():
    greetings = [
        f"Hello! I'm {bot_name}, your study helper.",
        f"Hi there! I'm {bot_name}, your friendly study companion.",
        f"Hey! I'm {bot_name}, here to help you with your studies."
    ]

    # Choose a random greeting and print it
    print_bot(random.choice(greetings))


# Print a random goodbye message when the user exits the chat

def goodbye_user():
    goodbyes = [
        "Goodbye! Happy studying!",
        "See you later! Keep up the great work!",
        "Take care! Don't forget to review your notes!"
    ]

    print_bot(random.choice(goodbyes))


# Tell the user a random joke

def tell_joke():
    jokes = [
        "Why did the math book look sad? Because it had too many problems.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the student eat his homework? Because the teacher said it was a piece of cake!"
    ]

    print_bot(random.choice(jokes))


# Show the user what commands they can use

def print_help():

    help_message = (
        "Here are some commands you can use:\n"
        "- 'help': Show this help message\n"
        "- 'joke': Hear a joke to lighten the mood\n"
        "- 'goodbye': End our chat session\n"
    )

    print_bot(help_message)


# Ask the user for their name and greet them
# Returns the user's name so the bot can use it later

def greet_user():

    print_seperator()

    # Show welcome message
    welcome_user()

    # Ask user their name
    user_name = input("What is your name? ")

    # Respond using their name
    print(f"Nice to meet you, {user_name}!")

    print_seperator()

    return user_name


# Simple calculator that evaluates math expressions
# Example input: 5 + 5 or 10 / 2

def calculator():

    # Ask user for a math expression
    expression = input("Enter a math problem: ")

    try:
        # Evaluate the expression
        result = eval(expression)

        # Show the result
        print_bot(f"The answer is {result}")

    except:
        # If something goes wrong, show an error
        print_bot("I couldn't calculate that.")


# Rock Paper Scissors game

def play_rock_paper_scissors():

    print_bot("Let's play Rock, Paper, Scissors! Type 'rock', 'paper', or 'scissors' to play.")

    choices = ["rock", "paper", "scissors"]

    while True:

        # Ask the user for their choice
        user_choice = input("Your choice: ").lower()

        # Check if the input is valid
        if user_choice not in choices:
            print_bot("Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Bot randomly chooses rock/paper/scissors
        bot_choice = random.choice(choices)

        print_bot(f"I chose {bot_choice}.")

        # Game result logic
        if user_choice == bot_choice:
            print_bot("It's a tie! Let's play again.")

        elif (user_choice == "rock" and bot_choice == "scissors") or (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
            print_bot("Congratulations! You win!")
            break

        else:
            print_bot("I win! Better luck next time.")
            break


# Number guessing game

def play_guessing_game():

    print_bot("Let's play a guessing game! I'm thinking of a number between 1 and 20.")

    # Bot chooses a random number
    number = random.randint(1, 20)

    attempts = 0

    while True:

        # Ask the user to guess the number
        guess = input("What's your guess? ")

        # Validate input
        if not guess.isdigit() or not 1 <= int(guess) <= 20:
            print_bot("Please enter a valid number between 1 and 20.")
            continue

        guess = int(guess)

        attempts += 1

        # Compare guess to the correct number
        if guess == number:
            print_bot("Congratulations! You guessed the number!")
            break

        elif guess < number:
            print_bot("Too low! Try again.")

        else:
            print_bot("Too high! Try again.")

    # Show how many attempts the user used
    print(f"You used {attempts} attempts to guess the number.")


# Analyze user message to detect mood (happy/sad)

def analyze_mood(message):

    happy_words = ["happy", "good", "great", "fantastic", "awesome"]

    sad_words = ["sad", "bad", "terrible", "awful", "depressed"]

    default_responses = [
        "That's interesting!",
        "Tell me more!",
        "I see...",
        "Cool!",
        "Thanks for sharing!"
    ]

    # Check if message contains happy words
    if any(word in message.lower() for word in happy_words):
        print_bot("I'm glad to hear you're feeling good!")

    # Check if message contains sad words
    elif any(word in message.lower() for word in sad_words):
        print_bot("I'm sorry to hear you're feeling sad. Remember, it's okay to have tough days!")

    # Otherwise respond with a generic response
    else:
        print_bot(random.choice(default_responses))


# Main message response logic
# Determines what the bot should do based on the user message

def get_response(message, user_name):

    message_lower = message.lower()

    # Greeting detection
    if "hello" in message_lower or "hi" in message_lower or "hey" in message_lower:
        print_bot(f"Hello {user_name}!")

    # Small talk
    elif "how are you" in message_lower:
        print_bot(f"I'm great, {user_name}! How are you?")

    # Bot identity
    elif "your name" in message_lower or "who are you" in message_lower:
        print_bot(f"My name is {bot_name}.")

    # Joke request
    elif "joke" in message_lower or "funny" in message_lower:
        tell_joke()

    # Game request
    elif "game" in message_lower or "play" in message_lower:
        return "game_menu"

    # Help command
    elif "help" in message_lower or "commands" in message_lower:
        print_help()
        print("What else can I help with?")

    # Calculator
    elif "calculate" in message_lower or "math" in message_lower:
        calculator()

    # Extra small talk responses
    elif "favorite color" in message_lower:
        print_bot("I think blue is pretty nice!")

    elif "hobbies" in message_lower:
        print_bot("I enjoy chatting with you and helping with your studies!")

    elif "science" in message_lower or "history" in message_lower or "english" in message_lower:
        print_bot("Some school subjects can be tough, but I'm here to help you with any questions you have!")

    elif "music" in message_lower:
        print_bot("I love music! Do you have a favorite band or genre?")

    elif "sports" in message_lower:
        print_bot("Sports are great for staying active! Do you have a favorite team or sport?")

    # If nothing matches, analyze mood
    else:
        analyze_mood(message)


# Main chat loop
# This keeps the conversation running until the user exits

def chat():

    # Get the user's name
    user_name = greet_user()

    # Show help at the start
    print_help()

    while True:

        # Ask user for a message
        user_message = input(f"\n{user_name}: ").strip()

        # Prevent empty input
        if not user_message:
            print_bot("Please enter a message.")
            continue

        # Exit commands
        if user_message.lower() in ["goodbye", "bye", "exit", "quit"]:
            goodbye_user()
            print(f"Thanks for chatting with me! Have a great day, {user_name}!")
            break

        # Get response from bot logic
        response = get_response(user_message, user_name)

        # If the user asked to play a game
        if response == "game_menu":

            print_bot(
                "What would you like to play?\n"
                "1. Guessing Game\n"
                "2. Rock, Paper, Scissors\n"
                "3. Never mind"
            )

            choice = input("Enter choice: ")

            if choice == "1":
                play_guessing_game()

            elif choice == "2":
                play_rock_paper_scissors()

            else:
                print_bot("No problem! Let me know if you want to play something else.")


# Start the program
# This ensures the chat only runs if the file is executed directly

if __name__ == "__main__":
    chat()
