import os

class APIKeys:
    """
    Class to handle API keys and sensitive data for external services
    """

    def __init__(self):
        # WhiteRabbit AI API key
        self.whiterabbit_api_key = os.getenv("WHITERABBIT_API_KEY", "your_whiterabbit_api_key_here")

        # OpenAI API key for GPT interaction
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

        # Weather API key (e.g., OpenWeather)
        self.weather_api_key = os.getenv("WEATHER_API_KEY", "your_weather_api_key_here")

        # News API key (e.g., NewsAPI)
        self.news_api_key = os.getenv("NEWS_API_KEY", "your_news_api_key_here")

        # Social Media API keys (for future integration)
        self.twitter_api_key = os.getenv("TWITTER_API_KEY", "your_twitter_api_key_here")
        self.instagram_api_key = os.getenv("INSTAGRAM_API_KEY", "your_instagram_api_key_here")

    def get_whiterabbit_api_key(self):
        """
        Retrieves the WhiteRabbit AI API key.
        """
        return self.whiterabbit_api_key

    def get_openai_api_key(self):
        """
        Retrieves the OpenAI API key.
        """
        return self.openai_api_key

    def get_weather_api_key(self):
        """
        Retrieves the Weather API key.
        """
        return self.weather_api_key

    def get_news_api_key(self):
        """
        Retrieves the News API key.
        """
        return self.news_api_key

    def get_twitter_api_key(self):
        """
        Retrieves the Twitter API key.
        """
        return self.twitter_api_key

    def get_instagram_api_key(self):
        """
        Retrieves the Instagram API key.
        """
        return self.instagram_api_key
