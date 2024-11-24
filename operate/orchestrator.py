import logging
import time
from modules.voice_assistant import VoiceAssistant
from modules.internet_tasks import InternetTasks
from modules.device_control import DeviceControl
from modules.social_media import SocialMediaManager
from modules.chatbot import ChatBot
from modules.machine_learning import ModelManager
from modules.error_handling import ErrorLogger
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

        # Initialize modules
        self.voice_assistant = VoiceAssistant(config)
        self.internet_tasks = InternetTasks(config)
        self.device_control = DeviceControl()
        self.social_media_manager = SocialMediaManager()
        self.chatbot = ChatBot(config)
        model_type = config.model_type  # or whichever field holds the model type
        self.ml = ModelManager(model_type=model_type)
        self.error_handler = ErrorLogger(log_directory="logs")  # Initialize the ErrorLogger

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
                self.device_control.move_mouse(100, 100)  # Example action
            elif "social" in command:
                self.logger.info("Interacting with social media.")
                if "post to twitter" in command:
                    self.social_media_manager.post_to_twitter("Automated post!")
                elif "fetch twitter posts" in command:
                    self.social_media_manager.get_latest_posts("twitter")
                elif "post to facebook" in command:
                    self.social_media_manager.post_to_facebook("Automated post!")
                else:
                    self.logger.warning("Unknown social media command.")
            elif "chat" in command:
                self.logger.info("Chatbot initiated.")
                self.chatbot.start_chatbot(command)
            else:
                self.logger.warning(f"Unknown command: {command}")
        except Exception as e:
            error_message = self.error_handler.handle_exception(e, "Error in execute_voice_command")
            self.logger.error(error_message)

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
            try:
                # Simulate receiving a voice command for testing
                command = self.voice_assistant.listen_for_command()
                if command:
                    self.logger.info(f"Received command: {command}")
                    self.execute_voice_command(command)
            except KeyboardInterrupt:
                self.shutdown()
                break
            except Exception as e:
                error_message = self.error_handler.handle_exception(e, "Error in orchestrator.run")
                self.logger.error(error_message)

    def shutdown(self):
        """
        Shutdown the orchestrator and clean up resources.
        """
        self.logger.info("Shutting down orchestrator...")
        self.voice_assistant.stop_listening()
        self.device_control.shutdown_system()
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
