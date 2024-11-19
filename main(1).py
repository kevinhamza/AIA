import os
import logging
from operate.config.settings import load_config
from operate.modules.voice_assistant import VoiceAssistant
from operate.modules.chatbot import Chatbot
from operate.modules.device_control import DeviceControl
from operate.modules.internet_tasks import InternetTasks
from operate.utils.misc import check_environment
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Main application class
class AIAApp:
    def __init__(self):
        logging.info("Initializing AIA...")
        self.config = load_config()
        self.voice_assistant = VoiceAssistant()
        self.chatbot = Chatbot()
        self.device_control = DeviceControl()
        self.internet_tasks = InternetTasks()

    def start(self):
        logging.info("Starting the AIA Application...")
        if not check_environment():
            logging.error("Environment check failed. Ensure all dependencies are installed.")
            return

        while True:
            try:
                logging.info("Awaiting user command...")
                user_input = self.voice_assistant.listen()
                response = self.process_command(user_input)
                if response:
                    self.voice_assistant.speak(response)
            except KeyboardInterrupt:
                logging.info("Shutting down AIA Application.")
                break
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")

    def process_command(self, command):
        logging.info(f"Processing command: {command}")

        if "search" in command:
            query = command.replace("search", "").strip()
            return self.internet_tasks.search_web(query)
        elif "control device" in command:
            device = command.replace("control device", "").strip()
            return self.device_control.control(device)
        elif "chat" in command:
            return self.chatbot.converse(command)
        elif "exit" in command:
            logging.info("User requested to exit.")
            exit(0)
        else:
            return "I didn't understand the command. Could you please repeat?"

if __name__ == "__main__":
    app = AIAApp()
    app.start()
