import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os
from elevenlabs import play, stream, ElevenLabs
from dotenv import load_dotenv # 1. Import dotenv

# 2. Load the keys from your .env file
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up ElevenLabs client
eleven_client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

r = sr.Recognizer()

def get_response(prompt):
    # Added check to ensure we don't call API with empty text
    if not prompt or prompt.strip() == "":
        return ""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "I'm sorry, I couldn't get a response right now."

def speak(text, voice_id="dRtOp8kfRuFIbDKMu38H"):
    if not text: return # Don't speak if there's no text
    try:
        audio_stream = eleven_client.text_to_speech.stream(
            text=text,
            voice_id=voice_id
        )
        stream(audio_stream)
    except Exception as e:
        print(f"ElevenLabs Error: {e}")

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=1) # Calibrate for your room
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except Exception:
        return ""

def main_loop():
    print("AI Voice Assistant Active. Say 'goodbye' to exit.")
    while True:
        command = listen()
        
        if not command:
            continue
            
        if "goodbye" in command.lower():
            speak("Goodbye! Have a great day.")
            break
        
        response = get_response(command)
        print(f"AI: {response}") # See the text response too
        speak(response)

if __name__ == "__main__":
    main_loop()