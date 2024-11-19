import unittest
from unittest.mock import patch
import pyttsx3
import speech_recognition as sr
from modules.voice_assistant import VoiceAssistant

class TestVoiceAssistant(unittest.TestCase):

    def setUp(self):
        self.voice_assistant = VoiceAssistant()

    @patch.object(pyttsx3.init(), 'say')
    @patch('speech_recognition.Recognizer.listen')
    def test_speech_recognition(self, mock_listen, mock_say):
        # Simulate microphone input (mock)
        mock_listen.return_value = sr.AudioData(b"mock_data", 1, 1)
        
        # Simulate user command for recognition
        response = self.voice_assistant.recognize_speech()

        self.assertIsNotNone(response)
        mock_say.assert_called_with("Recognizing your speech now...")

    @patch('speech_recognition.Recognizer.recognize_google')
    def test_recognize_google(self, mock_recognize_google):
        # Simulate Google Speech API response
        mock_recognize_google.return_value = "Turn off the lights"
        
        # Call the recognize_google method
        command = self.voice_assistant.recognize_speech()

        self.assertEqual(command, "Turn off the lights")

    @patch('modules.voice_assistant.os.system')
    def test_task_execution(self, mock_system):
        # Simulate an executed command
        command = "Turn off the lights"
        
        # Trigger the execution
        self.voice_assistant.execute_task(command)

        # Verify if the system command was called
        mock_system.assert_called_with("turn_off_lights_command")

    @patch('modules.voice_assistant.pyttsx3.init')
    def test_speak(self, mock_speech):
        mock_engine = mock_speech.return_value
        self.voice_assistant.speak("Hello, world!")
        
        # Ensure the speak function was called with the correct parameters
        mock_engine.say.assert_called_with("Hello, world!")

if __name__ == '__main__':
    unittest.main()
