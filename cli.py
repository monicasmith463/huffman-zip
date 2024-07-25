import argparse
from collections import Counter
from compressor import Compressor  # Assume you have implemented Huffman coding in a module

def main():
    parser = argparse.ArgumentParser(description='Compress files using Huffman coding.')
    parser.add_argument('action', choices=['compress', 'decompress'], help='Action to perform: compress or decompress')
    parser.add_argument('input_file', type=str, help='Input file to process')
    parser.add_argument('output_file', type=str, help='Output file after processing')
    
    args = parser.parse_args()

    if args.action == 'compress':
        compressor.compress_file(args.input_file, args.output_file)
    elif args.action == 'decompress':
        compressor.decompress_file(args.input_file, args.output_file)
    else:
        print("Invalid action. Valid actions are 'compress' or 'decompress'.")

if __name__ == '__main__':
    main()
