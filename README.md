# Robot Assistant

This project implements a real-time robot assistant capable of detecting objects, recognizing hand gestures, and responding to voice commands. Built using TensorFlow, OpenCV, Mediapipe, and YOLO, the robot assistant aims to interact seamlessly with users.

## Features

- **Object Detection**: Identifies and classifies objects in real-time using YOLO.
- **Gesture Recognition**: Recognizes hand gestures to trigger specific actions.
- **Voice Recognition**: Listens for voice commands and responds appropriately.
- **Text-to-Speech**: Provides spoken responses to user queries and commands.

## Requirements

To run this project, you will need to install the required Python packages. 

### Installation Steps

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/nawabkh2040/Robo
   cd Robo
   ```
2. **Create A  Virtual Environment** 
     *  You can name your virtual environment anything you prefer
     ```bash
          python -m venv tfod 
          .\tfod\Scripts\activate

     ```
3. **Activate the virtual environment:**
* On Windows:
     ```bash
     .\tfod\Scripts\activate

     ```
     or
* On Mac:
     ```bash
     source tfod/bin/activate

     ```
4. **Install required packages**:
     ```
     opencv-python
     opencv-python-headless
     mediapipe
     tensorflow
     torch
     ultralytics
     pyttsx3
     SpeechRecognition
     pyaudio
     numpy

     ```
     or 
```bash

pip install -r requirements.txt

```
# Usage
1. Ensure your webcam is connected and working.

2. Run the main application:
```bash
python main.py

```
3. The robot assistant will greet you and start listening for commands. You can say commands like:
* "identify object" to start object detection.
* "hello" for a friendly greeting.
* "exit" to shut down the assistant.

# Contributing
If you wish to contribute to this project, please fork the repository and create a pull request with your changes


# Acknowledgments
* Ultralytics: For providing the YOLO implementation.
* TensorFlow: For machine learning framework.
* OpenCV and Mediapipe: For computer vision functionalities.