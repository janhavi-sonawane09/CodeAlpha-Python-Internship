from datetime import datetime


def chatbot():
    print("🤖 Chatbot: Hello! I am your Basic Python Chatbot.")
    print("🤖 Chatbot: Type 'help' to see what I can do.")
    print("🤖 Chatbot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi" or user_input == "hey":
            print("Chatbot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Chatbot: My name is BasicBot.")

        elif user_input == "time":
            current_time = datetime.now().strftime("%I:%M %p")
            print("Chatbot: Current time is", current_time)

        elif user_input == "help":
            print("Chatbot: You can ask me:")
            print("- hello")
            print("- how are you")
            print("- what is your name")
            print("- time")
            print("- bye")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()