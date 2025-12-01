from services.ai_service import ask_gemini

def main():
    print("=== Gemini AI Chatbot ===")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = ask_gemini(user_input)
        print("AI:", reply)

if __name__ == "__main__":
    main()
