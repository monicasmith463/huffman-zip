import unittest
import os
from huffman_compressor import Compressor

class TestCli(unittest.TestCase):
    def setUp(self):
        self.input_compress_filename = './test_compress.txt'
        self.output_compress_filename = './test_compress.bin'
        self.output_decompress_filename = './test_output_decompress.txt'
        self.db_filename = './persisted_trees.db'
        self.compressor = Compressor()

        # Create a sample input file with known content
        with open(self.input_compress_filename, 'w') as f:
            f.write('Test me. I am a test input. I contain special characters like !, &, $, \. Numbers too, like 1, 7, 1934.')

        # Clean up files if they exist
        for file in [self.output_compress_filename, self.output_decompress_filename]:
            if os.path.exists(file):
                os.remove(file)
    
    def tearDown(self):
        # Remove test files after tests are run
        for file in [self.input_compress_filename, self.output_compress_filename, self.output_decompress_filename]:
            if os.path.exists(file):
                os.remove(file)

    def test_compress(self):
        self.compressor.compress_file(self.input_compress_filename, self.output_compress_filename)
        self.assertTrue(os.path.exists(self.output_compress_filename), f"Output file '{self.output_compress_filename}' does not exist")
        with open(self.output_compress_filename, 'rb') as f:
            compressed_data = f.read()
        self.assertIsInstance(compressed_data, bytes, "Compressed data is not in bytes")
    
    def test_decompress(self):
        self.compressor.compress_file(self.input_compress_filename, self.output_compress_filename)
        self.compressor.decompress_file(self.output_compress_filename, self.output_decompress_filename)

        with open(self.output_decompress_filename, 'r') as f:
            compressed_data = f.read()
        self.assertIsInstance(compressed_data, str, "Compressed data is not a string")

    def test_compressed_file_is_smaller(self):
        self.compressor.compress_file(self.input_compress_filename, self.output_compress_filename)
        
        original_size = os.path.getsize(self.input_compress_filename)
        compressed_size = os.path.getsize(self.output_compress_filename)
        
        self.assertLess(compressed_size, original_size, "Compressed file is not smaller than the original file")
        

if __name__ == '__main__':
    unittest.main()

