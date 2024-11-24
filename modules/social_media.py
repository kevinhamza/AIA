import os
import requests
import json
from config.social_media_keys import SocialMediaKeys

class SocialMediaManager:
    def __init__(self, config=None):
        # Ensure config is passed and has necessary attributes
        if config:
            self.config = config
        else:
            # Fallback to hardcoded keys if no config is provided
            self.config = {}

        self.twitter_api_key = self.config.get("twitter", {}).get("api_key", "default_twitter_api_key")
        self.facebook_api_key = self.config.get("facebook", {}).get("access_token", "default_facebook_access_token")
        
    def post_to_twitter(self, message):
        url = f"https://api.twitter.com/2/tweets"
        headers = {
            "Authorization": f"Bearer {self.twitter_api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "status": message
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 201:
            print("Successfully posted to Twitter!")
        else:
            print(f"Error posting to Twitter: {response.status_code}")

    def post_to_facebook(self, message):
        url = f"https://graph.facebook.com/v10.0/me/feed"
        headers = {
            "Authorization": f"Bearer {self.facebook_api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "message": message
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print("Successfully posted to Facebook!")
        else:
            print(f"Error posting to Facebook: {response.status_code}")

    def get_latest_posts(self, platform="twitter"):
        if platform == "twitter":
            url = f"https://api.twitter.com/2/tweets"
            headers = {
                "Authorization": f"Bearer {self.twitter_api_key}"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("Latest posts from Twitter:", response.json())
            else:
                print(f"Error fetching posts from Twitter: {response.status_code}")
        elif platform == "facebook":
            url = f"https://graph.facebook.com/v10.0/me/feed"
            headers = {
                "Authorization": f"Bearer {self.facebook_api_key}"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("Latest posts from Facebook:", response.json())
            else:
                print(f"Error fetching posts from Facebook: {response.status_code}")
        else:
            print("Invalid platform specified.")

if __name__ == "__main__":
    # Example of initializing with a config
    smm = SocialMediaManager(config={
        "twitter": {"api_key": "your_twitter_api_key"},
        "facebook": {"access_token": "your_facebook_access_token"}
    })
    smm.post_to_twitter("Hello from my assistant!")
    smm.get_latest_posts("twitter")
