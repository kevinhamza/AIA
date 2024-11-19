import speech_recognition as sr
import pyttsx3
import os
import time
import threading

class VoiceAssistant:
    def __init__(self, name="Assistant"):
        self.name = name
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def speak(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def listen(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print(f"{self.name} is listening...")
            audio = self.recognizer.listen(source)
        return audio

    def recognize_speech(self, audio):
        try:
            print("Recognizing...")
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            self.speak("Sorry, I'm having trouble connecting to the service.")
            return None

    def process_command(self, command):
        if command:
            if "hello" in command:
                self.speak(f"Hello, I'm {self.name}, how can I assist you?")
            elif "time" in command:
                self.speak(f"The current time is {time.strftime('%H:%M:%S')}")
            elif "open" in command and "browser" in command:
                os.system("start chrome")  # For Windows, use appropriate command for other OS
                self.speak("Opening the browser")
            elif "shutdown" in command:
                self.speak("Shutting down the system.")
                os.system("shutdown /s /t 1")  # For Windows, change for other systems
            else:
                self.speak("Sorry, I don't recognize that command.")

    def listen_and_process(self):
        while True:
            audio = self.listen()
            command = self.recognize_speech(audio)
            self.process_command(command)

    def start(self):
        listening_thread = threading.Thread(target=self.listen_and_process)
        listening_thread.daemon = True
        listening_thread.start()
        self.speak(f"Hello, I am {self.name}, I am now listening for commands.")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.start()
