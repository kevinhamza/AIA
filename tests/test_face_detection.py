import unittest
import os
from modules.face_detection import FaceDetection
from modules.data_retrieval import DataRetrievalEngine
from unittest.mock import patch, MagicMock

class TestFaceDetection(unittest.TestCase):
    """
    Test suite for face detection and data retrieval functionalities.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up resources for testing, including test images and mock APIs.
        """
        cls.face_detection = FaceDetection()
        cls.data_engine = DataRetrievalEngine(pim_eye_api_key="mock_api_key")
        cls.test_image_path = "tests/resources/test_image.jpg"

        # Ensure test resource folder exists
        if not os.path.exists("tests/resources"):
            os.makedirs("tests/resources")

        # Create a mock test image
        with open(cls.test_image_path, "wb") as f:
            f.write(b"mock_image_data")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up resources after testing.
        """
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)

    def test_face_detection_from_image(self):
        """
        Test that face detection correctly identifies faces in an image.
        """
        with patch("modules.face_detection.FaceDetection.detect_faces") as mock_detect_faces:
            mock_detect_faces.return_value = [
                {"face_id": "123", "bounding_box": [0, 0, 100, 100]},
                {"face_id": "456", "bounding_box": [150, 50, 250, 150]},
            ]

            faces = self.face_detection.detect_faces(self.test_image_path)
            self.assertEqual(len(faces), 2)
            self.assertEqual(faces[0]["face_id"], "123")
            self.assertEqual(faces[1]["face_id"], "456")

    @patch("modules.data_retrieval.PimEyeIntegration.upload_image")
    @patch("modules.data_retrieval.PimEyeIntegration.search_faces")
    def test_data_retrieval_with_pimeyes(self, mock_search_faces, mock_upload_image):
        """
        Test data retrieval from PimEyes-like service.
        """
        # Mock the PimEye integration
        mock_upload_image.return_value = {"id": "mock_image_id"}
        mock_search_faces.return_value = [
            {"name": "John Doe", "image_url": "http://example.com/john.jpg", "confidence": 0.95},
            {"name": "Jane Smith", "image_url": "http://example.com/jane.jpg", "confidence": 0.92},
        ]

        individuals_data = self.data_engine.process_image(self.test_image_path)
        self.assertEqual(len(individuals_data), 2)
        self.assertEqual(individuals_data[0]["name"], "John Doe")
        self.assertEqual(individuals_data[1]["name"], "Jane Smith")

    @patch("modules.social_media.SocialMediaManager.query_facebook")
    @patch("modules.social_media.SocialMediaManager.query_twitter")
    @patch("modules.social_media.SocialMediaManager.query_instagram")
    @patch("modules.social_media.SocialMediaManager.query_linkedin")
    def test_social_media_integration(self, mock_linkedin, mock_instagram, mock_twitter, mock_facebook):
        """
        Test social media integration for retrieving personal data.
        """
        # Mock social media responses
        mock_facebook.return_value = {"profile_url": "http://facebook.com/john.doe"}
        mock_twitter.return_value = {"profile_url": "http://twitter.com/john_doe"}
        mock_instagram.return_value = {"profile_url": "http://instagram.com/john.doe"}
        mock_linkedin.return_value = {"profile_url": "http://linkedin.com/in/johndoe"}

        match = {"name": "John Doe", "confidence": 0.95}
        personal_data = self.data_engine.get_individual_data(match)

        self.assertIn("facebook", personal_data["social_media_profiles"])
        self.assertIn("twitter", personal_data["social_media_profiles"])
        self.assertIn("instagram", personal_data["social_media_profiles"])
        self.assertIn("linkedin", personal_data["social_media_profiles"])

        self.assertEqual(personal_data["social_media_profiles"]["facebook"]["profile_url"], "http://facebook.com/john.doe")

    def test_report_generation(self):
        """
        Test the report generation for detected individuals.
        """
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
                "image_match_details": {"confidence": 0.92, "image_url": "http://example.com/jane.jpg"},
                "social_media_profiles": {
                    "instagram": {"profile_url": "http://instagram.com/jane.smith"},
                    "linkedin": {"profile_url": "http://linkedin.com/in/janesmith"},
                },
            },
        ]

        report = self.data_engine.generate_report(individuals_data)
        self.assertIn("John Doe", report)
        self.assertIn("http://facebook.com/john.doe", report)
        self.assertIn("Jane Smith", report)
        self.assertIn("http://linkedin.com/in/janesmith", report)


if __name__ == "__main__":
    unittest.main()
