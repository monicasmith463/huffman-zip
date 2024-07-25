from collections import Counter
from huffman_tree import HuffmanTree

class Compressor:
    def __init__(self) -> None:
        self.trees = {}

    def compress_file(self, input_filepath, output_filepath):
        with open(input_filepath, 'r') as input_file:
            data = input_file.read()
        
        frequencies = Counter(data)
        huffman_tree = HuffmanTree(frequencies)
        output_file = open(output_filepath, 'w')

        for char in data:
            output_file.write(huffman_tree.encodings[char])
        output_file.close()
        print(f"Compression successful. Output file: {output_file}")
        self.trees[output_filepath] = huffman_tree


    def decompress_file(self, input_filepath, output_filepath):
        if 
