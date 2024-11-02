import pyttsx3
import cv2
from modules import voice_recognition, gesture_recognition, object_detection
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize Text-to-Speech Engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # Set speaking speed

def speak(text):
    """Speak the provided text using TTS."""
    print(f"Robot says: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def handle_command(command):
    """Handle voice or gesture commands."""
    if "identify object" in command:
        speak("Starting object detection...")
        object_detection.start_detection()  # Call the object detection module

    elif "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "exit" in command or "quit" in command:
        speak("Shutting down the robot assistant.")
        exit()

    else:
        speak("Unknown command, please try again.")

def main():
    print("Starting the robot assistant...")
    speak("Hello, I am your assistant. Listening for commands.")

    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)  # 0 is the default camera

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Listen for a command
        command = voice_recognition.listen_for_command()
        
        if command:
            print(f"Command heard: {command}")
            handle_command(command)
        else:
            # Capture frame for gesture recognition
            ret, frame = cap.read()
            if ret:
                gesture = gesture_recognition.detect_gesture(frame)
                print(f"Gesture recognized: {gesture}")

                if gesture == "Open Hand":
                    speak("I see an open hand. How can I assist?")
                elif gesture == "Closed Fist":
                    speak("Fist detected. Initiating object detection.")
                    object_detection.start_detection()
                else:
                    print("Unknown gesture.")
        
    # Release resources
    cap.release()

if __name__ == "__main__":
    main()
