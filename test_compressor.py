import unittest
import os
from huffman_compressor import Compressor

class TestCli(unittest.TestCase):
    def setUp(self):
        self.input_compress_filename = './test_input.txt'
        self.output_compress_filename = './test_output_compress.txt'
        self.output_decompress_filename = './test_output_decompress.txt'
        self.compressor = Compressor()

    def tearDown(self):
        if os.path.exists(self.output_compress_filename):
            os.remove(self.output_compress_filename)
        if os.path.exists(self.output_decompress_filename):
            os.remove(self.output_decompress_filename)

    def test_compress(self):
        self.compressor.compress_file(self.input_compress_filename, self.output_compress_filename)
        self.assertTrue(os.path.exists(self.output_compress_filename), f"Output file '{self.output_compress_filename}' does not exist")
        with open(self.output_compress_filename, 'r') as f:
            compressed_data = f.read()
        self.assertIsInstance(compressed_data, str, "Compressed data is not a string")
    
    def test_decompress(self):
        self.compressor.compress_file(self.input_compress_filename, self.output_compress_filename)
        self.compressor.decompress_file(self.output_compress_filename, self.output_decompress_filename)

        with open(self.output_decompress_filename, 'r') as f:
            compressed_data = f.read()
        self.assertIsInstance(compressed_data, str, "Compressed data is not a string")

if __name__ == '__main__':
    unittest.main()

