import argparse
from collections import Counter
from huffman_tree import HuffmanTree  # Assume you have implemented Huffman coding in a module

def main():
    parser = argparse.ArgumentParser(description='Compress files using Huffman coding.')
    parser.add_argument('action', choices=['compress', 'decompress'], help='Action to perform: compress or decompress')
    parser.add_argument('input_file', type=str, help='Input file to process')
    parser.add_argument('output_file', type=str, help='Output file after processing')
    
    args = parser.parse_args()

    if args.action == 'compress':
        compress_file(args.input_file, args.output_file)
    elif args.action == 'decompress':
        decompress_file(args.input_file, args.output_file)
    else:
        print("Invalid action. Valid actions are 'compress' or 'decompress'.")

def compress_file(input_filepath, output_filepath):
    with open(input_filepath, 'r') as input_file:
        data = input_file.read()
    
    frequencies = Counter(data)
    huffman_tree = HuffmanTree(frequencies)
    output_file = open(output_filepath, 'w')
    
    for char in data:
        output_file.write(huffman_tree.encodings[char])
    output_file.close()
    print(f"Compression successful. Output file: {output_file}")

def decompress_file(input_file, output_file):
    # Read compressed file
    pass

if __name__ == '__main__':
    main()
