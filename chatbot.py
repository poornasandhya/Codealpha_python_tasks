while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hi!")
    elif message == "how are you":
        print("Bot: I'm fine, thanks!")
    elif message == "bye":
        print("Bot: Goodbye!")
    elif message == "What can you do?":
        print("Bot: I can answer simple questions and chat with you.")
    elif message == "What is python?":
        print("Bot: Python is a popular programming language.")
    elif message == "Thank you":
        print("Bot: You're welcome")
        break
    else:
        print("Bot: I don't understand.")
