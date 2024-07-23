import unittest
from huffman_tree import HuffmanTree, HuffmanNode 

class TestHuffmanTree(unittest.TestCase):
    def setUp(self):
        # Initialize HuffmanTree with frequency_dict
        self.frequency_dict = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
        self.huffman_tree = HuffmanTree(self.frequency_dict)

    def test_build_tree(self):
        self.assertIsNotNone(self.huffman_tree.root)
        self.assertIsInstance(self.huffman_tree.root, HuffmanNode)
    
    def test_encode_tree(self):
        # Assert encoding dictionary correctness
        self.assertIsNotNone(self.huffman_tree.encodings)
        self.assertEqual(self.huffman_tree.encodings['A'], '1100')
        self.assertEqual(self.huffman_tree.encodings['B'], '1101')
        self.assertEqual(self.huffman_tree.encodings['C'], '100')
        self.assertEqual(self.huffman_tree.encodings['D'], '101')
        self.assertEqual(self.huffman_tree.encodings['E'], '111')
        self.assertEqual(self.huffman_tree.encodings['F'], '0')

if __name__ == '__main__':
    unittest.main()

