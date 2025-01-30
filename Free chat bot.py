print("Hi, Wellcome to free_chat_bot, how can i help you?")
while True:
    user_input = input("You: ").lower()  # Convert input to lowercase

    if user_input == "hello":
        print("Free_chatbot: Hello! How are you?")
    elif user_input == "how are you?":
        print("Free_chatbot: I'm a Free Chatbot program, but I’m doing well. Thank you!")
    elif user_input == "bye":
        print("Free_chatbot: Goodbye! Have a great day!")
        break  # Exit loop when user says "bye"
    elif user_input == "i am fine":
        print("Free_chatbot: That's great!")
    else:
        print("Free_chatbot: Sorry, I didn't understand that.")
