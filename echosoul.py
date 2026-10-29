
import os
import wave
import tempfile

import pyaudio
import whisper
import pyttsx3


# ==========================================
# EchoSoul - Simple Voice Assistant
# ==========================================

SAMPLE_RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5
MICROPHONE_INDEX = 1


# ==========================================
# Initialize Whisper and Text-to-Speech
# ==========================================

print("Loading Whisper model...")
model = whisper.load_model("small")

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(message):
    """Print and speak EchoSoul's response."""
    print(f"EchoSoul: {message}")
    engine.say(message)
    engine.runAndWait()


# ==========================================
# Initialize Microphone
# ==========================================

audio = pyaudio.PyAudio()


def listen():
    """Record a voice command for five seconds."""
    filename = os.path.join(
        tempfile.gettempdir(),
        "echosoul_input.wav"
    )

    print("\nEchoSoul is listening. Speak now!")

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        input_device_index=MICROPHONE_INDEX,
        frames_per_buffer=CHUNK,
    )

    frames = []

    try:
        for _ in range(int(SAMPLE_RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )
            frames.append(data)
    finally:
        stream.stop_stream()
        stream.close()

    with wave.open(filename, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(
            audio.get_sample_size(pyaudio.paInt16)
        )
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(b"".join(frames))

    return filename


# ==========================================
# Process Voice Commands
# ==========================================

def respond(text):
    """Respond to supported voice commands."""
    command = text.lower().strip()
    print(f"You said: {text}")

    if not command:
        speak("I didn't catch that. Please try again.")

    elif any(
        word in command.split()
        for word in ["hello", "hi", "hey"]
    ):
        speak("Hello! How can I help you?")

    elif "who are you" in command:
        speak("I am EchoSoul, your voice assistant.")

    elif "how are you" in command:
        speak("I'm doing well! Thanks for asking.")

    elif any(
        word in command.split()
        for word in ["exit", "quit", "stop", "goodbye"]
    ):
        speak("Goodbye! See you later.")
        return False

    else:
        speak("Sorry, I don't understand that command yet.")

    return True


# ==========================================
# Main Program
# ==========================================

try:
    print("\nEchoSoul is ready!")
    print("Try saying:")
    print("- Hello")
    print("- Who are you?")
    print("- How are you?")
    print("- Exit")

    while True:
        audio_file = listen()

        result = model.transcribe(
            audio_file,
            language="en",
            fp16=False,
            temperature=0,
            condition_on_previous_text=False,
        )

        if not respond(result["text"]):
            break

finally:
    audio.terminate()
    engine.stop()
    print("\nEchoSoul stopped.")
