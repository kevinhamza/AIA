import unittest
from unittest.mock import patch
from modules.social_media import SocialMedia

class TestSocialMediaModule(unittest.TestCase):

    def setUp(self):
        self.social_media = SocialMedia()

    @patch('modules.social_media.requests.get')
    def test_fetch_twitter_feed(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": [{"id": "1", "text": "Hello World"}]}

        # Call the method to fetch the Twitter feed
        tweets = self.social_media.fetch_twitter_feed()

        # Validate that the correct tweet is fetched
        self.assertEqual(tweets[0]["text"], "Hello World")
        mock_get.assert_called_once_with("https://api.twitter.com/2/tweets?ids=1")

    @patch('modules.social_media.requests.post')
    def test_post_to_facebook(self, mock_post):
        # Simulate a successful API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Post successful"}

        # Call the method to post to Facebook
        response = self.social_media.post_to_facebook("Hello Facebook")

        # Ensure the post was successful
        self.assertEqual(response["message"], "Post successful")
        mock_post.assert_called_once_with(
            "https://graph.facebook.com/v10.0/me/feed",
            data={"message": "Hello Facebook"}
        )

    @patch('modules.social_media.requests.get')
    def test_fetch_instagram_feed(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": [{"id": "2", "caption": "Insta post"}]}

        # Call the method to fetch the Instagram feed
        feed = self.social_media.fetch_instagram_feed()

        # Validate the fetched Instagram post
        self.assertEqual(feed[0]["caption"], "Insta post")
        mock_get.assert_called_once_with("https://api.instagram.com/v1/users/self/media/recent")

    @patch('modules.social_media.requests.get')
    def test_fetch_linkedin_profile(self, mock_get):
        # Simulate a successful API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"firstName": "John", "lastName": "Doe"}

        # Call the method to fetch LinkedIn profile info
        profile = self.social_media.fetch_linkedin_profile()

        # Validate the LinkedIn profile information
        self.assertEqual(profile["firstName"], "John")
        self.assertEqual(profile["lastName"], "Doe")
        mock_get.assert_called_once_with("https://api.linkedin.com/v2/me")

if __name__ == '__main__':
    unittest.main()
