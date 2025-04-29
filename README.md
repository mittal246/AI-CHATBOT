
# AI-POWERED CALL CENTRE INTELLIGENCE CHATBOT

AI Call Center is an interactive and professional call center chatbot application designed to handle customer queries effectively. It features both text-based and voice-based interactions, leveraging AI-powered conversational capabilities to deliver efficient and empathetic responses.


## Features

- Text Chat Interface: Seamlessly interact with the chatbot through a text-based interface.
- Voice Chat Functionality: Enable voice-based conversations for a more natural communication experience.
- Memory-Powered Conversations: Retain conversation history to provide contextually relevant and continuous interactions.
- Text-to-Speech (TTS): Optional feature to convert chatbot responses to audio for enhanced accessibility.
- Streamlit-Powered UI: Clean and intuitive user interface built with Streamlit.



## Tech Stack

- Backend:- **Python**
- **Langchain** for managing the conversational AI logic.
- **Google Generative AI** for advanced natural language processing.
- **SpeechRecognition** for voice input handling.
- **pyttsx3** for converting text responses to speech
- Frontend:- **Streamlit**


## Installation
#### 1. Clone the repository

```bash
  git clone https://github.com/mittal246/AI-CHATBOT.git
  cd AI-CHATBOT
```
#### 2. Set up virtual environment
```bash
python3 -m venv env
.\env\Scripts\activate  # On Mac:source env/bin/activate
```
#### 3. Install dependencies
```bash
pip install -r requirements.txt
```
#### 4. Set Up Environment Variables: 
Create a .env file in the root directory with the following content:
```bash
GOOGLE_KEY= your_api_key
```
#### 5. Run the application
```bash
streamlit run backend.py
```

    
## Usage
### Text Chat
- Start the application and navigate to the Text Chat option from the sidebar.
- Type your queries in the input box, and the chatbot will respond in real-time.

### Voice Chat
- Select the Voice Chat option from the sidebar.
- Click the "Start Recording" button and speak into your microphone.
- The chatbot will process your query and provide a response. Optionally, enable the Voice Response checkbox for audio feedback.

### Additional options
- Use the Clear Conversation button in the sidebar to reset the chat history.

## File Structure

```bash
.
├── backend.py             # Streamlit app entry point
├── chatbot.py             # Chatbot logic and AI integration
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
