print("Bot: Hello! I am your AI Assistant ")

while True:

    user = input("You: ").lower()

    if user in ["hi","hello","hey","hy"]:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am Ume AI Assistant.")

    elif "how are you" in user:
        print("Bot: I am great. Thanks for asking!")

    elif "study" in user:
        print("Bot: Keep learning and improving!")

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs ")

    elif user in ["bye","exit","quit","by"]:
        print("Bot: Goodbye! Have a nice day ")
        break

    else:
        print("Bot: Sorry, I don't understand.")