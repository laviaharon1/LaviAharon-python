"""
SMART CHATBOT PROJECT
=====================

Student Name: Lavi Aharon
Bot Name: Robi
Bot Purpose: Study Helper
"""
import random

bot_name = "Robi"

def print_seperator():
    print("=" * 50)

def print_bot(message):
    print(f"🤖 {bot_name}: {message}")

def input_bot(message):
    return input(f"🤖 {bot_name}: {message} ")

def welcome_user():
    greetings = [
        f"Hello! I'm {bot_name}, your study helper.",
        f"Hi there! I'm {bot_name}, your friendly study companion.",
        f"Hey! I'm {bot_name}, here to help you with your studies."
    ]
    print_bot(random.choice(greetings))

def goodbye_user():
    goodbyes = [
        "Goodbye! Happy studying!",
        "See you later! Keep up the great work!",
        "Take care! Don't forget to review your notes!"
    ]
    print_bot(random.choice(goodbyes))

def tell_joke():
    jokes = [
        "Why did the math book look sad? Because it had too many problems.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the student eat his homework? Because the teacher said it was a piece of cake!"
    ]
    print_bot(random.choice(jokes))


def print_help():
    help_message = (
        "Here are some commands you can use:\n"
        "- 'help': Show this help message\n"
        "- 'joke': Hear a joke to lighten the mood\n"
        "- 'goodbye': End our chat session\n"
    )
    print_bot(help_message)

def greet_user():
    print_seperator()
    welcome_user()
    user_name = input("What is your name? ")
    print(f"Nice to meet you, {user_name}!")
    print_seperator()
    return user_name

def calculator():
    expression = input("Enter a math problem: ")
    try:
        result = eval(expression)
        print_bot(f"The answer is {result}")
    except:
        print_bot("I couldn't calculate that.")

def play_rock_paper_scissors():
    print_bot("Let's play Rock, Paper, Scissors! Type 'rock', 'paper', or 'scissors' to play.")
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice not in choices:
            print_bot("Please choose 'rock', 'paper', or 'scissors'.")
            continue

        bot_choice = random.choice(choices)
        print_bot(f"I chose {bot_choice}.")

        if user_choice == bot_choice:
            print_bot("It's a tie! Let's play again.")
        elif (user_choice == "rock" and bot_choice == "scissors") or (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
            print_bot("Congratulations! You win!")
            break
        else:
            print_bot("I win! Better luck next time.")
            break
def play_guessing_game():
    print_bot("Let's play a guessing game! I'm thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = input("What's your guess? ")

        if not guess.isdigit() or not 1 <= int(guess) <= 20:
            print_bot("Please enter a valid number between 1 and 20.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == number:
            print_bot("Congratulations! You guessed the number!")
            break
        elif guess < number:
            print_bot("Too low! Try again.")
        else:
            print_bot("Too high! Try again.")

    print(f"You used {attempts} attempts to guess the number.")

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

    if any(word in message.lower() for word in happy_words):
        print_bot("I'm glad to hear you're feeling good!")
    elif any(word in message.lower() for word in sad_words):
        print_bot("I'm sorry to hear you're feeling sad. Remember, it's okay to have tough days!")
    else:
        print_bot(random.choice(default_responses))

def get_response(message, user_name):
    message_lower = message.lower()
    if "hello" in message_lower or "hi" in message_lower or "hey" in message_lower:
        print_bot(f"Hello {user_name}!")
    elif "how are you" in message_lower:
        print_bot(f"I'm great, {user_name}! How are you?")
    elif "your name" in message_lower or "who are you" in message_lower:
        print_bot(f"My name is {bot_name}.")
    elif "joke" in message_lower or "funny" in message_lower:
        tell_joke()
    elif "game" in message_lower or "play" in message_lower:
        return "game_menu"
    elif "help" in message_lower or "commands" in message_lower:
        print_help()
        print("What else can I help with?")
    elif "calculate" in message_lower or "math" in message_lower:
        calculator()
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
    else:
        analyze_mood(message)

def chat():
    user_name = greet_user()
    print_help()

    while True:
        user_message = input(f"\n{user_name}: ").strip()
        if not user_message:
            print_bot("Please enter a message.")
            continue
        if user_message.lower() in ["goodbye", "bye", "exit", "quit"]:
            goodbye_user()
            print(f"Thanks for chatting with me! Have a great day, {user_name}!")
            break
        response = get_response(user_message, user_name)

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


if __name__ == "__main__":
    chat()