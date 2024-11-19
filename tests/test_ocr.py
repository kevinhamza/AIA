import unittest
from unittest.mock import patch
from modules.ocr import OCRProcessor

class TestOCRModule(unittest.TestCase):

    def setUp(self):
        self.ocr_processor = OCRProcessor()

    @patch('modules.ocr.pytesseract.image_to_string')
    def test_extract_text_from_image(self, mock_image_to_string):
        # Simulate OCR text extraction from an image
        mock_image_to_string.return_value = "Extracted text from image"

        # Call the method to extract text from an image
        text = self.ocr_processor.extract_text_from_image("test_image.png")

        # Verify that the text extraction is correct
        self.assertEqual(text, "Extracted text from image")
        mock_image_to_string.assert_called_once_with("test_image.png")

    @patch('modules.ocr.pytesseract.image_to_string')
    def test_handle_ocr_error(self, mock_image_to_string):
        # Simulate an OCR error (e.g., invalid image)
        mock_image_to_string.side_effect = Exception("OCR error")

        # Call the method and verify the error is handled
        with self.assertRaises(Exception):
            self.ocr_processor.extract_text_from_image("invalid_image.png")

    @patch('modules.ocr.pytesseract.image_to_string')
    def test_extract_text_from_multiple_images(self, mock_image_to_string):
        # Simulate text extraction from multiple images
        mock_image_to_string.side_effect = ["Text from image 1", "Text from image 2"]

        # Call the method to extract text from multiple images
        images = ["image1.png", "image2.png"]
        texts = self.ocr_processor.extract_text_from_multiple_images(images)

        # Verify that the extracted texts match
        self.assertEqual(texts, ["Text from image 1", "Text from image 2"])
        mock_image_to_string.assert_any_call("image1.png")
        mock_image_to_string.assert_any_call("image2.png")

if __name__ == '__main__':
    unittest.main()
