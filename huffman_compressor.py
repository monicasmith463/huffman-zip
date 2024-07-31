from collections import Counter
from huffman_tree import HuffmanTree
from bitstring import BitArray, Bits
import os
import shelve

class Compressor:
    def compress_file(self, input_filepath, output_filepath):
        try:
            input_basename, input_file_ext = os.path.basename(input_filepath).split('.')
            output_basename, output_file_ext = os.path.basename(output_filepath).split('.')
            if input_file_ext != "txt" or output_file_ext != "bin":
                raise Exception("Invalid format. Input file must be in .txt format and output file must be in .bin format.")
            if input_basename != output_basename:
                raise Exception("Invalid filenames. Input file basename must be the same as output file basename.")
        except:
            raise Exception("Invalid format. Input file must be in .txt format and output file must be in bin format.")

        with open(input_filepath, 'r') as input_file:
            data = input_file.read()

        frequencies = Counter(data)
        huffman_tree = HuffmanTree(frequencies)
        output_file = open(output_filepath, 'wb')
        raw_encoded_data = huffman_tree.encode(data)
        raw_encoded_data_bits = BitArray(bin=raw_encoded_data)
        raw_encoded_data_bits.tofile(output_file)
        output_file.close()
        with shelve.open("persisted_trees") as db:
            input_len = len(data)
            db[input_basename] = { "huffman_tree" : huffman_tree, "input_len": input_len }

    def decompress_file(self, input_filepath, output_filepath):
        try:
            input_basename, input_file_ext = os.path.basename(input_filepath).split('.')
            output_basename, output_file_ext = os.path.basename(output_filepath).split('.')
            if input_file_ext != "bin" or output_file_ext != "txt":
                raise Exception("Invalid format. Input file must be in .bin format and output file must be in .txt format.")
        except:
            raise Exception("Invalid format. Input file must be in .bin format and output file must be in .txt format.")
        data = BitArray(filename=input_filepath).bin
        
        # we can lookup the tree in order to decompress
        with shelve.open("persisted_trees") as db:
            if input_basename not in db:
                raise Exception(f"Huffman tree for {input_filepath} not found. {input_filepath} must be a previously compressed file.")
            huffman_tree = db[input_basename]["huffman_tree"]
            input_len = db[input_basename]["input_len"]

        output_file = open(output_filepath, 'w')
        # sometimes padding is added to the end of binary data. so, we truncate any extra characters.
        decoded_data = huffman_tree.decode(data)[:input_len]
        output_file.write(decoded_data)
        output_file.close()