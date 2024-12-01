import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """
    A class to store all configuration settings for the project.
    """

    # General Settings
    APP_NAME = "AIA - All-In-One Assistant"
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False").strip().lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

    # AI & Machine Learning Settings
    MODEL_TYPE = os.getenv("MODEL_TYPE", "random_forest")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

    # White Rabbit AI Integration
    WHITERABBIT_API_KEY = os.getenv("WHITERABBIT_API_KEY", "")
    WHITERABBIT_ENDPOINT = os.getenv("WHITERABBIT_ENDPOINT", "https://api.whiterabbitneo.com/v1/")

    # Task Scheduling
    TASK_REFRESH_RATE = int(os.getenv("TASK_REFRESH_RATE", "60"))  # In seconds

    # OCR Settings
    OCR_LANGUAGE = os.getenv("OCR_LANGUAGE", "en")
    OCR_ENGINE = os.getenv("OCR_ENGINE", "easyocr")

    # File Handling
    TEMP_DIRECTORY = os.getenv("TEMP_DIRECTORY", "./temp")
    UPLOAD_DIRECTORY = os.getenv("UPLOAD_DIRECTORY", "./uploads")
    os.makedirs(TEMP_DIRECTORY, exist_ok=True)
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    # Social Media Configurations
    SOCIAL_MEDIA_ENABLED = os.getenv("SOCIAL_MEDIA_ENABLED", "False").strip().lower() == "true"
    ALLOWED_SOCIAL_PLATFORMS = os.getenv("ALLOWED_SOCIAL_PLATFORMS", "twitter,facebook,instagram").split(",")

    # Network Settings
    PROXY_ENABLED = os.getenv("PROXY_ENABLED", "False").strip().lower() == "true"
    PROXY_URL = os.getenv("PROXY_URL", "")
    TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "30"))

    # Security Settings
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "default-encryption-key")
    AUTH_TOKEN_EXPIRY = int(os.getenv("AUTH_TOKEN_EXPIRY", "3600"))  # In seconds

    # User Interface
    UI_THEME = os.getenv("UI_THEME", "dark")
    UI_LANGUAGE = os.getenv("UI_LANGUAGE", "en")
    UI_FONT_SIZE = int(os.getenv("UI_FONT_SIZE", "12"))
    UI_COLOR_SCHEME = os.getenv("UI_COLOR_SCHEME", "blue")

    # Io T Device Control
    IOT_ENABLED = os.getenv("IOT_ENABLED", "False").strip().lower() == "true"
    IOT_DEVICES = os.getenv("IOT_DEVICES", "smart_light,thermostat").split(",")

    # Logging Configuration
    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "./logs/app.log")
    MAX_LOG_FILE_SIZE_MB = int(os.getenv("MAX_LOG_FILE_SIZE_MB", "5"))
    LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "3"))

    # Notification Settings
    NOTIFICATION_ENABLED = os.getenv("NOTIFICATION_ENABLED", "True").strip().lower() == "true"
    NOTIFICATION_CHANNELS = os.getenv("NOTIFICATION_CHANNELS", "email,sms").split(",")

    # API Rate Limiting
    API_RATE_LIMIT = int(os.getenv("API_RATE_LIMIT", "100"))

    # Database Settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./database.db")
    DATABASE_POOL_SIZE = int(os.getenv("DATABASE_POOL_SIZE", "5"))

    @staticmethod
    def get(key, default_value=None):
        """
        Utility method to fetch a configuration setting dynamically.
        """
        return getattr(Config, key, default_value)

    @staticmethod
    def get_api_key(key_name: str) -> str:
        """Retrieve a specific API key."""
        return os.getenv(key_name, '')

    # @staticmethod
    # def get_model_config() -> str:
    #     """Retrieve the model configuration."""
    #     return Config.MODEL_TYPE

    @staticmethod
    def get_model_config(key_name: str) -> str:
        """Retrieve a specific model configuration."""
        if key_name == "MODEL_TYPE":
            return Config.MODEL_TYPE
        # Add more model configuration retrieval as needed
        return ''

    def validate(self):
        """Validate required configuration settings."""
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY must be set in the environment.")
        # Add more validations as needed

    @staticmethod
    def load_config() -> 'Config':
        """
        Returns the Config class with all configurations.
        """
        config = Config()
        config.validate()  # Validate configuration
        return config
    

# Example usage for debugging
if __name__ == "__main__":
    # config = load_config()
    config = Config.load_config()  # Use the static method
    print(f"App Name: {config.APP_NAME}")
    print(f"Debug Mode: {config.DEBUG_MODE}")
    print(f"Log Level: {config.LOG_LEVEL}")
    print(f"OpenAI API Key: {config.OPENAI_API_KEY}")
    print(f"Social Media Enabled: {config.SOCIAL_MEDIA_ENABLED}")
    print(f"Allowed Platforms: {config.ALLOWED_SOCIAL_PLATFORMS}")
    print(f"Temp Directory: {config.TEMP_DIRECTORY}")
    print(f"Model Type: {config.get_model_config()}")
