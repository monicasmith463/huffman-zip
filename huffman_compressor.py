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
        output_file.write(huffman_tree.encode(data))
        output_file.close()
        self.trees[output_filepath] = huffman_tree


    def decompress_file(self, input_filepath, output_filepath):
        if input_filepath not in self.trees:
            raise Exception("Only previously compressed files can be processed at this time")
        huffman_tree = self.trees[input_filepath]

        with open(input_filepath, 'r') as input_file:
            data = input_file.read()
        output_file = open(output_filepath, 'w')
        output_file.write(huffman_tree.decode(data))
        output_file.close()