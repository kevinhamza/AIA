import unittest
from unittest.mock import patch, MagicMock
from modules.data_retrieval import DataRetrievalEngine
from modules.social_media import SocialMediaManager

class TestDataRetrieval(unittest.TestCase):
    """
    Test suite for DataRetrievalEngine and its integrations with PimEyes-like services
    and social media platforms.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the testing environment.
        """
        cls.data_engine = DataRetrievalEngine(pim_eye_api_key="mock_pimeye_api_key")
        cls.social_media_manager = SocialMediaManager()

        # Sample mock matches
        cls.sample_matches = [
            {"name": "John Doe", "confidence": 0.95, "image_url": "http://example.com/john.jpg"},
            {"name": "Jane Smith", "confidence": 0.90, "image_url": "http://example.com/jane.jpg"},
        ]

    def test_pimeyes_integration(self):
        """
        Test PimEyes-like integration for image matching.
        """
        with patch("modules.pimeye_integration.PimEyeIntegration.upload_image") as mock_upload, \
             patch("modules.pimeye_integration.PimEyeIntegration.search_faces") as mock_search:

            # Mock responses
            mock_upload.return_value = {"id": "mock_image_id"}
            mock_search.return_value = self.sample_matches

            # Run data retrieval
            results = self.data_engine.process_image("tests/resources/test_image.jpg")
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0]["name"], "John Doe")
            self.assertAlmostEqual(results[0]["confidence"], 0.95)
            self.assertIn("image_url", results[0])

    @patch("modules.social_media.SocialMediaManager.query_facebook")
    @patch("modules.social_media.SocialMediaManager.query_twitter")
    @patch("modules.social_media.SocialMediaManager.query_instagram")
    @patch("modules.social_media.SocialMediaManager.query_linkedin")
    def test_social_media_data_retrieval(self, mock_linkedin, mock_instagram, mock_twitter, mock_facebook):
        """
        Test the retrieval of personal data from various social media platforms.
        """
        # Mock responses
        mock_facebook.return_value = {"profile_url": "http://facebook.com/john.doe", "data": {"name": "John Doe"}}
        mock_twitter.return_value = {"profile_url": "http://twitter.com/john_doe", "data": {"tweets": 10}}
        mock_instagram.return_value = {"profile_url": "http://instagram.com/john.doe", "data": {"followers": 500}}
        mock_linkedin.return_value = {"profile_url": "http://linkedin.com/in/johndoe", "data": {"position": "Developer"}}

        individual = {"name": "John Doe", "confidence": 0.95, "image_url": "http://example.com/john.jpg"}

        # Retrieve personal data
        personal_data = self.data_engine.get_individual_data(individual)

        # Validate the data
        self.assertIn("facebook", personal_data["social_media_profiles"])
        self.assertIn("twitter", personal_data["social_media_profiles"])
        self.assertIn("instagram", personal_data["social_media_profiles"])
        self.assertIn("linkedin", personal_data["social_media_profiles"])

        self.assertEqual(personal_data["social_media_profiles"]["facebook"]["data"]["name"], "John Doe")
        self.assertEqual(personal_data["social_media_profiles"]["twitter"]["data"]["tweets"], 10)

    def test_generate_combined_report(self):
        """
        Test report generation for multiple individuals.
        """
        # Sample data
        individuals_data = [
            {
                "name": "John Doe",
                "image_match_details": {"confidence": 0.95, "image_url": "http://example.com/john.jpg"},
                "social_media_profiles": {
                    "facebook": {"profile_url": "http://facebook.com/john.doe"},
                    "twitter": {"profile_url": "http://twitter.com/john_doe"},
                },
            },
            {
                "name": "Jane Smith",
                "image_match_details": {"confidence": 0.90, "image_url": "http://example.com/jane.jpg"},
                "social_media_profiles": {
                    "instagram": {"profile_url": "http://instagram.com/jane.smith"},
                    "linkedin": {"profile_url": "http://linkedin.com/in/janesmith"},
                },
            },
        ]

        # Generate report
        report = self.data_engine.generate_report(individuals_data)

        # Assertions
        self.assertIn("John Doe", report)
        self.assertIn("Jane Smith", report)
        self.assertIn("http://facebook.com/john.doe", report)
        self.assertIn("http://linkedin.com/in/janesmith", report)

    def test_handle_empty_results(self):
        """
        Test behavior when no matches or social media data are found.
        """
        with patch("modules.pimeye_integration.PimEyeIntegration.search_faces") as mock_search:
            mock_search.return_value = []

            results = self.data_engine.process_image("tests/resources/test_image.jpg")
            self.assertEqual(results, [])

    def test_integration_failure(self):
        """
        Test behavior when integrations fail (e.g., API errors).
        """
        with patch("modules.pimeye_integration.PimEyeIntegration.search_faces") as mock_search:
            mock_search.side_effect = Exception("PimEyes API error")

            with self.assertRaises(Exception):
                self.data_engine.process_image("tests/resources/test_image.jpg")

if __name__ == "__main__":
    unittest.main()
