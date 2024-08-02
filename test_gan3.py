import unittest
from PIL import Image
import os
from pyuzantı import convert_png_to_ico


class TestConvertPngToIco(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources for testing
        self.test_folder = 'test_images'
        os.makedirs(self.test_folder, exist_ok=True)

    def tearDown(self):
        # Clean up resources after testing
        os.rmdir(self.test_folder)

    def test_convert_png_to_ico(self):
        # Create a test PNG file
        test_png_path = os.path.join(self.test_folder, 'test_image.png')
        Image.new('RGB', (100, 100), color='red').save(test_png_path)

        # Call the function with the test PNG file
        convert_png_to_ico(self.test_folder, self.test_folder)

        # Check if the ICO file is created
        ico_path = os.path.join(self.test_folder, 'icon', 'test_image.ico')
        self.assertTrue(os.path.exists(ico_path), 'ICO file not created.')

if __name__ == '__main__':
    unittest.main()
