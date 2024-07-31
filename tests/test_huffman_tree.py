import unittest

from huffman_zip.huffman_tree import HuffmanNode, HuffmanTree


class TestHuffmanTree(unittest.TestCase):
    def setUp(self):
        self.frequency_dict = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
        self.huffman_tree = HuffmanTree(self.frequency_dict)

    def test_build_tree(self):
        self.assertIsNotNone(self.huffman_tree.root)
        self.assertIsInstance(self.huffman_tree.root, HuffmanNode)
    
    def test_build_encodings_tree(self):
        self.assertIsNotNone(self.huffman_tree.encodings)
        self.assertEqual(self.huffman_tree.encodings['A'], '1100')
        self.assertEqual(self.huffman_tree.encodings['B'], '1101')
        self.assertEqual(self.huffman_tree.encodings['C'], '100')
        self.assertEqual(self.huffman_tree.encodings['D'], '101')
        self.assertEqual(self.huffman_tree.encodings['E'], '111')
        self.assertEqual(self.huffman_tree.encodings['F'], '0')

    def test_encode(self):
        encoded_string = self.huffman_tree.encode('ABCDEFABCABC')
        self.assertIsInstance(encoded_string, str)
        self.assertEqual(encoded_string, '1100110110010111101100110110011001101100')

    def test_decode(self):
        decoded_string = self.huffman_tree.decode('1100110110010111101100110110011001101100')
        self.assertIsInstance(decoded_string, str)
        self.assertEqual(decoded_string, 'ABCDEFABCABC')


if __name__ == '__main__':
    unittest.main()

