import unittest
import os
from compressor import Compressor

class TestCli(unittest.TestCase):
    def setUp(self):
        self.input_filename = './test_input.txt'
        self.output_filename = './test_output'
        c = Compressor()
        c.compress_file(self.input_filename, self.output_filename)

    def tearDown(self):
        if os.path.exists(self.output_filename):
            os.remove(self.output_filename)

    def test_compress(self):
        self.assertTrue(os.path.exists(self.output_filename), f"Output file '{self.output_filename}' does not exist")
        with open(self.output_filename, 'r') as f:
            compressed_data = f.read()
        print("compressed data", compressed_data)

        self.assertIsInstance(compressed_data, str, "Compressed data is not a string")

if __name__ == '__main__':
    unittest.main()

