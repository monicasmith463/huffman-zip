import unittest
import os
import subprocess

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.input_compress_filename = './test_compress.txt'
        self.output_compress_filename = './test_compress.bin'
        self.output_decompress_filename = './test_output_decompress.txt'
        self.db_filename = './persisted_trees.db'

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

    def run_cli(self, *args):
        """Helper function to run the CLI with arguments."""
        result = subprocess.run(['python', 'cli.py'] + list(args))
        return result.returncode, result.stdout, result.stderr
    
    def test_compress(self):
        """Test the compression functionality."""
        returncode, stdout, stderr = self.run_cli('compress', self.input_compress_filename, self.output_compress_filename)
        
        self.assertEqual(returncode, 0, f"Compression failed with stderr: {stderr}")
        self.assertTrue(os.path.exists(self.output_compress_filename), "Compressed file was not created")

    def test_decompress(self):
        """Test the decompression functionality."""
        # First compress the file
        returncode, stdout, stderr = self.run_cli('compress', self.input_compress_filename, self.output_compress_filename)
        
        returncode, stdout, stderr = self.run_cli('decompress', self.output_compress_filename, self.output_decompress_filename)
        
        self.assertEqual(returncode, 0, f"Decompression failed with stderr: {stderr}")
        self.assertTrue(os.path.exists(self.output_decompress_filename), "Decompressed file was not created")

        # Verify that the decompressed file matches the original input file
        with open(self.output_decompress_filename, 'r') as f:
            decompressed_content = f.read()
        
        with open(self.input_compress_filename, 'r') as f:
            original_content = f.read()

        self.assertEqual(decompressed_content, original_content, "Decompressed content does not match original content")

if __name__ == '__main__':
    unittest.main()
