print("===== Welcome to My Chatbot =====")
print("You can chat with the bot.")
print("Type 'exit' to stop the chatbot.\n")

while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif message == "how are you":
        print("Bot: I am doing great!")

    elif message == "what is your name":
        print("Bot: My name is PyBot.")

    elif message == "what can you do":
        print("Bot: I can answer simple questions.")

    elif message == "exit":
        print("Bot: Chat ended. Have a nice day!")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")