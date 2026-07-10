while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hi!")
    elif message == "how are you":
        print("Bot: I'm fine, thanks!")
    elif message == "bye":
        print("Bot: Goodbye!")
    elif message == "what can you do?":
        print("Bot: I can answer simple questions and chat with you.")
    elif message == "what is python?":
        print("Bot: Python is a popular programming language.")
    elif message == "can you help me":
        print("Bot: Of course! I'll do my best.")
    elif message == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")
    elif message == "what is machine learning":
        print("Bot: Machine learning is a branch of AI that enables computers to learn from data.")
    elif message == "what is your hobby":
        print("Bot: My hobby is chatting with people.")
    elif message == "i love python":
        print("Bot: That's awesome! Python is a great language.")
    elif message == "can you sing":
        print("Bot: Sorry, I can only chat.")
    elif message == "can you dance":
        print("Bot: I wish I could!")
    elif message == "see you":
        print("Bot: See you soon! Take care.")
    elif message == "Thank you":
        print("Bot: You're welcome")
        break
    else:
        print("Bot: I don't understand.")
