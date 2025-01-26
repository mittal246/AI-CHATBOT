import io
import streamlit as st
from chatbot import Chatbot
import speech_recognition as sr
import pyttsx3
# import sounddevice as sd
# import numpy as np

chatbot = Chatbot()

st.set_page_config(
    page_title="AI-POWERED CHATBOT",
    page_icon="🤖",
    layout="centered"
)
# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_page" not in st.session_state:
        st.session_state.current_page = "chat"
    if "enable_voice_response" not in st.session_state:
        st.session_state.enable_voice_response = False

def play_text_to_speech_streamlit(text):
    audio_fp = io.BytesIO()
    tts_engine.save_to_file(text,'temp_audio.mp3')
    tts_engine.runAndWait()
    # Read the saved file into memory for Streamlit playback
    with open("temp_audio.mp3", "rb") as audio_file:
        audio_fp.write(audio_file.read())
    audio_fp.seek(0)
    st.audio(audio_fp, format="audio/mp3")

recognizer = sr.Recognizer()
# def record_audio(duration=5, sample_rate=16000):
#     print("Listening...")
#     audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
#     sd.wait()  # Wait until the recording is finished
#     print("Recording complete!")
#     return np.squeeze(audio_data)

# # Use recorded audio with speech_recognition
# audio_data = record_audio()
# try:
#     audio_text = recognizer.recognize_google(sr.AudioData(audio_data.tobytes(), 16000, 2))
#     print("You said:", audio_text)
# except Exception as e:
#     print("Error:", e)

def chat_page():
    st.title("AI-POWERED CHATBOT 🤖")
    st.success("What can I help with?")
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Enter the text here"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Response from chatbot
        with st.chat_message("assistant"):
            with st.spinner("Generating output..."):
                response = chatbot.chat(prompt)
                if response:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

                    # Check if voice response is enabled
                    if st.session_state.enable_voice_response:
                        play_text_to_speech_streamlit(response)

def voice_conversation_page():
    st.title("Voice Chat 🗣")
    st.write("Click the button below and start speaking.")

    
    
    # Placeholder for status
    status_placeholder = st.empty()
    if st.button("Start Speaking....🎤"):
        listening_message = status_placeholder.info("Listening...🦻")
        
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=10)
                listening_message.empty()
                
                try:
                    query = recognizer.recognize_google(audio)
                    
                    st.chat_message("user").markdown(query)
                    st.session_state.messages.append({"role": "user", "content": query})
                    
                    with st.chat_message("assistant"):
                        with st.spinner("Generating response..."):
                            response = chatbot.chat(query)
                            if response:
                                st.markdown(response)
                                st.session_state.messages.append({"role": "assistant", "content": response})

                                # Check if voice response is enabled
                                if st.session_state.enable_voice_response:
                                    play_text_to_speech_streamlit(response)
                
                except sr.UnknownValueError:
                    status_placeholder.error("Sorry, I could not understand the audio.")
                except sr.RequestError as e:
                    status_placeholder.error(f"Error with speech recognition service: {e}")
                
        except Exception as e:
            status_placeholder.error(f"An error occurred: {str(e)}")
                                
def main():
    initialize_session_state()

    # Sidebar
    with st.sidebar:
        st.markdown("""
            ## Available Commands:
            - Speak or write 'quit' to exit
            - Speak or write 'clear' to clear history
            - Speak or write 'type' to use keyboard
            - Speak or write 'voice' to use voice
            """)
        st.header("Settings")
        if st.button("Text Conversation"):
            st.session_state.current_page = "chat"
            st.rerun()
        
        if st.button("Voice Conversation"):
            st.session_state.current_page = "voice"
            st.rerun()

        st.session_state.enable_voice_response = st.checkbox("Enable voice response", value=st.session_state.enable_voice_response)
        
        if st.button("Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
    
    # Main content
    if st.session_state.current_page == "voice":
        voice_conversation_page()
    else:
        chat_page()

if __name__ == "__main__":
    main()
