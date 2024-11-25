import os
import logging
import subprocess
from config.settings import load_config
from modules.voice_assistant import VoiceAssistant
from modules.chatbot import ChatBot
from modules.social_media import SocialMediaManager
from modules.internet_tasks import InternetTasks
from modules.face_detection import FaceDetection
from modules.face_recognition import FaceRecognitionSystem
from modules.data_retrieval import DataRetrievalEngine
from operate.orchestrator import Orchestrator
from modules.device_control import DeviceControl
from modules.machine_learning import ModelManager
from modules.pimeye_integration import PimEyeIntegration
from apis.whiterabbit import WhiteRabbitAI
from config.settings import load_config

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("aia.log"), logging.StreamHandler()]
)

logger = logging.getLogger("AIA_Main")

def initialize_modules(orchestrator, config):
    """
    Initialize and register additional modules, including advanced integrations.
    """
    logger = logging.getLogger("ModuleInitializer")
    
    try:
        # Device Control Module
        device_control = DeviceControl(config=config)
        orchestrator.register_module("device_control", device_control)
        logger.info("Device Control module initialized.")
    except Exception as e:
        logger.error(f"Error initializing Device Control module: {e}", exc_info=True)
    
    try:
        # Machine Learning Manager
        model_manager = ModelManager()
        orchestrator.register_module("model_manager", model_manager)
        logger.info("Machine Learning module initialized.")
    except Exception as e:
        logger.error(f"Error initializing Machine Learning module: {e}", exc_info=True)
    
    try:
        # PimEye Integration
        pimeye = PimEyeIntegration(api_key=config["pimeye_api_key"])
        orchestrator.register_module("pimeye_integration", pimeye)
        logger.info("PimEye integration initialized.")
    except Exception as e:
        logger.error(f"Error initializing PimEye integration: {e}", exc_info=True)

    try:
        # Face Detection Module
        face_detection = FaceDetection(config=config)
        orchestrator.register_module("face_detection", face_detection)
        logger.info("Face Detection module initialized.")
    except Exception as e:
        logger.error(f"Error initializing Face Detection module: {e}", exc_info=True)
    
    try:
        # Face Recognition Module
        face_recognition = FaceRecognitionSystem(config=config)
        orchestrator.register_module("face_recognition", face_recognition)
        logger.info("Face Recognition module initialized.")
    except Exception as e:
        logger.error(f"Error initializing Face Recognition module: {e}", exc_info=True)
    
    try:
        # Data Retrieval Engine
        data_engine = DataRetrievalEngine(config=config)
        orchestrator.register_module("data_retrieval", data_engine)
        logger.info("Data Retrieval engine initialized.")
    except Exception as e:
        logger.error(f"Error initializing Data Retrieval Engine: {e}", exc_info=True)

    try:
        # WhiteRabbit AI API
        white_rabbit = WhiteRabbitAI(config=config)
        orchestrator.register_module("white_rabbit_ai", white_rabbit)
        logger.info("WhiteRabbit AI integration initialized.")
    except Exception as e:
        logger.error(f"Error initializing WhiteRabbit AI API: {e}", exc_info=True)

def start_s3_service():
    """
    Function to start the FastAPI S3 file download service in a separate process.
    """
    try:
        subprocess.Popen(['python', 'services/s3_service.py'])  # Ensure s3_service.py is in the services/ folder
        logger.info("S3 Service started successfully.")
    except Exception as e:
        logger.error(f"Error starting S3 service: {e}", exc_info=True)

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
                print("Available Commands: [start, stop, detect_face, recognize_person, retrieve_data, download_file, status, exit]")
            elif user_input.lower() == "download_file":
                file_name = input("Enter the file name to download from S3: ")
                # Call the new S3 download function
                download_from_s3(file_name)
            elif user_input.lower() == "detect_face":
                image_path = input("Enter the image path for face detection: ")
                results = orchestrator.execute_task("face_detection", {"image_path": image_path})
                print(f"Detected Faces: {results}")
            elif user_input.lower() == "recognize_person":
                image_path = input("Enter the image path for recognition: ")
                results = orchestrator.execute_task("face_recognition", {"image_path": image_path})
                print(f"Recognition Results: {results}")
            elif user_input.lower() == "retrieve_data":
                image_path = input("Enter the image path for data retrieval: ")
                results = orchestrator.execute_task("data_retrieval", {"image_path": image_path})
                print(f"Data Retrieved: {results}")
            else:
                response = orchestrator.handle_command(user_input)
                print(f"AIA: {response}")
        except KeyboardInterrupt:
            print("\nExiting AIA System. Goodbye!")
            break
        except Exception as e:
            logger.error(f"An error occurred in the UI: {e}", exc_info=True)
            print("An unexpected error occurred. Please check the logs.")

def download_from_s3(file_name):
    """
    Function to download files from S3 using the FastAPI endpoint.
    """
    import requests
    url = f"http://localhost:8000/download/{file_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"File {file_name} downloaded successfully.")
    else:
        print(f"Error: {response.json()}")

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
    
    # Initialize voice assistant
    voice_assistant = VoiceAssistant(config=config)
    orchestrator.register_module("voice_assistant", voice_assistant)
    
    # Initialize chatbot
    chatbot = ChatBot()
    orchestrator.register_module("chatbot", chatbot)
    
    # Initialize social media manager
    social_media_manager = SocialMediaManager(config=config)
    orchestrator.register_module("social_media", social_media_manager)
    
    # Initialize internet tasks manager
    internet_task_manager = InternetTasks(config=config)
    orchestrator.register_module("internet_tasks", internet_task_manager)
    
    # Initialize additional modules
    initialize_modules(orchestrator, config)
    
    # Start the S3 service
    start_s3_service()
    
    # Start interactive UI
    interactive_ui(orchestrator)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Critical error in main execution: {e}", exc_info=True)
