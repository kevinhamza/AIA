import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SocialMediaKeys:
    """
    Store API keys and credentials for various social media platforms.
    """

    # Twitter API
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", "")

    # Facebook API
    FACEBOOK_APP_ID = os.getenv("FACEBOOK_APP_ID", "")
    FACEBOOK_APP_SECRET = os.getenv("FACEBOOK_APP_SECRET", "")
    FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN", "")

    # Instagram API
    INSTAGRAM_CLIENT_ID = os.getenv("INSTAGRAM_CLIENT_ID", "")
    INSTAGRAM_CLIENT_SECRET = os.getenv("INSTAGRAM_CLIENT_SECRET", "")
    INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")

    # LinkedIn API
    LINKEDIN_CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID", "")
    LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET", "")
    LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "")

    # YouTube API
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

    @staticmethod
    def get_keys(platform):
        """
        Retrieve the API keys for a specific platform.
        """
        platform_keys = {
            "twitter": {
                "api_key": SocialMediaKeys.TWITTER_API_KEY,
                "api_secret": SocialMediaKeys.TWITTER_API_SECRET,
                "access_token": SocialMediaKeys.TWITTER_ACCESS_TOKEN,
                "access_secret": SocialMediaKeys.TWITTER_ACCESS_SECRET,
            },
            "facebook": {
                "app_id": SocialMediaKeys.FACEBOOK_APP_ID,
                "app_secret": SocialMediaKeys.FACEBOOK_APP_SECRET,
                "access_token": SocialMediaKeys.FACEBOOK_ACCESS_TOKEN,
            },
            "instagram": {
                "client_id": SocialMediaKeys.INSTAGRAM_CLIENT_ID,
                "client_secret": SocialMediaKeys.INSTAGRAM_CLIENT_SECRET,
                "access_token": SocialMediaKeys.INSTAGRAM_ACCESS_TOKEN,
            },
            "linkedin": {
                "client_id": SocialMediaKeys.LINKEDIN_CLIENT_ID,
                "client_secret": SocialMediaKeys.LINKEDIN_CLIENT_SECRET,
                "access_token": SocialMediaKeys.LINKEDIN_ACCESS_TOKEN,
            },
            "youtube": {
                "api_key": SocialMediaKeys.YOUTUBE_API_KEY,
            },
        }
        return platform_keys.get(platform.lower(), {})

    @staticmethod
    def validate_keys(platform):
        """
        Validate if the required keys are available for a platform.
        """
        keys = SocialMediaKeys.get_keys(platform)
        missing_keys = [key for key, value in keys.items() if not value]
        if missing_keys:
            return False, f"Missing keys: {', '.join(missing_keys)}"
        return True, "All keys are present."

# Example usage:
# status, message = SocialMediaKeys.validate_keys("twitter")
# print(message)
