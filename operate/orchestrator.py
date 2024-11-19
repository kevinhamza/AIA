import logging
import time
from modules.voice_assistant import VoiceAssistant
from modules.internet_tasks import InternetTasks
from modules.device_control import DeviceControl
from modules.social_media import SocialMedia
from modules.chatbot import ChatBot
from modules.machine_learning import MachineLearning
from modules.error_handling import ErrorHandler
from config.settings import Config

class Orchestrator:
    """
    Orchestrates various AI modules and system operations, combining voice recognition,
    task automation, device control, social media interactions, and error handling.
    """
    def __init__(self, config: Config):
        self.config = config
        self.logger = logging.getLogger("Orchestrator")
        self.logger.setLevel(logging.DEBUG)

        # Initializing modules
        self.voice_assistant = VoiceAssistant(config)
        self.internet_tasks = InternetTasks(config)
        self.device_control = DeviceControl(config)
        self.social_media = SocialMedia(config)
        self.chatbot = ChatBot(config)
        self.ml = MachineLearning(config)
        self.error_handler = ErrorHandler()

    def execute_voice_command(self, command: str):
        """
        Process a voice command, calling the respective method or module.
        """
        try:
            if "weather" in command:
                self.logger.info("Fetching weather information.")
                self.internet_tasks.get_weather()
            elif "news" in command:
                self.logger.info("Fetching news.")
                self.internet_tasks.get_news()
            elif "control" in command:
                self.logger.info("Controlling devices.")
                self.device_control.control_device(command)
            elif "social" in command:
                self.logger.info("Interacting with social media.")
                self.social_media.perform_task(command)
            elif "chat" in command:
                self.logger.info("Chatbot initiated.")
                self.chatbot.start_chatbot(command)
            else:
                self.logger.warning(f"Unknown command: {command}")
        except Exception as e:
            self.error_handler.log_error(f"Error executing voice command: {e}")

    def monitor_system(self):
        """
        Monitor the system's performance and handle any system-level requests.
        """
        try:
            while True:
                self.logger.info("System is running...")
                time.sleep(5)
        except KeyboardInterrupt:
            self.logger.info("System monitoring interrupted by user.")

    def run(self):
        """
        Run the orchestrator to handle commands, control the system, and process tasks.
        """
        self.logger.info("Starting Orchestrator...")
        while True:
            # For testing, simulate receiving a voice command
            command = self.voice_assistant.listen_for_command()
            if command:
                self.logger.info(f"Received command: {command}")
                self.execute_voice_command(command)

    def shutdown(self):
        """
        Shutdown the orchestrator and clean up resources.
        """
        self.logger.info("Shutting down orchestrator...")
        self.voice_assistant.stop_listening()
        self.device_control.shutdown_devices()
        self.logger.info("Orchestrator shut down successfully.")

# Example usage:
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    config = Config()
    orchestrator = Orchestrator(config)

    try:
        orchestrator.run()
    except KeyboardInterrupt:
        orchestrator.shutdown()
