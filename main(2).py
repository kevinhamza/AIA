import os
import logging
import pyautogui
from config.settings import load_config
from modules.voice_assistant import VoiceAssistant
from modules.chatbot import ChatBot
from modules.social_media import SocialMediaManager
from modules.internet_tasks import InternetTaskManager
from modules.device_control import DeviceControl
from modules.machine_learning import ModelManager
from apis.whiterabbit import WhiteRabbitAI
from utils.error_handler import ErrorHandler
from utils.logging import setup_custom_logger
from operate.orchestrator import Orchestrator

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("aia.log"), logging.StreamHandler()]
)

logger = logging.getLogger("AIA_Main")

class DeviceControl:
    def __init__(self, config):
        self.config = config

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y)

    def click_mouse(self):
        pyautogui.click()

    def type_text(self, text):
        pyautogui.typewrite(text)

def initialize_modules(orchestrator, config):
    """
    Initialize and register additional modules.
    """
    logger = logging.getLogger("ModuleInitializer")
    
    # Device Control Module
    try:
        device_control = DeviceControl(config=config)
        orchestrator.register_module("device_control", device_control)
        logger.info("Device Control module initialized.")
    except Exception as e:
        logger.error(f"Error initializing Device Control module: {e}", exc_info=True)
    
    # Machine Learning Manager
    try:
        model_manager = ModelManager(config=config)
        orchestrator.register_module("model_manager", model_manager)
        logger.info("Machine Learning module initialized.")
    except Exception as e:
        logger.error(f"Error initializing Machine Learning module: {e}", exc_info=True)
    
    # WhiteRabbit AI API
    try:
        white_rabbit = WhiteRabbitAI(config=config)
        orchestrator.register_module("white_rabbit_ai", white_rabbit)
        logger.info("WhiteRabbit AI integration initialized.")
    except Exception as e:
        logger.error(f"Error initializing WhiteRabbit AI API: {e}", exc_info=True)

def interactive_ui(orchestrator):
    """
    Command-line UI for interacting with the AIA system.
    """
    logger = logging.getLogger("InteractiveUI")
    print("\nWelcome to the Advanced Intelligent Assistant (AIA) System!")
    print("Type 'help' for available commands or 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("AIA > ").strip()
            if user_input.lower() == "exit":
                print("Exiting AIA System. Goodbye!")
                break
            elif user_input.lower() == "help":
                print("Available Commands: [start, stop, status, exit, move, click, type]")
            elif user_input.lower().startswith("move"):
                _, x, y = user_input.split()
                orchestrator.get_module("device_control").move_mouse(int(x), int(y))
                print(f"Mouse moved to ({x}, {y})")
            elif user_input.lower() == "click":
                orchestrator.get_module("device_control").click_mouse()
                print("Mouse clicked.")
            elif user_input.lower().startswith("type"):
                _, text = user_input.split(maxsplit=1)
                orchestrator.get_module("device_control").type_text(text)
                print(f"Typed text: {text}")
            else:
                response = orchestrator.handle_command(user_input)
                print(f"AIA: {response}")
        except KeyboardInterrupt:
            print("\nExiting AIA System. Goodbye!")
            break
        except Exception as e:
            logger.error(f"An error occurred in the UI: {e}", exc_info=True)
            print("An unexpected error occurred. Please check the logs.")

def main():
    """
    Main entry point for the AIA system.
    Initializes configurations, orchestrator, and various modules.
    """
    logger.info("Starting AIA System...")
    
    # Load configuration
    config = load_config()
    logger.info("Configuration loaded successfully.")
    
    # Initialize orchestrator
    orchestrator = Orchestrator(config=config)
    
    # Initialize core modules
    voice_assistant = VoiceAssistant(config=config)
    orchestrator.register_module("voice_assistant", voice_assistant)
    
    chatbot = ChatBot(config=config)
    orchestrator.register_module("chatbot", chatbot)
    
    social_media_manager
