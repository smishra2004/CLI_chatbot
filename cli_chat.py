import google.generativeai as genai
import os

# Set your Gemini API key
GOOGLE_API_KEY = "YOUR API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Define exit commands to watch for
EXIT_COMMANDS = {"bye", "exit", "end chat", "i want to leave"}

# Helper function to check if user wants to exit
def is_exit_intent(message):
    return message.lower().strip() in EXIT_COMMANDS

# Define the function schema for structured feedback (function calling)
review_function_schema = {
    "name": "capture_feedback",
    "description": "Captures a short review and rating from the user.",
    "parameters": {
        "type": "object",
        "properties": {
            "review": {
                "type": "string",
                "description": "A short review of the chat experience."
            },
            "rating": {
                "type": "integer",
                "description": "A rating from 1 to 5."
            },
        },
        "required": ["review", "rating"]
    }
}

# Initialize Gemini model with function support
chat_model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    tools=[{"function_declarations": [review_function_schema]}]
)

# Start chat session
chat = chat_model.start_chat()

print("🤖 Gemini Chatbot: Hello! I'm ready to chat. (Type 'bye', 'exit', or 'end chat' to leave)\n")

# CLI chat loop
while True:
    user_input = input("You: ")

    if is_exit_intent(user_input):  # User wants to leave
        farewell_prompt = "Before you go, could you leave a short review and a rating (1–5)?"
        print(f"\n🤖 Gemini Chatbot: {farewell_prompt}")

        # Save this final user input + bot farewell to chat history
        try:
            with open("chat_history.txt", "a", encoding="utf-8") as f:
                f.write(f"You: {user_input}\n")
                f.write(f"Gemini: {farewell_prompt}\n\n")
        except Exception as e:
            print("⚠️ Error saving final message:", e)

        # Ask for user input for review and rating
        user_review = input("Your Review: ").strip()
        user_rating = input("Your Rating (1–5): ").strip()

        # Check for empty input
        if not user_review or not user_rating:
            print("\n You left the review or rating blank. Please enter both a review and a rating before exiting.")
            continue

        # Ask Gemini to format review + rating using function calling
        response = chat.send_message(
            f'The user gave this review: "{user_review}" and rating: {user_rating}. '
            f'Please extract this as JSON using the capture_feedback function.'
        )

        feedback_data = None
        # Extract feedback from Gemini's function_call output
        for part in response.parts:
            if hasattr(part, 'function_call'):  # Check if this part contains function call
                function_call_args = part.function_call.args  # Correct way to access arguments
                if function_call_args:
                    feedback_data = function_call_args
                    break


        if function_call_args:
            feedback_data = function_call_args  # Store the arguments as feedback_data
            # Save feedback to file
            with open("feedback.txt", "a") as f:
                f.write("\n--- New Feedback ---\n")
                f.write(f"Review: {feedback_data['review']}\n")
                f.write(f"Rating: {feedback_data['rating']}/5\n")

            print("\nThank you for your feedback! Goodbye! ")
        else:
            print("Sorry, I couldn’t process your review. Please try again later.")

        break  # Exit the chat loop

    # If not exiting, continue chat with Gemini
    response = chat.send_message(user_input)
    bot_reply = response.text
    print("Gemini:", bot_reply)

    # Save chat to chat_history.txt
    try:
        with open("chat_history.txt", "a", encoding="utf-8") as f:
            f.write(f"You: {user_input}\n")
            f.write(f"Gemini: {bot_reply}\n\n")
    except Exception as e:
        print("⚠️ Error saving chat:", e)


