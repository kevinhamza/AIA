import requests
import json
import os
from config.social_media_keys import TWITTER_API_KEY, FACEBOOK_API_KEY

class SocialMediaManager:
    def __init__(self):
        self.twitter_api_key = TWITTER_API_KEY
        self.facebook_api_key = FACEBOOK_API_KEY

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
    smm = SocialMediaManager()
    smm.post_to_twitter("Hello from my assistant!")
    smm.get_latest_posts("twitter")
