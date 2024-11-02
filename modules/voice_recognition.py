import speech_recognition as sr

def listen_for_command():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command heard: {command}")
        return command.lower()  # Convert to lowercase for consistency
    except sr.UnknownValueError:
        print("Could not understand the command.")
        return None
    except sr.RequestError:
        print("Error: Could not request results from the speech recognition service.")
        return None
