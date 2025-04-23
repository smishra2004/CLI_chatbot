
# CLI-based chat application using Gemini API

This is a simple command line interface based chat application built using python and Gemini API where a user can interact with the chat bot by sending messages and recieving intelligent responses from the Gemini Language model.


## Key Features
 1. Users can type messages and get intelligent, conversational replies from the Gemini language model using the CLI.

2. The app detects when you want to end the chat using phrases like:

   bye, exit, end chat, or i want to leave

3. Before you exit, the bot asks for review and rating, your response is structured and extracted using Gemini’s Function Calling feature. Also handles invalid and empty responses. 

4. Your review and rating are saved in a file called feedback.txt in a readable format.

5. All messages (both user's and the bot’s) are automatically saved in chat_history.txt for future reference.
## Getting Started
1. Clone the repository to your local machine.
2. Install python version 3.12.3

3. Create a virtual environment and activate it

```python -m venv venv```

```venv\Scripts\activate``` 

4. Install google-generativeai package to interact with gemini:

```pip install google-generativeai ```

5. Gemini API key setup:

```GOOGLE_API_KEY = "YOUR_API_KEY_HERE"```

 Get your free Gemini API key here:
 https://aistudio.google.com/app/apikey
 
   a. Click on "Get API Key" or navigate to the API Keys section.
   
   b. Choose "Create API Key".
   
   c. Copy the generated key to your clipboard.
   
   6. Run the application by launching the chatbot from your teminal:

 ```python cli_chat.py```

8. Your CLI-based chatbot is ready to use.


    
## Tech Stack
1. Python version 3.12.3
2. API: Google Gemini(Text Generation+Function Calling)
3. File I/O for saving review, chat history and rating

## Example Chat Session

![Screenshot 2025-04-22 232440](https://github.com/user-attachments/assets/1856bd57-6a7f-4711-8325-dfe030438996)


![Screenshot 2025-04-22 232632](https://github.com/user-attachments/assets/3c2bbf2f-427b-4abe-95dd-a993eeade52b)

 
